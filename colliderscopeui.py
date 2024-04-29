# This Python file uses the following encoding: utf-8
from __init__ import *

import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
# sys.path.insert(0, os.path.join(path))  # picks up this package
sys.path.insert(0, os.path.join(path, path+os.sep+'assets'))  # picks up this package

os.chdir(path)
# print('colliderscopeui.py path = %s\n' % path)
# print('SYS Path = %s\n' % sys.path)
# print('CWD = %s\n' % os.getcwd())

import time
import pandas as pd
import numpy as np
import pyqtgraph as pg
from pyqtgraph import PlotWidget
from pyqtgraph.console import ConsoleWidget

import PySide6
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QFileDialog, QTableWidget, QTableWidgetItem, QLabel,
                               QMessageBox, QGraphicsScene, QGraphicsWidget, QGraphicsProxyWidget, QSizePolicy,
                               QVBoxLayout, QHBoxLayout)

from PySide6.QtGui import QStandardItemModel

from pythonhighlighter import PythonHighlighter

# Important:
# You need to run the following command to generate the ui_form.py file or Build/Run in Qt Creator first:
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_colliderscope import Ui_ColliderScopeUI

app = None
mainwindow = None
data = None
status_bar_message = ''
latest_item = None
latest_items = None

original_numeric_fields = []
original_string_fields = []

active_numeric_fields = []
active_string_fields = []
ignore_fields = []

pg.setConfigOptions(antialias=False)
# pg.setConfigOption('background', 'w')
# pg.setConfigOption('foreground', 'b')


def file_dialog(file_pathname, file_type_filter, file_dialog_title):
    """
    Opens a file dialog to select a file with extension options.

    :param file_pathname: Default file name
    :param file_type_filter: Specifies extension filter type
    :param file_dialog_title: Title for dialog box
    :return: User selected file name, Echo file_type, Echo file_dialog_title
    """

    dialog = QFileDialog()
    dialog.selectFile(file_pathname)
    dialog.setWindowTitle(file_dialog_title)
    dialog.setFileMode(QFileDialog.ExistingFile)
    # dialog.setFileMode(QFileDialog.AnyFile)
    if type(file_type_filter) is not list:
        dialog.setNameFilters([file_type_filter])
    else:
        dialog.setNameFilters(file_type_filter)
    dialog.setViewMode(QFileDialog.Detail)
    if dialog.exec():
        file_pathname = dialog.selectedFiles()
        file_pathname = str(file_pathname)[2:-2]
        return file_pathname
    else:
        file_pathname = ""
        return file_pathname


def get_unitized_columns(filename, sheet_name=None, ignore_units=[], encoding='utf-8', skiprows=0, units_nrows=0):
    """
    Combine column labels and units row into a single combined string to identify the column.

    Args:
        filename (str): name of the file to read
        sheet_name (str): for reading a particular Excel sheet, or ``None`` for CSV files
        ignore_units (list of str): unit values to ignore, default ``Text``
        encoding (str): file encoding (decoding) method name
        units_nrows (int): number of units rows, if any

    Returns:
        List of combined column headers and units as in ``['ColumnName_units', ...]``

    """
    if sheet_name:
        columns = pd.read_excel(filename, header=None, skiprows=skiprows, nrows=1, sheet_name=sheet_name)
        if units_nrows > 0:
            units = pd.read_excel(filename, header=None, skiprows=skiprows+1, nrows=units_nrows, sheet_name=sheet_name)
        else:
            units = pd.DataFrame({'units': [''] * columns.shape[1]}).transpose()
    else:
        columns = pd.read_csv(filename, header=None, nrows=1, skiprows=0, encoding=encoding,
                              encoding_errors='strict')
        if units_nrows > 0:
            units = pd.read_csv(filename, header=None, skiprows=1, nrows=units_nrows, encoding=encoding,
                                encoding_errors='strict')
        else:
            units = pd.DataFrame({'units': [''] * columns.shape[1]}).transpose()

    unitized_columns = []

    for col, unit in zip(columns.values[0], units.values[0]):
        if unit not in ignore_units and pd.notna(unit) and units_nrows > 0:
            unitized_columns.append('%s_%s' % (col, unit))
        else:
            unitized_columns.append('%s' % col)

    return unitized_columns


def mouseMoved(*args, **kwargs):
    print('mouseMoved', args)


def mouseHover(*args, **kwargs):
    print('mouseHover', args)


def mouseClicked(*args, **kwargs):
    print('mouseClicked', args)


def run():
    exec(mainwindow.ui.script_preview_plainTextEdit.toPlainText(), globals())


def dropEvent(event):
    item_list = [i.text() for i in event.source().selectedItems()]

    for i in item_list:
        event.source().source_data.remove(i)
        ignore_fields.append(i)

    mainwindow.ui.triage_ignore_listWidget.addItems(item_list)

    event.setDropAction(PySide6.QtCore.Qt.DropAction.MoveAction)
    event.accept()


class ColliderScopeUI(QMainWindow):
    def __init__(self, parent=None):
        global active_numeric_fields, active_string_fields, ignore_fields

        super().__init__(parent)
        self.ui = Ui_ColliderScopeUI()
        self.ui.setupUi(self)

        self.init_graphic_preview_plot_widget()

        # set up selection rectangle
        self.ui.graphic_preview_plot_widget.getViewBox().setMouseMode(pg.ViewBox.RectMode)
        self.ui.graphic_preview_plot_widget.getViewBox().rbScaleBox.setPen(pg.mkPen((64, 128, 200), width=2))
        self.ui.graphic_preview_plot_widget.getViewBox().rbScaleBox.setBrush(pg.mkBrush(81,	197, 255, 100))

        # self.ui.graphic_preview_plot_widget.plotItem.ctrlMenu # for future work...

        # self.ui.graphic_preview_plot_widget.scene().sigMouseMoved.connect(mouseMoved)
        # self.ui.graphic_preview_plot_widget.scene().sigMouseHover.connect(mouseHover)
        self.ui.graphic_preview_plot_widget.scene().sigMouseClicked.connect(mouseClicked)

        self.ui.plot_graphicsView.showGrid(x=True, y=True)

        self.ui.file_import_browse_pushButton.setFocus()

        self.hl = PythonHighlighter(self.ui.script_preview_plainTextEdit.document())

        self.ui.triage_numeric_listWidget.source_data = active_numeric_fields
        self.ui.triage_string_listWidget.source_data = active_string_fields
        self.ui.triage_ignore_listWidget.source_data = ignore_fields

        self.ui.triage_filter_widget.widget_list = \
            [self.ui.triage_numeric_listWidget, self.ui.triage_string_listWidget]

        self.ui.triage_ignore_listWidget.dropEvent = dropEvent

        self.prior_nan_count = None

        # timer.start()

    def generic_slot(self):
        print('generic slot...')

    @staticmethod
    def get_csv_help():
        doc_link = 'https://pandas.pydata.org/pandas-docs/version/%s/reference/api/pandas.read_csv.html' % pd.__version__

        if sys.platform.startswith('win'):
            os.system("start \"\" %s" % doc_link)
        else:
            os.system('open %s' % doc_link)

    @staticmethod
    def get_excel_help():
        doc_link = 'https://pandas.pydata.org/pandas-docs/version/%s/reference/api/pandas.read_excel.html' % pd.__version__

        if sys.platform.startswith('win'):
            os.system("start \"\" %s" % doc_link)
        else:
            os.system('open %s' % doc_link)

    def init_graphic_preview_plot_widget(self):
        self.ui.graphic_preview_plot_widget.plotItem.clear()
        self.ui.graphic_preview_plot_widget.showGrid(x=True, y=True)
        self.ui.graphic_preview_plot_widget.plotItem.setTitle('Graphic Preview')
        self.ui.graphic_preview_plot_widget.plotItem.showButtons()
        self.ui.graphic_preview_plot_widget.new = True

    def load_file_preview(self, qstring='', file_pathname=None):
        self.ui.file_import_browse_pushButton.clearFocus()

        if self.ui.preview_size_checkBox.isChecked():
            self.ui.preview_size_spinBox.setEnabled(True)
            num_preview_rows = self.ui.preview_size_spinBox.value()
        else:
            self.ui.preview_size_spinBox.setEnabled(False)
            num_preview_rows = None

        if file_pathname is None:
            file_pathname = self.ui.filepathname_lineEdit.text()

        if file_pathname:
            if 'xls' in file_pathname.split('.')[-1]:
                self.ui.file_import_tabWidget.setCurrentIndex(1)
                self.ui.import_excel_pushButton.setFocus()
                self.ui.import_csv_pushButton.clearFocus()

                df = self.import_excel_file(preview=True, nrows=num_preview_rows)
                if df is not None:
                    self.preview_dataframe(df, num_preview_rows)

            else:
                self.ui.file_import_tabWidget.setCurrentIndex(0)
                self.ui.import_csv_pushButton.setFocus()
                self.ui.import_excel_pushButton.clearFocus()

                # preview first N lines of input file
                self.ui.file_preview_tableWidget.setRowCount(0)
                self.ui.file_preview_tableWidget.setColumnCount(1)

                df = self.import_csv_file(preview=True, nrows=num_preview_rows)
                if df is not None:
                    self.preview_dataframe(df, num_preview_rows)
                else:
                    with open(file_pathname, 'r') as f_read:
                        for i in range(0, num_preview_rows):
                            line = f_read.readline()
                            if line:
                                self.ui.file_preview_tableWidget.insertRow(self.ui.file_preview_tableWidget.rowCount())
                                self.ui.file_preview_tableWidget.setItem(i-1, 1, QTableWidgetItem('%s' % line.rstrip()))

                        self.ui.file_preview_tableWidget.horizontalHeader().setVisible(False)
                        self.ui.file_preview_tableWidget.resizeColumnsToContents()

    def preview_dataframe(self, df, num_preview_rows):
        # Set row and column count
        self.ui.file_preview_tableWidget.setRowCount(df.shape[0])
        self.ui.file_preview_tableWidget.setColumnCount(df.shape[1])

        # Set headers
        self.ui.file_preview_tableWidget.setHorizontalHeaderLabels(df.columns)

        # Populate the table
        for i in range(df.shape[0]):
            for j in range(df.shape[1]):
                item = QTableWidgetItem(str(df.iloc[i, j]))
                self.ui.file_preview_tableWidget.setItem(i, j, item)

        self.ui.file_preview_tableWidget.horizontalHeader().setVisible(True)
        self.ui.file_preview_tableWidget.resizeColumnsToContents()

    def handle_import_button_enables(self):
        if self.ui.filepathname_lineEdit.text():
            self.ui.file_import_tabWidget.setEnabled(True)
        else:
            self.ui.file_import_tabWidget.setEnabled(False)

    def filepathname_changed(self):
        self.load_file_preview('', self.ui.filepathname_lineEdit.text())
        self.handle_import_button_enables()

    def import_filebrowse(self):
        # file_pathname = file_dialog('', ['*.txt', '*.csv', '*.xls*'], 'file_dialog_title')
        file_pathname = file_dialog('', '*.*', 'file_dialog_title')
        self.ui.filepathname_lineEdit.setText(file_pathname)
        self.ui.import_excel_sheet_comboBox.clear()
        self.handle_import_button_enables()

        self.load_file_preview('', file_pathname)

    def update_string_preview(self, force=False):
        global latest_item, latest_items

        if self.ui.preview_tabWidget.currentIndex() != 2 or force:
            self.ui.preview_tabWidget.setCurrentIndex(0)

        self.ui.triage_numeric_listWidget.clearSelection()
        self.ui.triage_ignore_listWidget.clearSelection()

        if self.ui.triage_string_listWidget.selectedItems():
            latest_items = [i.text() for i in self.ui.triage_string_listWidget.selectedItems()]
            latest_item = self.ui.triage_string_listWidget.selectedItems()[-1].text()
            self.ui.text_preview_listWidget.clear()
            self.ui.text_preview_listWidget.addItems(data[latest_item].unique())

    def force_string_preview(self):
        print('force_string_preview')
        self.update_string_preview(force=True)

    def update_numeric_preview(self, force=False):
        global latest_item, latest_items

        self.ui.triage_string_listWidget.clearSelection()
        self.ui.triage_ignore_listWidget.clearSelection()

        if force:
            self.ui.preview_tabWidget.setCurrentIndex(1)

        if self.ui.triage_numeric_listWidget.selectedItems():
            latest_items = [i.text() for i in self.ui.triage_numeric_listWidget.selectedItems()]
            latest_item = self.ui.triage_numeric_listWidget.selectedItems()[-1].text()
            self.ui.text_preview_listWidget.clear()
            self.ui.text_preview_listWidget.addItems([str(d) for d in data[latest_item].unique()])

            nan_count = sum(data[latest_item].isna())

            if self.ui.graphic_preview_plot_widget.new or nan_count != self.prior_nan_count:
                # self.ui.graphic_preview_plot_widget.plot(data[latest_item].values, pen=None,
                #                                      symbolBrush=(231, 232, 255), symbolPen=(231, 232, 255), symbol='o',
                #                                      symbolSize=1.5, clear=True)
                # self.ui.graphic_preview_plot_widget.plot(data[latest_item].values, pen=None,
                #                                      symbolBrush=None, symbolPen=(231, 232, 255), symbol='t1',
                #                                      symbolSize=4, clear=True)

                # self.ui.graphic_preview_plot_widget.plot(data[latest_item].values, pen=(231, 232, 255), clear=True)

                if sum(data[latest_item].isna()) > 0 or len(data[latest_item]) == 1:
                    self.ui.graphic_preview_plot_widget.plot(data[latest_item].values, pen='#00000000',
                                                             symbolBrush=None, symbolPen=(231, 232, 255),
                                                             symbol='t1', symbolSize=4, clear=True)
                    text = pg.TextItem(
                        html='<div style="text-align: center"><span style="color: #FFF;'
                             '"<span style="color: #FF0; font-size: 16pt;">%d NaNs</span></div>' % nan_count,
                        anchor=(-0.3, 0.5), border='w', fill=(255, 80, 80, 100))
                    self.ui.graphic_preview_plot_widget.addItem(text)
                    text.setPos(0, data[latest_item].max())
                else:
                    self.ui.graphic_preview_plot_widget.plot(data[latest_item].values, pen=(231, 232, 255),
                                                             clear=True)

                self.ui.graphic_preview_plot_widget.new = False
            else:
                self.ui.graphic_preview_plot_widget.plotItem.curves[0].setData(data[latest_item].values)

            self.ui.graphic_preview_plot_widget.plotItem.setTitle(latest_item)
            self.ui.graphic_preview_plot_widget.plotItem.autoRange()
            # maybe do this if len(data) > X?
            # self.ui.graphic_preview_plot_widget.setDownsampling(auto=True, mode='peak')

            self.prior_nan_count = nan_count

    def force_numeric_preview(self):
        print('force_numeric_preview')
        self.update_numeric_preview(force=True)

    def update_triage_lists(self):
        global data
        data = data.convert_dtypes()
        active_numeric_fields.clear()
        active_string_fields.clear()
        ignore_fields.clear()

        active_numeric_fields.extend(data.select_dtypes(exclude=['string', 'object']).columns)
        active_string_fields.extend(data.select_dtypes(include='string').columns)

        self.ui.triage_numeric_listWidget.clear()
        self.ui.triage_numeric_listWidget.addItems(active_numeric_fields)
        self.ui.triage_string_listWidget.clear()
        self.ui.triage_string_listWidget.addItems(active_string_fields)
        self.ui.triage_ignore_listWidget.clear()

    def setup_initial_triage_lists(self):
        global data
        self.ui.triage_tab.setEnabled(True)
        self.ui.tabWidget_main.setCurrentIndex(1)
        self.update_triage_lists()
        # grab non-filtered original fields for later reference:
        original_numeric_fields.extend(active_numeric_fields)
        original_string_fields.extend(active_string_fields)

    def import_csv_file(self, preview=False, nrows=False):
        global status_bar_message, data

        file_pathname = self.ui.filepathname_lineEdit.text()

        if file_pathname:
            self.init_on_import()

            delimiter = self.ui.import_csv_delimiter_comboBox.currentText()
            if delimiter == 'Auto':
                delimiter = None

            try:
                if self.ui.import_csv_two_row_header_comboBox.currentText() == 'False':
                    units_nrows = 0
                else:
                    units_nrows = 1
                    self.ui.import_csv_skip_rows_lineEdit.setText('[0, 1]')

                skiprows = self.ui.import_csv_skip_rows_lineEdit.text()
                if skiprows.startswith('[') and skiprows.endswith(']'):
                    skiprows = eval(skiprows)
                else:
                    skiprows = int(skiprows)

                unitized_columns = get_unitized_columns(self.ui.filepathname_lineEdit.text(),
                                                        encoding=self.ui.import_csv_encoding_comboBox.currentText(),
                                                        skiprows=skiprows, units_nrows=units_nrows)

                if preview:
                    try:
                        df = pd.read_csv(self.ui.filepathname_lineEdit.text(), names=unitized_columns, header=0,
                                         delimiter=delimiter,
                                         encoding=self.ui.import_csv_encoding_comboBox.currentText(),
                                         skip_blank_lines=self.ui.import_csv_skip_blank_lines_comboBox.currentText(),
                                         skiprows=skiprows,
                                         nrows=nrows,
                                         )
                    except:
                        df = pd.read_csv(self.ui.filepathname_lineEdit.text(), header=0,
                                         delimiter=delimiter,
                                         encoding=self.ui.import_csv_encoding_comboBox.currentText(),
                                         skip_blank_lines=self.ui.import_csv_skip_blank_lines_comboBox.currentText(),
                                         skiprows=skiprows,
                                         nrows=nrows,
                                         )
                else:
                    df = pd.read_csv(self.ui.filepathname_lineEdit.text(), names=unitized_columns, header=0,
                                     delimiter=delimiter,
                                     encoding=self.ui.import_csv_encoding_comboBox.currentText(),
                                     skip_blank_lines=self.ui.import_csv_skip_blank_lines_comboBox.currentText(),
                                     skiprows=skiprows,
                                     )
                    data = df
                    self.setup_initial_triage_lists()

                self.ui.statusbar.showMessage('imported %d rows of data, %d columns' %
                                              (len(df), len(df.columns)), 10000)

                self.ui.script_preview_consoleWidget.locals().update(globals())
                self.ui.script_preview_consoleWidget.output.setPlainText('use run() to run user script!\n')

                return df

            except Exception as e:
                QMessageBox(QMessageBox.Icon.Critical, 'CSV Import Error', 'Error reading "%s"\n\n%s' %
                            (file_pathname, str(e))).exec()
                return None

    def import_excel_file(self, preview=False, nrows=False):
        global status_bar_message, data

        file_pathname = self.ui.filepathname_lineEdit.text()

        if file_pathname:
            self.init_on_import()

            if self.ui.import_excel_sheet_comboBox.count() == 0:
                from openpyxl import load_workbook
                wb = load_workbook(filename=self.ui.filepathname_lineEdit.text(), read_only=True)
                self.ui.import_excel_sheet_comboBox.addItems(wb.sheetnames)
                self.ui.import_excel_sheet_comboBox.setCurrentIndex(0)

            sheet_name = self.ui.import_excel_sheet_comboBox.currentText()

            header = self.ui.import_excel_header_lineEdit.text()
            if header == 'None':
                header = None
            elif header.startswith('[') and header.endswith(']'):
                header = eval(header)
            else:
                header = int(header)

            try:
                if nrows is False:
                    nrows = None

                if self.ui.import_excel_two_row_header_comboBox.currentText() == 'False':
                    units_nrows = 0
                else:
                    units_nrows = 1
                    self.ui.import_excel_skip_rows_lineEdit.setText('[0, 1]')

                skiprows = self.ui.import_excel_skip_rows_lineEdit.text()
                if skiprows.startswith('[') and skiprows.endswith(']'):
                    skiprows = eval(skiprows)
                else:
                    skiprows = int(skiprows)

                unitized_columns = get_unitized_columns(self.ui.filepathname_lineEdit.text(), sheet_name=sheet_name,
                                                        skiprows=skiprows, units_nrows=units_nrows)

                engine_kwargs = {'read_only': preview is True}
                df = pd.read_excel(self.ui.filepathname_lineEdit.text(), names=unitized_columns, sheet_name=sheet_name,
                                     skiprows=skiprows, header=header, nrows=nrows, engine_kwargs=engine_kwargs,
                                     )

                self.ui.statusbar.showMessage('imported %d rows of df, %d columns' %
                                              (len(df), len(df.columns)), 10000)

                self.ui.script_preview_consoleWidget.locals().update(globals())
                self.ui.script_preview_consoleWidget.output.setPlainText('use run() to run user script!\n')

                if not preview:
                    data = df
                    self.setup_initial_triage_lists()

                return df

            except Exception as e:
                QMessageBox(QMessageBox.Icon.Critical, 'Excel Import Error', 'Error reading "%s"\n\n%s' %
                            (file_pathname, str(e))).exec()
                return None

    def init_on_import(self):
        original_numeric_fields.clear()
        original_string_fields.clear()
        active_numeric_fields.clear()
        active_string_fields.clear()
        ignore_fields.clear()
        self.init_graphic_preview_plot_widget()

    def script_run(self):
        self.ui.script_preview_consoleWidget.repl.runCmd('run()')
        # update consoleWidget namespace in case new vars created:
        self.ui.script_preview_consoleWidget.locals().update(globals())
        # update triage lists in case new fields created:
        self.update_triage_lists()

    def script_open(self):
        file_pathname = file_dialog('', '*.py', 'Load triage script')
        if file_pathname:
            with open(file_pathname, 'r') as f_read:
                self.ui.script_preview_plainTextEdit.setPlainText(f_read.read())

    def script_save(self):
        file_pathname = QFileDialog().getSaveFileName(self, 'Save triage script', os.getcwd(), '*.py', '*.py')[0]

        if file_pathname:
            with open(file_pathname, 'w') as f_write:
                f_write.write(self.ui.script_preview_plainTextEdit.toPlainText())

    def add_to_script(self):
        if latest_items:
            for i in latest_items:
                self.ui.script_preview_plainTextEdit.insertPlainText("data['%s']\n" % i)
        elif latest_item:
            self.ui.script_preview_plainTextEdit.insertPlainText("data['%s']" % latest_item)

        self.ui.preview_tabWidget.setCurrentIndex(2)


def status_bar():
    # print(time.time())
    # if widget:
    #     widget.ui.statusbar.showMessage(status_bar_message, 1000)
    pass


def run_colliderscope():
    global app, mainwindow
    import multitimer
    timer = multitimer.MultiTimer(interval=1, function=status_bar)
    app = QApplication(sys.argv)

    # set app style
    app.setStyle("Fusion")

    # customize tooltip style
    app.setStyleSheet("QToolTip {color: #ffffff; background-color: #402a82da; border: 2px solid black; "
                      "border-radius: 10px; padding: 2.5px; margin: 0px}")
    # app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; opacity: 200; "
    #                   "border: 2px solid black; border-radius: 10px; padding: 2.5px; margin: 0px}")

    mainwindow = ColliderScopeUI()
    mainwindow.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    run_colliderscope()

# self.ui.graphic_preview_plot_widget.getViewBox().rbScaleBox.setPen(pg.mkPen((64, 128, 200), width=2)) #4080C8
# self.ui.graphic_preview_plot_widget.getViewBox().rbScaleBox.setBrush(pg.mkBrush(81, 197, 255, 100)) #51c5ff64