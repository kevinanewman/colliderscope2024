# This Python file uses the following encoding: utf-8
import os, sys

from PySide6.QtWidgets import QApplication, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic filterwidget.ui -o ui_filterwidget.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_filterwidget import Ui_FilterWidget


class FilterWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_FilterWidget()
        self.ui.setupUi(self)
        self.widget_list = []

    def addListWidgets(self, widget_list):
        self.widget_list = widget_list

    def inputChanged(self):
        if self.ui.not_pushButton.isChecked():
            invert = 'not'
        else:
            invert = ''

        if (self.ui.cc_pushButton.isChecked() or
                (self.ui.comboBox.currentText() == 'contains' and self.ui.w_pushButton.isChecked())):
            case_modifier = ''
        else:
            case_modifier = '.lower()'

        if self.ui.w_pushButton.isChecked():
            compare = '=='
        else:
            compare = 'in'

        for lw in self.widget_list:
            # print(lw.source_data)
            lw.clear()

            if self.ui.comboBox.currentText() == 'contains':
                string_fun = ''
                self.ui.w_pushButton.setEnabled(True)
            elif self.ui.comboBox.currentText() == 'starts with':
                string_fun = '.startswith'
                self.ui.w_pushButton.setEnabled(False)
            else:  # self.ui.comboBox.currentText() == 'ends with':
                string_fun = '.endswith'
                self.ui.w_pushButton.setEnabled(False)

            if string_fun:
                fields = eval(
                    f'[f for f in lw.source_data if {invert} f{case_modifier}{string_fun}(self.ui.lineEdit.text(){case_modifier})]'.format(), locals())
            else:
                fields = eval(
                    f'[f for f in lw.source_data if {invert} (self.ui.lineEdit.text(){case_modifier} {compare} f{case_modifier})]'.format(), locals())

            lw.addItems(fields)

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
