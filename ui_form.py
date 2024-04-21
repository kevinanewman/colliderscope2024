# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QFrame, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QSplitter,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget
from pyqtgraph.console import ConsoleWidget

class Ui_ColliderScopeUI(object):
    def setupUi(self, ColliderScopeUI):
        if not ColliderScopeUI.objectName():
            ColliderScopeUI.setObjectName(u"ColliderScopeUI")
        ColliderScopeUI.resize(1083, 723)
        ColliderScopeUI.setTabShape(QTabWidget.Rounded)
        self.actionsubmenu = QAction(ColliderScopeUI)
        self.actionsubmenu.setObjectName(u"actionsubmenu")
        self.centralwidget = QWidget(ColliderScopeUI)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.tabWidget_main = QTabWidget(self.centralwidget)
        self.tabWidget_main.setObjectName(u"tabWidget_main")
        self.tabWidget_main.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget_main.sizePolicy().hasHeightForWidth())
        self.tabWidget_main.setSizePolicy(sizePolicy1)
        self.tabWidget_main.setTabPosition(QTabWidget.North)
        self.tabWidget_main.setTabShape(QTabWidget.Triangular)
        self.tabWidget_main.setDocumentMode(True)
        self.import_tab = QWidget()
        self.import_tab.setObjectName(u"import_tab")
        self.horizontalLayout_12 = QHBoxLayout(self.import_tab)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.import_tab_verticalLayout = QVBoxLayout()
        self.import_tab_verticalLayout.setObjectName(u"import_tab_verticalLayout")
        self.file_import_browse_horizontalLayout = QHBoxLayout()
        self.file_import_browse_horizontalLayout.setObjectName(u"file_import_browse_horizontalLayout")
        self.filepathname_label = QLabel(self.import_tab)
        self.filepathname_label.setObjectName(u"filepathname_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.filepathname_label.sizePolicy().hasHeightForWidth())
        self.filepathname_label.setSizePolicy(sizePolicy2)

        self.file_import_browse_horizontalLayout.addWidget(self.filepathname_label)

        self.filepathname_lineEdit = QLineEdit(self.import_tab)
        self.filepathname_lineEdit.setObjectName(u"filepathname_lineEdit")
        self.filepathname_lineEdit.setEnabled(True)
        self.filepathname_lineEdit.setClearButtonEnabled(True)

        self.file_import_browse_horizontalLayout.addWidget(self.filepathname_lineEdit)

        self.file_import_browse_pushButton = QPushButton(self.import_tab)
        self.file_import_browse_pushButton.setObjectName(u"file_import_browse_pushButton")

        self.file_import_browse_horizontalLayout.addWidget(self.file_import_browse_pushButton)


        self.import_tab_verticalLayout.addLayout(self.file_import_browse_horizontalLayout)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.file_preview_horizontalLayout = QHBoxLayout()
        self.file_preview_horizontalLayout.setObjectName(u"file_preview_horizontalLayout")
        self.file_preview_label = QLabel(self.import_tab)
        self.file_preview_label.setObjectName(u"file_preview_label")
        self.file_preview_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.file_preview_horizontalLayout.addWidget(self.file_preview_label)

        self.file_preview_tableWidget = QTableWidget(self.import_tab)
        if (self.file_preview_tableWidget.columnCount() < 1):
            self.file_preview_tableWidget.setColumnCount(1)
        self.file_preview_tableWidget.setObjectName(u"file_preview_tableWidget")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Ignored)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.file_preview_tableWidget.sizePolicy().hasHeightForWidth())
        self.file_preview_tableWidget.setSizePolicy(sizePolicy3)
        self.file_preview_tableWidget.setMinimumSize(QSize(0, 0))
        self.file_preview_tableWidget.setMaximumSize(QSize(16777215, 16777208))
        self.file_preview_tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.file_preview_tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.file_preview_tableWidget.setAutoScroll(False)
        self.file_preview_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.file_preview_tableWidget.setTabKeyNavigation(False)
        self.file_preview_tableWidget.setProperty("showDropIndicator", False)
        self.file_preview_tableWidget.setDragDropOverwriteMode(False)
        self.file_preview_tableWidget.setAlternatingRowColors(True)
        self.file_preview_tableWidget.setTextElideMode(Qt.ElideNone)
        self.file_preview_tableWidget.setShowGrid(False)
        self.file_preview_tableWidget.setWordWrap(True)
        self.file_preview_tableWidget.setCornerButtonEnabled(False)
        self.file_preview_tableWidget.setRowCount(0)
        self.file_preview_tableWidget.setColumnCount(1)
        self.file_preview_tableWidget.horizontalHeader().setVisible(False)
        self.file_preview_tableWidget.horizontalHeader().setDefaultSectionSize(10000)
        self.file_preview_tableWidget.horizontalHeader().setHighlightSections(False)
        self.file_preview_tableWidget.horizontalHeader().setStretchLastSection(False)

        self.file_preview_horizontalLayout.addWidget(self.file_preview_tableWidget)

        self.file_import_tabWidget = QTabWidget(self.import_tab)
        self.file_import_tabWidget.setObjectName(u"file_import_tabWidget")
        self.file_import_tabWidget.setEnabled(False)
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.file_import_tabWidget.sizePolicy().hasHeightForWidth())
        self.file_import_tabWidget.setSizePolicy(sizePolicy4)
        self.file_import_tabWidget.setMinimumSize(QSize(250, 0))
        self.file_import_tabWidget.setDocumentMode(True)
        self.import_csv_tab = QWidget()
        self.import_csv_tab.setObjectName(u"import_csv_tab")
        self.verticalLayout = QVBoxLayout(self.import_csv_tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 0)
        self.import_csv_delimiter_horizontalLayout = QHBoxLayout()
        self.import_csv_delimiter_horizontalLayout.setObjectName(u"import_csv_delimiter_horizontalLayout")
        self.import_csv_delimiter_label = QLabel(self.import_csv_tab)
        self.import_csv_delimiter_label.setObjectName(u"import_csv_delimiter_label")
        self.import_csv_delimiter_label.setMinimumSize(QSize(70, 0))

        self.import_csv_delimiter_horizontalLayout.addWidget(self.import_csv_delimiter_label)

        self.import_csv_delimiter_comboBox = QComboBox(self.import_csv_tab)
        self.import_csv_delimiter_comboBox.addItem("")
        self.import_csv_delimiter_comboBox.addItem("")
        self.import_csv_delimiter_comboBox.addItem("")
        self.import_csv_delimiter_comboBox.addItem("")
        self.import_csv_delimiter_comboBox.setObjectName(u"import_csv_delimiter_comboBox")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.import_csv_delimiter_comboBox.sizePolicy().hasHeightForWidth())
        self.import_csv_delimiter_comboBox.setSizePolicy(sizePolicy5)
        self.import_csv_delimiter_comboBox.setMaximumSize(QSize(16777215, 16777215))

        self.import_csv_delimiter_horizontalLayout.addWidget(self.import_csv_delimiter_comboBox)


        self.verticalLayout.addLayout(self.import_csv_delimiter_horizontalLayout)

        self.import_csv_encoding_horizontalLayout = QHBoxLayout()
        self.import_csv_encoding_horizontalLayout.setObjectName(u"import_csv_encoding_horizontalLayout")
        self.import_csv_encoding_label = QLabel(self.import_csv_tab)
        self.import_csv_encoding_label.setObjectName(u"import_csv_encoding_label")
        self.import_csv_encoding_label.setMinimumSize(QSize(70, 0))

        self.import_csv_encoding_horizontalLayout.addWidget(self.import_csv_encoding_label)

        self.import_csv_encoding_comboBox = QComboBox(self.import_csv_tab)
        self.import_csv_encoding_comboBox.addItem(u"utf_8")
        self.import_csv_encoding_comboBox.addItem(u"cp1253")
        self.import_csv_encoding_comboBox.setObjectName(u"import_csv_encoding_comboBox")
        sizePolicy5.setHeightForWidth(self.import_csv_encoding_comboBox.sizePolicy().hasHeightForWidth())
        self.import_csv_encoding_comboBox.setSizePolicy(sizePolicy5)
        self.import_csv_encoding_comboBox.setMaximumSize(QSize(16777215, 16777215))

        self.import_csv_encoding_horizontalLayout.addWidget(self.import_csv_encoding_comboBox)


        self.verticalLayout.addLayout(self.import_csv_encoding_horizontalLayout)

        self.import_csv_skip_rows_horizontalLayout = QHBoxLayout()
        self.import_csv_skip_rows_horizontalLayout.setObjectName(u"import_csv_skip_rows_horizontalLayout")
        self.import_csv_skip_rows_label = QLabel(self.import_csv_tab)
        self.import_csv_skip_rows_label.setObjectName(u"import_csv_skip_rows_label")
        self.import_csv_skip_rows_label.setMinimumSize(QSize(70, 0))

        self.import_csv_skip_rows_horizontalLayout.addWidget(self.import_csv_skip_rows_label)

        self.import_csv_skip_rows_lineEdit = QLineEdit(self.import_csv_tab)
        self.import_csv_skip_rows_lineEdit.setObjectName(u"import_csv_skip_rows_lineEdit")
        self.import_csv_skip_rows_lineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.import_csv_skip_rows_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.import_csv_skip_rows_horizontalLayout.addWidget(self.import_csv_skip_rows_lineEdit)


        self.verticalLayout.addLayout(self.import_csv_skip_rows_horizontalLayout)

        self.import_csv_skip_blank_lines_horizontalLayout = QHBoxLayout()
        self.import_csv_skip_blank_lines_horizontalLayout.setObjectName(u"import_csv_skip_blank_lines_horizontalLayout")
        self.import_csv_skip_blank_lines_label = QLabel(self.import_csv_tab)
        self.import_csv_skip_blank_lines_label.setObjectName(u"import_csv_skip_blank_lines_label")

        self.import_csv_skip_blank_lines_horizontalLayout.addWidget(self.import_csv_skip_blank_lines_label)

        self.import_csv_skip_blank_lines_comboBox = QComboBox(self.import_csv_tab)
        self.import_csv_skip_blank_lines_comboBox.addItem("")
        self.import_csv_skip_blank_lines_comboBox.addItem("")
        self.import_csv_skip_blank_lines_comboBox.setObjectName(u"import_csv_skip_blank_lines_comboBox")

        self.import_csv_skip_blank_lines_horizontalLayout.addWidget(self.import_csv_skip_blank_lines_comboBox)


        self.verticalLayout.addLayout(self.import_csv_skip_blank_lines_horizontalLayout)

        self.import_csv_freeform_label = QLabel(self.import_csv_tab)
        self.import_csv_freeform_label.setObjectName(u"import_csv_freeform_label")

        self.verticalLayout.addWidget(self.import_csv_freeform_label)

        self.import_csv_freeform_options_plainTextEdit = QPlainTextEdit(self.import_csv_tab)
        self.import_csv_freeform_options_plainTextEdit.setObjectName(u"import_csv_freeform_options_plainTextEdit")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.import_csv_freeform_options_plainTextEdit.sizePolicy().hasHeightForWidth())
        self.import_csv_freeform_options_plainTextEdit.setSizePolicy(sizePolicy6)

        self.verticalLayout.addWidget(self.import_csv_freeform_options_plainTextEdit)

        self.import_csv_pushButton = QPushButton(self.import_csv_tab)
        self.import_csv_pushButton.setObjectName(u"import_csv_pushButton")
        sizePolicy5.setHeightForWidth(self.import_csv_pushButton.sizePolicy().hasHeightForWidth())
        self.import_csv_pushButton.setSizePolicy(sizePolicy5)
        self.import_csv_pushButton.setAutoDefault(True)

        self.verticalLayout.addWidget(self.import_csv_pushButton)

        self.file_import_tabWidget.addTab(self.import_csv_tab, "")
        self.import_excel_tab = QWidget()
        self.import_excel_tab.setObjectName(u"import_excel_tab")
        self.verticalLayout_8 = QVBoxLayout(self.import_excel_tab)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.import_excel_skip_rows_horizontalLayout = QHBoxLayout()
        self.import_excel_skip_rows_horizontalLayout.setObjectName(u"import_excel_skip_rows_horizontalLayout")
        self.import_excel_skip_rows_label = QLabel(self.import_excel_tab)
        self.import_excel_skip_rows_label.setObjectName(u"import_excel_skip_rows_label")
        self.import_excel_skip_rows_label.setMinimumSize(QSize(70, 0))

        self.import_excel_skip_rows_horizontalLayout.addWidget(self.import_excel_skip_rows_label)

        self.import_excel_skip_rows_lineEdit = QLineEdit(self.import_excel_tab)
        self.import_excel_skip_rows_lineEdit.setObjectName(u"import_excel_skip_rows_lineEdit")
        self.import_excel_skip_rows_lineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.import_excel_skip_rows_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.import_excel_skip_rows_horizontalLayout.addWidget(self.import_excel_skip_rows_lineEdit)


        self.verticalLayout_8.addLayout(self.import_excel_skip_rows_horizontalLayout)

        self.import_excel_sheet_horizontalLayout = QHBoxLayout()
        self.import_excel_sheet_horizontalLayout.setObjectName(u"import_excel_sheet_horizontalLayout")
        self.import_excel_sheet_label = QLabel(self.import_excel_tab)
        self.import_excel_sheet_label.setObjectName(u"import_excel_sheet_label")
        self.import_excel_sheet_label.setMinimumSize(QSize(70, 0))

        self.import_excel_sheet_horizontalLayout.addWidget(self.import_excel_sheet_label)

        self.import_excel_sheet_lineEdit = QLineEdit(self.import_excel_tab)
        self.import_excel_sheet_lineEdit.setObjectName(u"import_excel_sheet_lineEdit")
        self.import_excel_sheet_lineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.import_excel_sheet_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.import_excel_sheet_horizontalLayout.addWidget(self.import_excel_sheet_lineEdit)


        self.verticalLayout_8.addLayout(self.import_excel_sheet_horizontalLayout)

        self.import_excel_header_horizontalLayout = QHBoxLayout()
        self.import_excel_header_horizontalLayout.setObjectName(u"import_excel_header_horizontalLayout")
        self.import_excel_header_label = QLabel(self.import_excel_tab)
        self.import_excel_header_label.setObjectName(u"import_excel_header_label")
        self.import_excel_header_label.setMinimumSize(QSize(70, 0))

        self.import_excel_header_horizontalLayout.addWidget(self.import_excel_header_label)

        self.import_excel_header_lineEdit = QLineEdit(self.import_excel_tab)
        self.import_excel_header_lineEdit.setObjectName(u"import_excel_header_lineEdit")
        self.import_excel_header_lineEdit.setMaximumSize(QSize(16777215, 16777215))
        self.import_excel_header_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.import_excel_header_horizontalLayout.addWidget(self.import_excel_header_lineEdit)


        self.verticalLayout_8.addLayout(self.import_excel_header_horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.import_excel_pushButton = QPushButton(self.import_excel_tab)
        self.import_excel_pushButton.setObjectName(u"import_excel_pushButton")
        sizePolicy5.setHeightForWidth(self.import_excel_pushButton.sizePolicy().hasHeightForWidth())
        self.import_excel_pushButton.setSizePolicy(sizePolicy5)
        self.import_excel_pushButton.setMinimumSize(QSize(252, 0))
        self.import_excel_pushButton.setAutoDefault(True)
        self.import_excel_pushButton.setFlat(False)

        self.verticalLayout_8.addWidget(self.import_excel_pushButton)

        self.file_import_tabWidget.addTab(self.import_excel_tab, "")

        self.file_preview_horizontalLayout.addWidget(self.file_import_tabWidget)


        self.horizontalLayout_7.addLayout(self.file_preview_horizontalLayout)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")

        self.horizontalLayout_7.addLayout(self.verticalLayout_6)


        self.import_tab_verticalLayout.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_12.addLayout(self.import_tab_verticalLayout)

        self.tabWidget_main.addTab(self.import_tab, "")
        self.triage_tab = QWidget()
        self.triage_tab.setObjectName(u"triage_tab")
        self.triage_tab.setEnabled(False)
        self.horizontalLayout_4 = QHBoxLayout(self.triage_tab)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.splitter_2 = QSplitter(self.triage_tab)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Vertical)
        self.splitter_2.setChildrenCollapsible(False)
        self.widget = QWidget(self.splitter_2)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.horizontalLayout_filter = QHBoxLayout()
        self.horizontalLayout_filter.setObjectName(u"horizontalLayout_filter")
        self.label_filter = QLabel(self.widget)
        self.label_filter.setObjectName(u"label_filter")

        self.horizontalLayout_filter.addWidget(self.label_filter)

        self.lineEdit_filter = QLineEdit(self.widget)
        self.lineEdit_filter.setObjectName(u"lineEdit_filter")

        self.horizontalLayout_filter.addWidget(self.lineEdit_filter)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_filter.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout_filter)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_numeric = QVBoxLayout()
#ifndef Q_OS_MAC
        self.verticalLayout_numeric.setSpacing(-1)
#endif
        self.verticalLayout_numeric.setObjectName(u"verticalLayout_numeric")
        self.verticalLayout_numeric.setContentsMargins(0, -1, -1, 0)
        self.label_numeric = QLabel(self.widget)
        self.label_numeric.setObjectName(u"label_numeric")
        self.label_numeric.setAlignment(Qt.AlignCenter)

        self.verticalLayout_numeric.addWidget(self.label_numeric)

        self.triage_numeric_listWidget = QListWidget(self.widget)
        self.triage_numeric_listWidget.setObjectName(u"triage_numeric_listWidget")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.triage_numeric_listWidget.sizePolicy().hasHeightForWidth())
        self.triage_numeric_listWidget.setSizePolicy(sizePolicy7)
        self.triage_numeric_listWidget.setMinimumSize(QSize(296, 202))
        self.triage_numeric_listWidget.setStyleSheet(u"background-color: rgb(196, 242, 196);\n"
"color: black\n"
"")
        self.triage_numeric_listWidget.setProperty("showDropIndicator", True)
        self.triage_numeric_listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.triage_numeric_listWidget.setSortingEnabled(True)

        self.verticalLayout_numeric.addWidget(self.triage_numeric_listWidget)

        self.copytostring_pushButton = QPushButton(self.widget)
        self.copytostring_pushButton.setObjectName(u"copytostring_pushButton")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.copytostring_pushButton.sizePolicy().hasHeightForWidth())
        self.copytostring_pushButton.setSizePolicy(sizePolicy8)
        self.copytostring_pushButton.setAutoDefault(False)
        self.copytostring_pushButton.setFlat(False)

        self.verticalLayout_numeric.addWidget(self.copytostring_pushButton)


        self.horizontalLayout_2.addLayout(self.verticalLayout_numeric)

        self.add2script_pushButton = QPushButton(self.widget)
        self.add2script_pushButton.setObjectName(u"add2script_pushButton")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.add2script_pushButton.sizePolicy().hasHeightForWidth())
        self.add2script_pushButton.setSizePolicy(sizePolicy9)
        self.add2script_pushButton.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(11)
        self.add2script_pushButton.setFont(font)
        self.add2script_pushButton.setLayoutDirection(Qt.LeftToRight)
        self.add2script_pushButton.setAutoFillBackground(False)

        self.horizontalLayout_2.addWidget(self.add2script_pushButton)

        self.verticalLayout_string = QVBoxLayout()
        self.verticalLayout_string.setObjectName(u"verticalLayout_string")
        self.label_string = QLabel(self.widget)
        self.label_string.setObjectName(u"label_string")
        self.label_string.setAlignment(Qt.AlignCenter)

        self.verticalLayout_string.addWidget(self.label_string)

        self.triage_string_listWidget = QListWidget(self.widget)
        self.triage_string_listWidget.setObjectName(u"triage_string_listWidget")
        self.triage_string_listWidget.setMinimumSize(QSize(296, 202))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(198, 244, 198, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(0, 0, 0, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.triage_string_listWidget.setPalette(palette)
        self.triage_string_listWidget.setStyleSheet(u"background-color: rgb(198, 244, 198);\n"
"color: black;\n"
"")
        self.triage_string_listWidget.setFrameShape(QFrame.StyledPanel)
        self.triage_string_listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.triage_string_listWidget.setSortingEnabled(True)

        self.verticalLayout_string.addWidget(self.triage_string_listWidget)

        self.convertonumeric_pushButton = QPushButton(self.widget)
        self.convertonumeric_pushButton.setObjectName(u"convertonumeric_pushButton")

        self.verticalLayout_string.addWidget(self.convertonumeric_pushButton)


        self.horizontalLayout_2.addLayout(self.verticalLayout_string)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.ignore_pushButton = QPushButton(self.widget)
        self.ignore_pushButton.setObjectName(u"ignore_pushButton")
        self.ignore_pushButton.setAutoFillBackground(False)
        self.ignore_pushButton.setFlat(False)

        self.verticalLayout_2.addWidget(self.ignore_pushButton)

        self.unignore_pushButton = QPushButton(self.widget)
        self.unignore_pushButton.setObjectName(u"unignore_pushButton")

        self.verticalLayout_2.addWidget(self.unignore_pushButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_ignore = QVBoxLayout()
        self.verticalLayout_ignore.setObjectName(u"verticalLayout_ignore")
        self.label_ignore = QLabel(self.widget)
        self.label_ignore.setObjectName(u"label_ignore")
        self.label_ignore.setEnabled(False)
        self.label_ignore.setAlignment(Qt.AlignCenter)

        self.verticalLayout_ignore.addWidget(self.label_ignore)

        self.triage_ignore_listWidget = QListWidget(self.widget)
        self.triage_ignore_listWidget.setObjectName(u"triage_ignore_listWidget")
        self.triage_ignore_listWidget.setStyleSheet(u"background-color: rgb(253, 223, 223);")

        self.verticalLayout_ignore.addWidget(self.triage_ignore_listWidget)


        self.horizontalLayout_2.addLayout(self.verticalLayout_ignore)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.splitter_2.addWidget(self.widget)
        self.preview_tabWidget = QTabWidget(self.splitter_2)
        self.preview_tabWidget.setObjectName(u"preview_tabWidget")
        self.preview_tabWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.preview_tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.preview_tabWidget.setDocumentMode(True)
        self.preview_tabWidget.setTabsClosable(False)
        self.text_preview_tab = QWidget()
        self.text_preview_tab.setObjectName(u"text_preview_tab")
        self.horizontalLayout = QHBoxLayout(self.text_preview_tab)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.text_preview_listWidget = QListWidget(self.text_preview_tab)
        self.text_preview_listWidget.setObjectName(u"text_preview_listWidget")

        self.horizontalLayout.addWidget(self.text_preview_listWidget)

        self.preview_tabWidget.addTab(self.text_preview_tab, "")
        self.graphic_preview_tab = QWidget()
        self.graphic_preview_tab.setObjectName(u"graphic_preview_tab")
        self.verticalLayout_4 = QVBoxLayout(self.graphic_preview_tab)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.graphic_preview_plot_widget = PlotWidget(self.graphic_preview_tab)
        self.graphic_preview_plot_widget.setObjectName(u"graphic_preview_plot_widget")
        brush3 = QBrush(QColor(7, 27, 46, 255))
        brush3.setStyle(Qt.SolidPattern)
        self.graphic_preview_plot_widget.setBackgroundBrush(brush3)
        self.graphic_preview_plot_widget.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.graphic_preview_plot_widget)

        self.preview_tabWidget.addTab(self.graphic_preview_tab, "")
        self.script_preview_tab = QWidget()
        self.script_preview_tab.setObjectName(u"script_preview_tab")
        self.horizontalLayout_6 = QHBoxLayout(self.script_preview_tab)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.splitter = QSplitter(self.script_preview_tab)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setChildrenCollapsible(False)
        self.script_preview_plainTextEdit = QPlainTextEdit(self.splitter)
        self.script_preview_plainTextEdit.setObjectName(u"script_preview_plainTextEdit")
        self.splitter.addWidget(self.script_preview_plainTextEdit)
        self.script_preview_consoleWidget = ConsoleWidget(self.splitter)
        self.script_preview_consoleWidget.setObjectName(u"script_preview_consoleWidget")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.script_preview_consoleWidget.sizePolicy().hasHeightForWidth())
        self.script_preview_consoleWidget.setSizePolicy(sizePolicy10)
        self.splitter.addWidget(self.script_preview_consoleWidget)

        self.horizontalLayout_6.addWidget(self.splitter)

        self.preview_tabWidget.addTab(self.script_preview_tab, "")
        self.splitter_2.addWidget(self.preview_tabWidget)

        self.horizontalLayout_4.addWidget(self.splitter_2)

        self.tabWidget_main.addTab(self.triage_tab, "")
        self.plot_tab = QWidget()
        self.plot_tab.setObjectName(u"plot_tab")
        self.plot_tab.setEnabled(False)
        self.horizontalLayout_5 = QHBoxLayout(self.plot_tab)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.plot_graphicsView = PlotWidget(self.plot_tab)
        self.plot_graphicsView.setObjectName(u"plot_graphicsView")
        self.plot_graphicsView.setBackgroundBrush(brush3)

        self.horizontalLayout_5.addWidget(self.plot_graphicsView)

        self.tabWidget_main.addTab(self.plot_tab, "")
        self.export_tab = QWidget()
        self.export_tab.setObjectName(u"export_tab")
        self.export_tab.setEnabled(False)
        self.tabWidget_main.addTab(self.export_tab, "")

        self.horizontalLayout_3.addWidget(self.tabWidget_main)

        ColliderScopeUI.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ColliderScopeUI)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1083, 24))
        self.menuColliderScope2024 = QMenu(self.menubar)
        self.menuColliderScope2024.setObjectName(u"menuColliderScope2024")
        ColliderScopeUI.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ColliderScopeUI)
        self.statusbar.setObjectName(u"statusbar")
        ColliderScopeUI.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuColliderScope2024.menuAction())
        self.menuColliderScope2024.addAction(self.actionsubmenu)

        self.retranslateUi(ColliderScopeUI)
        self.import_excel_pushButton.clicked.connect(ColliderScopeUI.import_excel_file)
        self.filepathname_lineEdit.returnPressed.connect(ColliderScopeUI.filepathname_changed)
        self.import_csv_pushButton.clicked.connect(ColliderScopeUI.import_csv_file)
        self.file_import_browse_pushButton.clicked.connect(ColliderScopeUI.import_filebrowse)
        self.import_excel_skip_rows_lineEdit.editingFinished.connect(ColliderScopeUI.load_file_preview)
        self.import_excel_sheet_lineEdit.editingFinished.connect(ColliderScopeUI.load_file_preview)
        self.import_excel_header_lineEdit.editingFinished.connect(ColliderScopeUI.load_file_preview)
        self.import_csv_delimiter_comboBox.currentTextChanged.connect(ColliderScopeUI.load_file_preview)
        self.import_csv_encoding_comboBox.currentTextChanged.connect(ColliderScopeUI.load_file_preview)
        self.import_csv_skip_rows_lineEdit.editingFinished.connect(ColliderScopeUI.load_file_preview)
        self.import_csv_skip_blank_lines_comboBox.currentTextChanged.connect(ColliderScopeUI.load_file_preview)
        self.import_csv_freeform_options_plainTextEdit.textChanged.connect(ColliderScopeUI.load_file_preview)
        self.triage_string_listWidget.itemSelectionChanged.connect(ColliderScopeUI.update_string_preview)
        self.triage_numeric_listWidget.itemSelectionChanged.connect(ColliderScopeUI.update_numeric_preview)

        self.tabWidget_main.setCurrentIndex(0)
        self.file_import_tabWidget.setCurrentIndex(1)
        self.import_excel_pushButton.setDefault(False)
        self.preview_tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ColliderScopeUI)
    # setupUi

    def retranslateUi(self, ColliderScopeUI):
        ColliderScopeUI.setWindowTitle(QCoreApplication.translate("ColliderScopeUI", u"ColliderScopeUI", None))
        self.actionsubmenu.setText(QCoreApplication.translate("ColliderScopeUI", u"submenu", None))
        self.filepathname_label.setText(QCoreApplication.translate("ColliderScopeUI", u"Filename", None))
        self.filepathname_lineEdit.setPlaceholderText(QCoreApplication.translate("ColliderScopeUI", u"path/to/input_file", None))
        self.file_import_browse_pushButton.setText(QCoreApplication.translate("ColliderScopeUI", u"Browse ...", None))
        self.file_preview_label.setText(QCoreApplication.translate("ColliderScopeUI", u"File\n"
"Preview", None))
        self.import_csv_delimiter_label.setText(QCoreApplication.translate("ColliderScopeUI", u"delimiter", None))
        self.import_csv_delimiter_comboBox.setItemText(0, QCoreApplication.translate("ColliderScopeUI", u"Auto", None))
        self.import_csv_delimiter_comboBox.setItemText(1, QCoreApplication.translate("ColliderScopeUI", u",", None))
        self.import_csv_delimiter_comboBox.setItemText(2, QCoreApplication.translate("ColliderScopeUI", u";", None))
        self.import_csv_delimiter_comboBox.setItemText(3, QCoreApplication.translate("ColliderScopeUI", u"\\t", None))

        self.import_csv_encoding_label.setText(QCoreApplication.translate("ColliderScopeUI", u"encoding", None))

        self.import_csv_skip_rows_label.setText(QCoreApplication.translate("ColliderScopeUI", u"skiprows", None))
        self.import_csv_skip_rows_lineEdit.setText(QCoreApplication.translate("ColliderScopeUI", u"0", None))
        self.import_csv_skip_blank_lines_label.setText(QCoreApplication.translate("ColliderScopeUI", u"skip_blank_lines", None))
        self.import_csv_skip_blank_lines_comboBox.setItemText(0, QCoreApplication.translate("ColliderScopeUI", u"True", None))
        self.import_csv_skip_blank_lines_comboBox.setItemText(1, QCoreApplication.translate("ColliderScopeUI", u"False", None))

        self.import_csv_freeform_label.setText(QCoreApplication.translate("ColliderScopeUI", u"read_csv freeform options:", None))
        self.import_csv_freeform_options_plainTextEdit.setPlaceholderText(QCoreApplication.translate("ColliderScopeUI", u"e.g. nrows=100, engine=python, etc...", None))
        self.import_csv_pushButton.setText(QCoreApplication.translate("ColliderScopeUI", u"Import", None))
        self.file_import_tabWidget.setTabText(self.file_import_tabWidget.indexOf(self.import_csv_tab), QCoreApplication.translate("ColliderScopeUI", u"CSV", None))
        self.import_excel_skip_rows_label.setText(QCoreApplication.translate("ColliderScopeUI", u"skiprows", None))
        self.import_excel_skip_rows_lineEdit.setText(QCoreApplication.translate("ColliderScopeUI", u"0", None))
        self.import_excel_sheet_label.setText(QCoreApplication.translate("ColliderScopeUI", u"sheet", None))
        self.import_excel_sheet_lineEdit.setText(QCoreApplication.translate("ColliderScopeUI", u"0", None))
        self.import_excel_header_label.setText(QCoreApplication.translate("ColliderScopeUI", u"header", None))
        self.import_excel_header_lineEdit.setText(QCoreApplication.translate("ColliderScopeUI", u"0", None))
        self.import_excel_pushButton.setText(QCoreApplication.translate("ColliderScopeUI", u"Import", None))
        self.file_import_tabWidget.setTabText(self.file_import_tabWidget.indexOf(self.import_excel_tab), QCoreApplication.translate("ColliderScopeUI", u"Excel", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.import_tab), QCoreApplication.translate("ColliderScopeUI", u"Import", None))
        self.label.setText(QCoreApplication.translate("ColliderScopeUI", u"Data Preview and Triage", None))
        self.label_filter.setText(QCoreApplication.translate("ColliderScopeUI", u"Filter", None))
        self.label_numeric.setText(QCoreApplication.translate("ColliderScopeUI", u"Numeric (Plot Sources)", None))
        self.copytostring_pushButton.setText(QCoreApplication.translate("ColliderScopeUI", u"Copy to String (update Script)", None))
        self.add2script_pushButton.setText(QCoreApplication.translate("ColliderScopeUI", u"A\n"
"d\n"
"d\n"
"\n"
"to\n"
"\n"
"s\n"
"c\n"
"r\n"
"i\n"
"p\n"
"t\n"
"\n"
"v\n"
"v\n"
"", None))
        self.label_string.setText(QCoreApplication.translate("ColliderScopeUI", u"String (Filter Sources)", None))
        self.convertonumeric_pushButton.setText(QCoreApplication.translate("ColliderScopeUI", u"Convert to Numeric (update Script)", None))
        self.ignore_pushButton.setText(QCoreApplication.translate("ColliderScopeUI", u">>>", None))
        self.unignore_pushButton.setText(QCoreApplication.translate("ColliderScopeUI", u"<<<", None))
        self.label_ignore.setText(QCoreApplication.translate("ColliderScopeUI", u"Ignore", None))
        self.preview_tabWidget.setTabText(self.preview_tabWidget.indexOf(self.text_preview_tab), QCoreApplication.translate("ColliderScopeUI", u"Text Preview", None))
        self.preview_tabWidget.setTabText(self.preview_tabWidget.indexOf(self.graphic_preview_tab), QCoreApplication.translate("ColliderScopeUI", u"Graphic Preview", None))
        self.script_preview_plainTextEdit.setPlainText(QCoreApplication.translate("ColliderScopeUI", u"print('hello colliderscope!')", None))
        self.preview_tabWidget.setTabText(self.preview_tabWidget.indexOf(self.script_preview_tab), QCoreApplication.translate("ColliderScopeUI", u"Preprocess Script", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.triage_tab), QCoreApplication.translate("ColliderScopeUI", u"Data Triage", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.plot_tab), QCoreApplication.translate("ColliderScopeUI", u"Plotting", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.export_tab), QCoreApplication.translate("ColliderScopeUI", u"Export", None))
        self.menuColliderScope2024.setTitle(QCoreApplication.translate("ColliderScopeUI", u"Menu", None))
    # retranslateUi

