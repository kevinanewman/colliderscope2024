# This Python file uses the following encoding: utf-8
import os
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
# You need to run the following command to generate the ui_form.py file or Build/Run in Qt Creator first:
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_ColliderScopeUI



# for syntax highlighting:
import keyword
import re
from PySide6 import QtWidgets
from PySide6.QtGui import QSyntaxHighlighter, QTextCharFormat, QFont
from PySide6.QtCore import QRegularExpression
import darkdetect


def charFormat(color, style='', background=None):
    """
    Return a QTextCharFormat with the given attributes.
    """
    _color = pg.functions.mkColor(color)

    _format = QTextCharFormat()
    _format.setForeground(_color)
    if 'bold' in style:
        _format.setFontWeight(QFont.Weight.Bold)
    if 'italic' in style:
        _format.setFontItalic(True)
    if background is not None:
        _format.setBackground(pg.mkColor(background))

    return _format


class LightThemeColors:
    Red = "#B71C1C"
    Pink = "#FCE4EC"
    Purple = "#4A148C"
    DeepPurple = "#311B92"
    Indigo = "#1A237E"
    Blue = "#0D47A1"
    LightBlue = "#01579B"
    Cyan = "#2CA9D2"  # "#80DEEA"
    Teal = "#004D40"
    Green = "#1B5E20"
    LightGreen = "#33691E"
    Lime = "#827717"
    Yellow = "#F57F17"
    Amber = "#FF6F00"
    Orange = "#E65100"
    DeepOrange = "#BF360C"
    Brown = "#3E2723"
    Grey = "#212121"
    BlueGrey = "#263238"


class DarkThemeColors:
    Red = "#F44336"
    Pink = "#F48FB1"
    Purple = "#CE93D8"
    DeepPurple = "#B39DDB"
    Indigo = "#9FA8DA"
    Blue = "#90CAF9"
    LightBlue = "#81D4FA"
    Cyan = "#2CA9D2"  # "#80DEEA"
    Teal = "#80CBC4"
    Green = "#A5D6A7"
    LightGreen = "#C5E1A5"
    Lime = "#E6EE9C"
    Yellow = "#FFF59D"
    Amber = "#FFE082"
    Orange = "#FFCC80"
    DeepOrange = "#FFAB91"
    Brown = "#BCAAA4"
    Grey = "#EEEEEE"
    BlueGrey = "#B0BEC5"


LIGHT_STYLES = {
    'keyword': charFormat(LightThemeColors.Blue, 'bold'),
    'operator': charFormat(LightThemeColors.Red, 'bold'),
    'brace': charFormat(LightThemeColors.Purple),
    'defclass': charFormat(LightThemeColors.Indigo, 'bold'),
    'string': charFormat(LightThemeColors.Cyan),
    'string2': charFormat(LightThemeColors.DeepPurple),
    'comment': charFormat(LightThemeColors.Red, 'italic'),
    'self': charFormat(LightThemeColors.Blue, 'bold'),
    'numbers': charFormat(LightThemeColors.Blue),
}

DARK_STYLES = {
    'keyword': charFormat(DarkThemeColors.Blue, 'bold'),
    'operator': charFormat(DarkThemeColors.Red, 'bold'),
    'brace': charFormat(DarkThemeColors.Purple),
    'defclass': charFormat(DarkThemeColors.Indigo, 'bold'),
    'string': charFormat(DarkThemeColors.Cyan),
    'string2': charFormat(DarkThemeColors.DeepPurple),
    'comment': charFormat(DarkThemeColors.DeepOrange, 'italic'),
    'self': charFormat(DarkThemeColors.LightBlue, 'bold'),
    'numbers': charFormat(DarkThemeColors.LightBlue),
}


class PythonHighlighter(QSyntaxHighlighter):
    """Syntax highlighter for the Python language.
    """
    # Python keywords
    keywords = keyword.kwlist

    # Python operators
    operators = [
        r'=',
        # Comparison
        r'==', r'!=', r'<', r'<=', r'>', r'>=',
        # Arithmetic
        r'\+', r"-", r'\*', r'/', r'//', r'%', r'\*\*',
        # In-place
        r'\+=', r'-=', r'\*=', r'/=', r'\%=',
        # Bitwise
        r'\^', r'\|', r'&', r'~', r'>>', r'<<',
    ]

    # Python braces
    braces = [
        r'\{', r'\}', r'\(', r'\)', r'\[', r'\]',
    ]

    def __init__(self, document):
        super().__init__(document)

        # Multi-line strings (expression, flag, style)
        self.tri_single = (QRegularExpression("'''"), 1, 'string2')
        self.tri_double = (QRegularExpression('"""'), 2, 'string2')

        rules = []

        # Keyword, operator, and brace rules
        rules += [(r'\b%s\b' % w, 0, 'keyword')
                  for w in PythonHighlighter.keywords]
        # rules += [(o, 0, 'operator')
        #           for o in PythonHighlighter.operators]
        # rules += [(b, 0, 'brace')
        #           for b in PythonHighlighter.braces]

        # All other rules
        rules += [
            # 'self'
            (r'\bself\b', 0, 'self'),

            # 'def' followed by an identifier
            (r'\bdef\b\s*(\w+)', 1, 'defclass'),
            # 'class' followed by an identifier
            (r'\bclass\b\s*(\w+)', 1, 'defclass'),

            # Numeric literals
            (r'\b[+-]?[0-9]+[lL]?\b', 0, 'numbers'),
            (r'\b[+-]?0[xX][0-9A-Fa-f]+[lL]?\b', 0, 'numbers'),
            (r'\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b', 0, 'numbers'),

            # Double-quoted string, possibly containing escape sequences
            (r'"[^"\\]*(\\.[^"\\]*)*"', 0, 'string'),
            # Single-quoted string, possibly containing escape sequences
            (r"'[^'\\]*(\\.[^'\\]*)*'", 0, 'string'),

            # From '#' until a newline
            (r'#[^\n]*', 0, 'comment'),
        ]
        self.rules = rules
        self.searchText = None

    @property
    def styles(self):
        # app = QtWidgets.QApplication.instance()
        # return DARK_STYLES if app.property('darkMode') else LIGHT_STYLES
        if darkdetect.isDark():
            return DARK_STYLES
        else:
            return LIGHT_STYLES

    def highlightBlock(self, text):
        """Apply syntax highlighting to the given block of text.
        """
        # Do other syntax formatting
        rules = self.rules.copy()
        for expression, nth, format in rules:
            format = self.styles[format]

            for n, match in enumerate(re.finditer(expression, text)):
                if n < nth:
                    continue
                start = match.start()
                length = match.end() - start
                self.setFormat(start, length, format)

        self.applySearchHighlight(text)
        self.setCurrentBlockState(0)

        # Do multi-line strings
        in_multiline = self.match_multiline(text, *self.tri_single)
        if not in_multiline:
            in_multiline = self.match_multiline(text, *self.tri_double)

    def match_multiline(self, text, delimiter, in_state, style):
        """Do highlighting of multi-line strings.

        =========== ==========================================================
        delimiter   (QRegularExpression) for triple-single-quotes or
                    triple-double-quotes
        in_state    (int) to represent the corresponding state changes when
                    inside those strings. Returns True if we're still inside a
                    multi-line string when this function is finished.
        style       (str) representation of the kind of style to use
        =========== ==========================================================
        """
        # If inside triple-single quotes, start at 0
        if self.previousBlockState() == in_state:
            start = 0
            add = 0
        # Otherwise, look for the delimiter on this line
        else:
            match = delimiter.match(text)
            start = match.capturedStart()
            # Move past this match
            add = match.capturedLength()

        # As long as there's a delimiter match on this line...
        while start >= 0:
            # Look for the ending delimiter
            match = delimiter.match(text, start + add)
            end = match.capturedEnd()
            # Ending delimiter on this line?
            if end >= add:
                length = end - start + add + match.capturedLength()
                self.setCurrentBlockState(0)
            # No; multi-line string
            else:
                self.setCurrentBlockState(in_state)
                length = len(text) - start + add
            # Apply formatting
            self.setFormat(start, length, self.styles[style])
            # Highlighting sits on top of this formatting
            # Look for the next match
            match = delimiter.match(text, start + length)
            start = match.capturedStart()

        self.applySearchHighlight(text)

        # Return True if still inside a multi-line string, False otherwise
        if self.currentBlockState() == in_state:
            return True
        else:
            return False

    def applySearchHighlight(self, text):
        if not self.searchText:
            return
        expr = f'(?i){self.searchText}'
        palette: QtGui.QPalette = app.palette()
        color = palette.highlight().color()
        fgndColor = palette.color(palette.ColorGroup.Current,
                                  palette.ColorRole.Text).name()
        style = charFormat(fgndColor, background=color.name())
        for match in re.finditer(expr, text):
            start = match.start()
            length = match.end() - start
            self.setFormat(start, length, style)





app = None
mainwindow = None
data = None
status_bar_message = ''
latest_item = None
latest_items = None

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

        self.hl = PythonHighlighter(self.ui.script_preview_plainTextEdit.document())
        # self.hl.setDocument(self.ui.codeView.document())

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
        global latest_item, latest_items

        if self.ui.preview_tabWidget.currentIndex() != 2:
            self.ui.preview_tabWidget.setCurrentIndex(0)

        self.ui.triage_numeric_listWidget.clearSelection()
        self.ui.triage_ignore_listWidget.clearSelection()

        if self.ui.triage_string_listWidget.selectedItems():
            latest_items = [i.text() for i in self.ui.triage_string_listWidget.selectedItems()]
            latest_item = self.ui.triage_string_listWidget.selectedItems()[-1].text()
            self.ui.text_preview_listWidget.clear()
            self.ui.text_preview_listWidget.addItems(data[latest_item].unique())

    def update_numeric_preview(self):
        global latest_item, latest_items

        self.ui.triage_string_listWidget.clearSelection()
        self.ui.triage_ignore_listWidget.clearSelection()

        if self.ui.triage_numeric_listWidget.selectedItems():
            latest_items = [i.text() for i in self.ui.triage_numeric_listWidget.selectedItems()]
            latest_item = self.ui.triage_numeric_listWidget.selectedItems()[-1].text()
            self.ui.text_preview_listWidget.clear()
            self.ui.text_preview_listWidget.addItems([str(d) for d in data[latest_item].unique()])

            if not self.ui.graphic_preview_plot_widget.plotItem.curves:
                # self.ui.graphic_preview_plot_widget.plot(data[latest_item].values, pen=None,
                #                                      symbolBrush=(231, 232, 255), symbolPen=(231, 232, 255), symbol='o',
                #                                      symbolSize=1.5, clear=True)
                # self.ui.graphic_preview_plot_widget.plot(data[latest_item].values, pen=None,
                #                                      symbolBrush=None, symbolPen=(231, 232, 255), symbol='+',
                #                                      symbolSize=2, clear=True)
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

    def script_run(self):
        self.ui.script_preview_consoleWidget.repl.runCmd('run()')
        # update consoleWidget namespace in case new vars created:
        self.ui.script_preview_consoleWidget.locals().update(globals())

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


if __name__ == "__main__":
    import multitimer

    timer = multitimer.MultiTimer(interval=1, function=status_bar)

    app = QApplication(sys.argv)
    mainwindow = ColliderScopeUI()
    mainwindow.show()
    sys.exit(app.exec())
