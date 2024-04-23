# This Python file uses the following encoding: utf-8
from __init__ import *

import os
import sys

path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(path))  # picks up sub-packages
# sys.path.insert(0, os.path.join(path))  # picks up omega_model sub-packages

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

from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QFileDialog, QTableWidget, QTableWidgetItem, QLabel,
                               QMessageBox, QGraphicsScene, QGraphicsWidget, QGraphicsProxyWidget, QSizePolicy,
                               QVBoxLayout, QHBoxLayout)

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

numeric_fields = ['num']
string_fields = ['str']
ignore_fields = ['ignore']

pg.setConfigOptions(antialias=False)
# pg.setConfigOption('background', 'w')
# pg.setConfigOption('foreground', 'b')


def file_dialog(file_pathname, file_type_filter, file_dialog_title, mode='open'):
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
    if mode == 'open':
        dialog.setFileMode(QFileDialog.ExistingFile)
    else:
        dialog.setAcceptMode(QFileDialog.AcceptSave)
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


def mouseMoved(*args, **kwargs):
    print('mouseMoved', args)


def mouseHover(*args, **kwargs):
    print('mouseHover', args)


def mouseClicked(*args, **kwargs):
    print('mouseClicked', args)


def run():
    exec(mainwindow.ui.script_preview_plainTextEdit.toPlainText(), globals())


class ColliderScopeUI(QMainWindow):
    def __init__(self, parent=None):
        global numeric_fields, string_fields, ignore_fields

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

        self.ui.triage_numeric_listWidget.source_data = numeric_fields
        self.ui.triage_string_listWidget.source_data = string_fields
        self.ui.triage_ignore_listWidget.source_data = ignore_fields

        self.ui.triage_filter_widget.widget_list = \
            [self.ui.triage_numeric_listWidget, self.ui.triage_string_listWidget]

        # timer.start()

    def init_graphic_preview_plot_widget(self):
        self.ui.graphic_preview_plot_widget.plotItem.clear()
        self.ui.graphic_preview_plot_widget.showGrid(x=True, y=True)
        self.ui.graphic_preview_plot_widget.plotItem.setTitle('Graphic Preview')
        self.ui.graphic_preview_plot_widget.plotItem.showButtons()
        self.ui.graphic_preview_plot_widget.new = True

    def load_file_preview(self, file_pathname=None):
        self.ui.file_import_browse_pushButton.clearFocus()

        num_preview_rows = 256

        if file_pathname is None:
            file_pathname = self.ui.filepathname_lineEdit.text()

        if 'xls' in file_pathname.split('.')[-1]:
            self.ui.file_import_tabWidget.setCurrentIndex(1)
            self.ui.import_excel_pushButton.setFocus()
            self.ui.import_csv_pushButton.clearFocus()

            df = self.import_excel_file(nrows=num_preview_rows)
            if df is not None:
                self.preview_dataframe(df, num_preview_rows)

        else:
            self.ui.file_import_tabWidget.setCurrentIndex(0)
            self.ui.import_csv_pushButton.setFocus()
            self.ui.import_excel_pushButton.clearFocus()

            # preview first N lines of input file
            self.ui.file_preview_tableWidget.setRowCount(0)
            self.ui.file_preview_tableWidget.setColumnCount(1)

            df = self.import_csv_file(nrows=num_preview_rows)
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
        self.load_file_preview(self.ui.filepathname_lineEdit.text())
        self.handle_import_button_enables()

    def import_filebrowse(self):
        # file_pathname = file_dialog('', ['*.txt', '*.csv', '*.xls*'], 'file_dialog_title')
        file_pathname = file_dialog('', '*.*', 'file_dialog_title')
        self.ui.filepathname_lineEdit.setText(file_pathname)
        self.handle_import_button_enables()

        self.load_file_preview(file_pathname)

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

            if self.ui.graphic_preview_plot_widget.new:
                # self.ui.graphic_preview_plot_widget.plot(data[latest_item].values, pen=None,
                #                                      symbolBrush=(231, 232, 255), symbolPen=(231, 232, 255), symbol='o',
                #                                      symbolSize=1.5, clear=True)
                # self.ui.graphic_preview_plot_widget.plot(data[latest_item].values, pen=None,
                #                                      symbolBrush=None, symbolPen=(231, 232, 255), symbol='t1',
                #                                      symbolSize=4, clear=True)

                # self.ui.graphic_preview_plot_widget.plot(data[latest_item].values, pen=(231, 232, 255), clear=True)

                self.ui.graphic_preview_plot_widget.plot(data[latest_item].values, pen=None, symbolBrush=None,
                                                         symbolPen=(231, 232, 255), symbol='t1', symbolSize=4) # , clear=True)

                self.ui.graphic_preview_plot_widget.new = False
            else:
                self.ui.graphic_preview_plot_widget.plotItem.curves[0].setData(data[latest_item].values)

            self.ui.graphic_preview_plot_widget.plotItem.autoRange()
            self.ui.graphic_preview_plot_widget.plotItem.setTitle(latest_item)
            # maybe do this if len(data) > X?
            # self.ui.graphic_preview_plot_widget.setDownsampling(auto=True, mode='peak')

    def force_numeric_preview(self):
        print('force_numeric_preview')
        self.update_numeric_preview(force=True)

    def update_triage_lists(self):
        global data
        data = data.convert_dtypes()
        numeric_fields.clear()
        string_fields.clear()

        numeric_fields.extend(data.select_dtypes(exclude='string').columns)
        string_fields.extend(data.select_dtypes(include='string').columns)

        self.ui.triage_numeric_listWidget.clear()
        self.ui.triage_numeric_listWidget.addItems(numeric_fields)
        self.ui.triage_string_listWidget.clear()
        self.ui.triage_string_listWidget.addItems(string_fields)

    def setup_initial_triage_lists(self):
        global data
        self.ui.triage_tab.setEnabled(True)
        self.ui.tabWidget_main.setCurrentIndex(1)
        self.update_triage_lists()

    def import_csv_file(self, nrows=False):
        global status_bar_message, data

        self.init_graphic_preview_plot_widget()

        file_pathname = self.ui.filepathname_lineEdit.text()

        delimiter = self.ui.import_csv_delimiter_comboBox.currentText()
        if delimiter == 'Auto':
            delimiter = None

        skiprows = self.ui.import_csv_skip_rows_lineEdit.text()
        if skiprows.startswith('[') and skiprows.endswith(']'):
            skiprows = eval(skiprows)
        else:
            skiprows = int(skiprows)

        try:
            if nrows is False:  # nrows can be False coming from Qt for some reason
                data = pd.read_csv(self.ui.filepathname_lineEdit.text(),
                                   delimiter=delimiter,
                                   encoding=self.ui.import_csv_encoding_comboBox.currentText(),
                                   skip_blank_lines=self.ui.import_csv_skip_blank_lines_comboBox.currentText(),
                                   skiprows=skiprows,
                                   )
                self.setup_initial_triage_lists()
            else: # just reading in a preview
                data = pd.read_csv(self.ui.filepathname_lineEdit.text(),
                                   delimiter=delimiter,
                                   encoding=self.ui.import_csv_encoding_comboBox.currentText(),
                                   skip_blank_lines=self.ui.import_csv_skip_blank_lines_comboBox.currentText(),
                                   skiprows=skiprows,
                                   nrows=nrows,
                                   )

            self.ui.statusbar.showMessage('imported %d rows of data, %d columns' %
                                          (len(data), len(data.columns)), 10000)

            self.ui.script_preview_consoleWidget.locals().update(globals())
            self.ui.script_preview_consoleWidget.output.setPlainText('use run() to run user script!\n')

            return data

        except Exception as e:
            QMessageBox(QMessageBox.Icon.Critical, 'CSV Import Error', 'Error reading "%s"\n\n%s' %
                        (file_pathname, str(e))).exec()
            return None

    def import_excel_file(self, nrows=False):
        global status_bar_message, data

        self.init_graphic_preview_plot_widget()

        file_pathname = self.ui.filepathname_lineEdit.text()

        skiprows = self.ui.import_excel_skip_rows_lineEdit.text()
        if skiprows.startswith('[') and skiprows.endswith(']'):
            skiprows = eval(skiprows)
        else:
            skiprows = int(skiprows)

        sheet = self.ui.import_excel_sheet_lineEdit.text()
        if sheet.startswith('[') and sheet.endswith(']') or str.isnumeric(sheet):
            sheet = eval(sheet)

        header = self.ui.import_excel_header_lineEdit.text()
        if header == 'None':
            header = None
        elif header.startswith('[') and header.endswith(']'):
            header = eval(sheet)
        else:
            header = int(header)

        try:
            if nrows is False:
                nrows = None

            data = pd.read_excel(self.ui.filepathname_lineEdit.text(),
                                 sheet_name=sheet,
                                 skiprows=skiprows,
                                 header=header,
                                 nrows=nrows,
                                 )

            if nrows is None:
                self.setup_initial_triage_lists()

            self.ui.statusbar.showMessage('imported %d rows of data, %d columns' %
                                          (len(data), len(data.columns)), 10000)

            self.ui.script_preview_consoleWidget.locals().update(globals())
            self.ui.script_preview_consoleWidget.output.setPlainText('use run() to run user script!\n')

            return data

        except Exception as e:
            QMessageBox(QMessageBox.Icon.Critical, 'Excel Import Error', 'Error reading "%s"\n\n%s' %
                        (file_pathname, str(e))).exec()
            return None

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