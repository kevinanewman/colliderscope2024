# This Python file uses the following encoding: utf-8
import os, sys

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_filterwidget import Ui_FilterWidget


class FilterWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_FilterWidget()
        self.ui.setupUi(self)
        self.widget_list = None

    def addListWidgets(self, widget_list):
        self.widget_list = widget_list

    def inputChanged(self):
        print('inputChanged')

    def goto_settings(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def goto_filter(self):
        self.ui.stackedWidget.setCurrentIndex(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    widget = FilterWidget()
    widget.show()
    sys.exit(app.exec())
