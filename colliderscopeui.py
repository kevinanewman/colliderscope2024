# This Python file uses the following encoding: utf-8
import sys
import time
import pandas as pd
import numpy as np
import pyqtgraph as pg
from pyqtgraph import PlotWidget
from pyqtgraph.console import ConsoleWidget

from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QFileDialog, QTableWidget, QTableWidgetItem, QLabel,
                               QMessageBox, QGraphicsScene, QGraphicsWidget, QGraphicsProxyWidget, QSizePolicy,
                               QVBoxLayout, QHBoxLayout)

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_ColliderScopeUI


app = None
mainwindow = None
data = None
status_bar_message = ''

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


def mouseMoved(*args, **kwargs):
    print('mouseMoved', args)


def mouseHover(*args, **kwargs):
    print('mouseHover', args)


def mouseClicked(*args, **kwargs):
    print('mouseClicked', args)


def run():
    exec(mainwindow.ui.script_preview_plainTextEdit.toPlainText())


class ColliderScopeUI(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ColliderScopeUI()
        self.ui.setupUi(self)

        self.ui.graphic_preview_plot_widget.showGrid(x=True, y=True)
        self.ui.graphic_preview_plot_widget.plotItem.setTitle('Graphic Preview')
        self.ui.graphic_preview_plot_widget.plotItem.showButtons()

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

        # timer.start()

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

    def update_string_preview(self):
        latest_item = self.ui.triage_string_listWidget.selectedItems()[-1].text()
        self.ui.text_preview_listWidget.clear()
        self.ui.text_preview_listWidget.addItems(data[latest_item].unique())

    def update_numeric_preview(self):
        latest_item = self.ui.triage_numeric_listWidget.selectedItems()[-1].text()
        self.ui.text_preview_listWidget.clear()
        self.ui.text_preview_listWidget.addItems([str(d) for d in data[latest_item].unique()])
        if not self.ui.graphic_preview_plot_widget.plotItem.curves:
            # self.ui.graphic_preview_plot_widget.plot(data[latest_item].values, pen=None,
            #                                      symbolBrush=(231, 232, 255), symbolPen=(231, 232, 255), symbol='o',
            #                                      symbolSize=1.5, clear=True)
            self.ui.graphic_preview_plot_widget.plot(data[latest_item].values, pen=(231, 232, 255), clear=True)
        else:
            self.ui.graphic_preview_plot_widget.plotItem.curves[0].setData(data[latest_item].values)
        self.ui.graphic_preview_plot_widget.plotItem.autoRange()
        self.ui.graphic_preview_plot_widget.plotItem.setTitle(latest_item)
        # maybe do this if len(data) > X?
        # self.ui.graphic_preview_plot_widget.setDownsampling(auto=True, mode='peak')

    def setup_initial_triage_lists(self):
        global data
        self.ui.triage_tab.setEnabled(True)
        self.ui.tabWidget_main.setCurrentIndex(1)
        data = data.convert_dtypes()
        non_string_columns = data.select_dtypes(exclude='string').columns
        string_columns = data.select_dtypes(include='string').columns
        self.ui.triage_numeric_listWidget.clear()
        self.ui.triage_numeric_listWidget.addItems(non_string_columns)
        self.ui.triage_string_listWidget.clear()
        self.ui.triage_string_listWidget.addItems(string_columns)

    def import_csv_file(self, nrows=False):
        global status_bar_message, data

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


def status_bar():
    # print(time.time())
    # if widget:
    #     widget.ui.statusbar.showMessage(status_bar_message, 1000)
    pass


if __name__ == "__main__":
    import multitimer

    timer = multitimer.MultiTimer(interval=1, function=status_bar)

    app = QApplication(sys.argv)
    mainwindow = ColliderScopeUI()
    mainwindow.show()
    sys.exit(app.exec())
