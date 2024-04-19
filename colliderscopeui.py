# This Python file uses the following encoding: utf-8
import sys
import time
import pandas as pd

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidget, QTableWidgetItem, QLabel, QMessageBox

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_ColliderScopeUI


app = None
widget = None
data = None
status_bar_message = ''


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


class ColliderScopeUI(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ColliderScopeUI()
        self.ui.setupUi(self)
        # timer.start()

    def load_file_preview(self, file_pathname):
        if 'xls' in file_pathname.split('.')[-1]:
            self.ui.file_import_tabWidget.setCurrentIndex(1)
            # need some way to preview Excel files...?
            self.ui.file_preview_tableWidget.clearContents()
            while self.ui.file_preview_tableWidget.rowCount() > 1:
                self.ui.file_preview_tableWidget.removeRow(0)
        else:
            self.ui.file_import_tabWidget.setCurrentIndex(0)

            # preview first N lines of input file
            self.ui.file_preview_tableWidget.setRowCount(0)
            self.ui.file_preview_tableWidget.setColumnCount(1)

            with open(file_pathname, 'r') as f_read:
                for i in range(0, 256):
                    line = f_read.readline()
                    if line:
                        self.ui.file_preview_tableWidget.insertRow(self.ui.file_preview_tableWidget.rowCount())
                        self.ui.file_preview_tableWidget.setItem(i-1, 1, QTableWidgetItem('%s' % line.rstrip()))

    def filepathname_changed(self):
        self.load_file_preview(self.ui.filepathname_lineEdit.text())

    def import_filebrowse(self):
        # file_pathname = file_dialog('', ['*.txt', '*.csv', '*.xls*'], 'file_dialog_title')
        file_pathname = file_dialog('', '*.*', 'file_dialog_title')
        self.ui.filepathname_lineEdit.setText(file_pathname)

        self.load_file_preview(file_pathname)

    def import_csv_file(self):
        global status_bar_message, data

        print('import CSV file here!!')
        file_pathname = self.ui.filepathname_lineEdit.text()

        if file_pathname:
            delimiter = self.ui.import_csv_delimiter_comboBox.currentText()
            if delimiter == 'Auto':
                delimiter = None

            skiprows = self.ui.import_csv_skip_rows_lineEdit.text()
            if skiprows.startswith('[') and skiprows.endswith(']'):
                skiprows = eval(skiprows)
            else:
                skiprows = int(skiprows)

            try:
                data = pd.read_csv(self.ui.filepathname_lineEdit.text(),
                               delimiter=delimiter,
                               encoding=self.ui.import_csv_encoding_comboBox.currentText(),
                               skip_blank_lines=self.ui.import_csv_skip_blank_lines_comboBox.currentText(),
                               skiprows=skiprows
                               )
            except Exception as e:
                QMessageBox(QMessageBox.Icon.Critical, 'CSV Import Error', 'Error reading "%s"\n\n%s' %
                            (file_pathname, repr(e))).exec()

            self.ui.statusbar.showMessage('imported %d rows of data, %d columns' % (len(data), len(data.columns)), 2000)
            print(data.columns)
            print(data.head())
        else:
            self.ui.statusbar.showMessage('WARNING: select an input file first', 2000)

    def import_excel_file(self):
        global status_bar_message, data

        print('import EXCEL file here!!')
        file_pathname = self.ui.filepathname_lineEdit.text()

        if file_pathname:
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
                data = pd.read_excel(self.ui.filepathname_lineEdit.text(),
                                     sheet_name=sheet,
                                     skiprows=skiprows,
                                     header=header,
                                     )
                self.ui.statusbar.showMessage('imported %d rows of data, %d columns' % (len(data), len(data.columns)), 2000)
                print(data.columns)
                print(data.head())
            except Exception as e:
                QMessageBox(QMessageBox.Icon.Critical, 'Excel Import Error', 'Error reading "%s"\n\n%s' %
                            (file_pathname, repr(e))).exec()
        else:
            self.ui.statusbar.showMessage('WARNING: select an input file first', 2000)


def status_bar():
    # print(time.time())
    # if widget:
    #     widget.ui.statusbar.showMessage(status_bar_message, 1000)
    pass


if __name__ == "__main__":
    import multitimer

    timer = multitimer.MultiTimer(interval=1, function=status_bar)

    app = QApplication(sys.argv)
    widget = ColliderScopeUI()
    widget.show()
    sys.exit(app.exec())
