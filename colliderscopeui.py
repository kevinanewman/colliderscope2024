# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_ColliderScopeUI


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

    def load_file_preview(self, file_pathname):
        # preview first N lines of input file
        self.ui.preview_tableWidget.setRowCount(0)
        self.ui.preview_tableWidget.setColumnCount(1)

        with open(file_pathname, 'r') as f_read:
            for i in range(0, 256):
                line = f_read.readline()
                if line:
                    self.ui.preview_tableWidget.insertRow(self.ui.preview_tableWidget.rowCount())
                    self.ui.preview_tableWidget.setItem(i-1, 1, QTableWidgetItem('%s' % line.rstrip()))

    def filepathname_changed(self):
        self.load_file_preview(self.ui.filepathname_lineEdit.text())

    def import_filebrowse(self):
        # file_pathname = file_dialog('', ['*.txt', '*.csv', '*.xls*'], 'file_dialog_title')
        file_pathname = file_dialog('', '*.*', 'file_dialog_title')
        self.ui.filepathname_lineEdit.setText(file_pathname)

        self.load_file_preview(file_pathname)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = ColliderScopeUI()
    widget.show()
    sys.exit(app.exec())
