# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'colliderscope.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QCheckBox,
    QComboBox, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QSplitter, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QToolButton, QVBoxLayout,
    QWidget)

from filterwidget import FilterWidget
from pyqtgraph import PlotWidget
from pyqtgraph.console import ConsoleWidget

class Ui_ColliderScopeUI(object):
    def setupUi(self, ColliderScopeUI):
        if not ColliderScopeUI.objectName():
            ColliderScopeUI.setObjectName(u"ColliderScopeUI")
        ColliderScopeUI.resize(1025, 768)
        ColliderScopeUI.setDocumentMode(True)
        ColliderScopeUI.setTabShape(QTabWidget.Triangular)
        ColliderScopeUI.setUnifiedTitleAndToolBarOnMac(False)
        self.actionsubmenu = QAction(ColliderScopeUI)
        self.actionsubmenu.setObjectName(u"actionsubmenu")
        self.centralwidget = QWidget(ColliderScopeUI)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout_11 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.tabWidget_main = QTabWidget(self.centralwidget)
        self.tabWidget_main.setObjectName(u"tabWidget_main")
        self.tabWidget_main.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget_main.sizePolicy().hasHeightForWidth())
        self.tabWidget_main.setSizePolicy(sizePolicy1)
        self.tabWidget_main.setTabPosition(QTabWidget.North)
        self.tabWidget_main.setTabShape(QTabWidget.Rounded)
        self.tabWidget_main.setDocumentMode(True)
        self.import_tab = QWidget()
        self.import_tab.setObjectName(u"import_tab")
        self.verticalLayout_6 = QVBoxLayout(self.import_tab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
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
        self.file_import_browse_pushButton.setAutoDefault(True)

        self.file_import_browse_horizontalLayout.addWidget(self.file_import_browse_pushButton)


        self.verticalLayout_6.addLayout(self.file_import_browse_horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.file_preview_label = QLabel(self.import_tab)
        self.file_preview_label.setObjectName(u"file_preview_label")
        self.file_preview_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_13.addWidget(self.file_preview_label)

        self.preview_size_checkBox = QCheckBox(self.import_tab)
        self.preview_size_checkBox.setObjectName(u"preview_size_checkBox")
        self.preview_size_checkBox.setChecked(True)

        self.verticalLayout_13.addWidget(self.preview_size_checkBox)

        self.preview_size_spinBox = QSpinBox(self.import_tab)
        self.preview_size_spinBox.setObjectName(u"preview_size_spinBox")
        self.preview_size_spinBox.setWrapping(False)
        self.preview_size_spinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.preview_size_spinBox.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.preview_size_spinBox.setAccelerated(True)
        self.preview_size_spinBox.setMinimum(100)
        self.preview_size_spinBox.setMaximum(1000000)
        self.preview_size_spinBox.setSingleStep(100)
        self.preview_size_spinBox.setValue(100)

        self.verticalLayout_13.addWidget(self.preview_size_spinBox)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_4)


        self.horizontalLayout_3.addLayout(self.verticalLayout_13)

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
        self.file_preview_tableWidget.setAutoScroll(False)
        self.file_preview_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.file_preview_tableWidget.setTabKeyNavigation(False)
        self.file_preview_tableWidget.setProperty("showDropIndicator", False)
        self.file_preview_tableWidget.setDragDropOverwriteMode(False)
        self.file_preview_tableWidget.setAlternatingRowColors(False)
        self.file_preview_tableWidget.setShowGrid(False)
        self.file_preview_tableWidget.setWordWrap(True)
        self.file_preview_tableWidget.setCornerButtonEnabled(False)
        self.file_preview_tableWidget.setRowCount(0)
        self.file_preview_tableWidget.setColumnCount(1)
        self.file_preview_tableWidget.horizontalHeader().setVisible(False)
        self.file_preview_tableWidget.horizontalHeader().setHighlightSections(False)
        self.file_preview_tableWidget.horizontalHeader().setStretchLastSection(False)

        self.horizontalLayout_3.addWidget(self.file_preview_tableWidget)

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
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
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

        self.import_csv_two_row_header_horizontalLayout = QHBoxLayout()
        self.import_csv_two_row_header_horizontalLayout.setObjectName(u"import_csv_two_row_header_horizontalLayout")
        self.import_csv_two_row_header_lines_label = QLabel(self.import_csv_tab)
        self.import_csv_two_row_header_lines_label.setObjectName(u"import_csv_two_row_header_lines_label")

        self.import_csv_two_row_header_horizontalLayout.addWidget(self.import_csv_two_row_header_lines_label)

        self.import_csv_two_row_header_comboBox = QComboBox(self.import_csv_tab)
        self.import_csv_two_row_header_comboBox.addItem("")
        self.import_csv_two_row_header_comboBox.addItem("")
        self.import_csv_two_row_header_comboBox.setObjectName(u"import_csv_two_row_header_comboBox")

        self.import_csv_two_row_header_horizontalLayout.addWidget(self.import_csv_two_row_header_comboBox)


        self.verticalLayout.addLayout(self.import_csv_two_row_header_horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.import_csv_help_toolButton = QToolButton(self.import_csv_tab)
        self.import_csv_help_toolButton.setObjectName(u"import_csv_help_toolButton")
        icon = QIcon()
        icon.addFile(u"assets/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.import_csv_help_toolButton.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.import_csv_help_toolButton)

        self.import_csv_freeform_label = QLabel(self.import_csv_tab)
        self.import_csv_freeform_label.setObjectName(u"import_csv_freeform_label")

        self.horizontalLayout_4.addWidget(self.import_csv_freeform_label)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

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

        self.import_excel_sheet_comboBox = QComboBox(self.import_excel_tab)
        self.import_excel_sheet_comboBox.setObjectName(u"import_excel_sheet_comboBox")

        self.import_excel_sheet_horizontalLayout.addWidget(self.import_excel_sheet_comboBox)


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

        self.import_excel_two_row_header_horizontalLayout = QHBoxLayout()
        self.import_excel_two_row_header_horizontalLayout.setObjectName(u"import_excel_two_row_header_horizontalLayout")
        self.import_excel_two_row_header_lines_label = QLabel(self.import_excel_tab)
        self.import_excel_two_row_header_lines_label.setObjectName(u"import_excel_two_row_header_lines_label")

        self.import_excel_two_row_header_horizontalLayout.addWidget(self.import_excel_two_row_header_lines_label)

        self.import_excel_two_row_header_comboBox = QComboBox(self.import_excel_tab)
        self.import_excel_two_row_header_comboBox.addItem("")
        self.import_excel_two_row_header_comboBox.addItem("")
        self.import_excel_two_row_header_comboBox.setObjectName(u"import_excel_two_row_header_comboBox")

        self.import_excel_two_row_header_horizontalLayout.addWidget(self.import_excel_two_row_header_comboBox)


        self.verticalLayout_8.addLayout(self.import_excel_two_row_header_horizontalLayout)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.import_excel_help_toolButton = QToolButton(self.import_excel_tab)
        self.import_excel_help_toolButton.setObjectName(u"import_excel_help_toolButton")
        self.import_excel_help_toolButton.setIcon(icon)

        self.horizontalLayout_7.addWidget(self.import_excel_help_toolButton)

        self.label_2 = QLabel(self.import_excel_tab)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_7.addWidget(self.label_2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_7)

        self.plainTextEdit = QPlainTextEdit(self.import_excel_tab)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout_8.addWidget(self.plainTextEdit)

        self.import_excel_pushButton = QPushButton(self.import_excel_tab)
        self.import_excel_pushButton.setObjectName(u"import_excel_pushButton")
        sizePolicy5.setHeightForWidth(self.import_excel_pushButton.sizePolicy().hasHeightForWidth())
        self.import_excel_pushButton.setSizePolicy(sizePolicy5)
        self.import_excel_pushButton.setMinimumSize(QSize(252, 0))
        self.import_excel_pushButton.setAutoDefault(True)
        self.import_excel_pushButton.setFlat(False)

        self.verticalLayout_8.addWidget(self.import_excel_pushButton)

        self.file_import_tabWidget.addTab(self.import_excel_tab, "")

        self.horizontalLayout_3.addWidget(self.file_import_tabWidget)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)

        self.tabWidget_main.addTab(self.import_tab, "")
        self.triage_tab = QWidget()
        self.triage_tab.setObjectName(u"triage_tab")
        self.triage_tab.setEnabled(False)
        self.verticalLayout_12 = QVBoxLayout(self.triage_tab)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(5, 5, 5, 5)
        self.splitter_2 = QSplitter(self.triage_tab)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Vertical)
        self.layoutWidget = QWidget(self.splitter_2)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_10 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_10.addWidget(self.label)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_filter = QHBoxLayout()
        self.horizontalLayout_filter.setObjectName(u"horizontalLayout_filter")
        self.triage_filter_widget = FilterWidget(self.layoutWidget)
        self.triage_filter_widget.setObjectName(u"triage_filter_widget")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.triage_filter_widget.sizePolicy().hasHeightForWidth())
        self.triage_filter_widget.setSizePolicy(sizePolicy7)
        self.triage_filter_widget.setMinimumSize(QSize(300, 0))
        self.triage_filter_widget.setMaximumSize(QSize(300, 25))

        self.horizontalLayout_filter.addWidget(self.triage_filter_widget)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_filter.addItem(self.horizontalSpacer)


        self.verticalLayout_9.addLayout(self.horizontalLayout_filter)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_numeric = QVBoxLayout()
#ifndef Q_OS_MAC
        self.verticalLayout_numeric.setSpacing(-1)
#endif
        self.verticalLayout_numeric.setObjectName(u"verticalLayout_numeric")
        self.verticalLayout_numeric.setContentsMargins(0, -1, -1, 0)
        self.label_numeric = QLabel(self.layoutWidget)
        self.label_numeric.setObjectName(u"label_numeric")
        self.label_numeric.setAlignment(Qt.AlignCenter)

        self.verticalLayout_numeric.addWidget(self.label_numeric)

        self.triage_numeric_listWidget = QListWidget(self.layoutWidget)
        self.triage_numeric_listWidget.setObjectName(u"triage_numeric_listWidget")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.triage_numeric_listWidget.sizePolicy().hasHeightForWidth())
        self.triage_numeric_listWidget.setSizePolicy(sizePolicy8)
        self.triage_numeric_listWidget.setMinimumSize(QSize(296, 202))
        self.triage_numeric_listWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.triage_numeric_listWidget.setStyleSheet(u"background-color: rgb(196, 242, 196);\n"
"color: black\n"
"")
        self.triage_numeric_listWidget.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.triage_numeric_listWidget.setProperty("showDropIndicator", True)
        self.triage_numeric_listWidget.setDragEnabled(False)
        self.triage_numeric_listWidget.setDragDropMode(QAbstractItemView.DragOnly)
        self.triage_numeric_listWidget.setAlternatingRowColors(False)
        self.triage_numeric_listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.triage_numeric_listWidget.setSortingEnabled(True)

        self.verticalLayout_numeric.addWidget(self.triage_numeric_listWidget)


        self.horizontalLayout_2.addLayout(self.verticalLayout_numeric)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)

        self.add_to_script_toolButton = QToolButton(self.layoutWidget)
        self.add_to_script_toolButton.setObjectName(u"add_to_script_toolButton")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.add_to_script_toolButton.sizePolicy().hasHeightForWidth())
        self.add_to_script_toolButton.setSizePolicy(sizePolicy9)
        self.add_to_script_toolButton.setMinimumSize(QSize(40, 0))
        self.add_to_script_toolButton.setMaximumSize(QSize(40, 16777215))
        icon1 = QIcon()
        icon1.addFile(u"assets/addList.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.add_to_script_toolButton.setIcon(icon1)
        self.add_to_script_toolButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout_3.addWidget(self.add_to_script_toolButton)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_string = QVBoxLayout()
        self.verticalLayout_string.setObjectName(u"verticalLayout_string")
        self.label_string = QLabel(self.layoutWidget)
        self.label_string.setObjectName(u"label_string")
        self.label_string.setAlignment(Qt.AlignCenter)

        self.verticalLayout_string.addWidget(self.label_string)

        self.triage_string_listWidget = QListWidget(self.layoutWidget)
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
        self.triage_string_listWidget.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.triage_string_listWidget.setDragEnabled(False)
        self.triage_string_listWidget.setDragDropMode(QAbstractItemView.DragOnly)
        self.triage_string_listWidget.setAlternatingRowColors(False)
        self.triage_string_listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.triage_string_listWidget.setSortingEnabled(True)

        self.verticalLayout_string.addWidget(self.triage_string_listWidget)


        self.horizontalLayout_2.addLayout(self.verticalLayout_string)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.ignore_pushButton = QPushButton(self.layoutWidget)
        self.ignore_pushButton.setObjectName(u"ignore_pushButton")
        self.ignore_pushButton.setAutoFillBackground(False)
        self.ignore_pushButton.setFlat(False)

        self.verticalLayout_2.addWidget(self.ignore_pushButton)

        self.unignore_pushButton = QPushButton(self.layoutWidget)
        self.unignore_pushButton.setObjectName(u"unignore_pushButton")

        self.verticalLayout_2.addWidget(self.unignore_pushButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_ignore = QVBoxLayout()
        self.verticalLayout_ignore.setObjectName(u"verticalLayout_ignore")
        self.label_ignore = QLabel(self.layoutWidget)
        self.label_ignore.setObjectName(u"label_ignore")
        self.label_ignore.setEnabled(False)
        self.label_ignore.setAlignment(Qt.AlignCenter)

        self.verticalLayout_ignore.addWidget(self.label_ignore)

        self.triage_ignore_listWidget = QListWidget(self.layoutWidget)
        self.triage_ignore_listWidget.setObjectName(u"triage_ignore_listWidget")
        self.triage_ignore_listWidget.setStyleSheet(u"background-color: rgb(253, 223, 223);\n"
"color: black;")
        self.triage_ignore_listWidget.setDragEnabled(False)
        self.triage_ignore_listWidget.setDragDropMode(QAbstractItemView.DragDrop)
        self.triage_ignore_listWidget.setSortingEnabled(True)

        self.verticalLayout_ignore.addWidget(self.triage_ignore_listWidget)


        self.horizontalLayout_2.addLayout(self.verticalLayout_ignore)


        self.verticalLayout_9.addLayout(self.horizontalLayout_2)


        self.verticalLayout_10.addLayout(self.verticalLayout_9)

        self.splitter_2.addWidget(self.layoutWidget)
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
        self.verticalLayout_7 = QVBoxLayout(self.script_preview_tab)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.splitter = QSplitter(self.script_preview_tab)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.layoutWidget1 = QWidget(self.splitter)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.script_load_toolButton = QToolButton(self.layoutWidget1)
        self.script_load_toolButton.setObjectName(u"script_load_toolButton")
        icon2 = QIcon()
        icon2.addFile(u"assets/open_line.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.script_load_toolButton.setIcon(icon2)
        self.script_load_toolButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_6.addWidget(self.script_load_toolButton)

        self.script_save_toolButton = QToolButton(self.layoutWidget1)
        self.script_save_toolButton.setObjectName(u"script_save_toolButton")
        icon3 = QIcon()
        icon3.addFile(u"assets/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.script_save_toolButton.setIcon(icon3)
        self.script_save_toolButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.script_save_toolButton.setArrowType(Qt.NoArrow)

        self.horizontalLayout_6.addWidget(self.script_save_toolButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.script_run_toolButton = QToolButton(self.layoutWidget1)
        self.script_run_toolButton.setObjectName(u"script_run_toolButton")
        icon4 = QIcon()
        icon4.addFile(u"assets/run.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.script_run_toolButton.setIcon(icon4)
        self.script_run_toolButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_6.addWidget(self.script_run_toolButton)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.script_preview_plainTextEdit = QPlainTextEdit(self.layoutWidget1)
        self.script_preview_plainTextEdit.setObjectName(u"script_preview_plainTextEdit")
        font = QFont()
        font.setFamilies([u"Courier New"])
        self.script_preview_plainTextEdit.setFont(font)
        self.script_preview_plainTextEdit.setPlainText(u"")
        self.script_preview_plainTextEdit.setTabStopDistance(32.000000000000000)

        self.verticalLayout_5.addWidget(self.script_preview_plainTextEdit)

        self.splitter.addWidget(self.layoutWidget1)
        self.script_preview_consoleWidget = ConsoleWidget(self.splitter)
        self.script_preview_consoleWidget.setObjectName(u"script_preview_consoleWidget")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.script_preview_consoleWidget.sizePolicy().hasHeightForWidth())
        self.script_preview_consoleWidget.setSizePolicy(sizePolicy10)
        self.splitter.addWidget(self.script_preview_consoleWidget)

        self.verticalLayout_7.addWidget(self.splitter)

        self.preview_tabWidget.addTab(self.script_preview_tab, "")
        self.splitter_2.addWidget(self.preview_tabWidget)

        self.verticalLayout_12.addWidget(self.splitter_2)

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
        self.export_tab.setEnabled(True)
        self.tabWidget_main.addTab(self.export_tab, "")

        self.verticalLayout_11.addWidget(self.tabWidget_main)

        ColliderScopeUI.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ColliderScopeUI)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1025, 24))
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
        self.import_excel_header_lineEdit.editingFinished.connect(ColliderScopeUI.load_file_preview)
        self.import_csv_delimiter_comboBox.currentTextChanged.connect(ColliderScopeUI.load_file_preview)
        self.import_csv_encoding_comboBox.currentTextChanged.connect(ColliderScopeUI.load_file_preview)
        self.import_csv_skip_rows_lineEdit.editingFinished.connect(ColliderScopeUI.load_file_preview)
        self.import_csv_skip_blank_lines_comboBox.currentTextChanged.connect(ColliderScopeUI.load_file_preview)
        self.import_csv_freeform_options_plainTextEdit.textChanged.connect(ColliderScopeUI.load_file_preview)
        self.triage_string_listWidget.itemSelectionChanged.connect(ColliderScopeUI.update_string_preview)
        self.triage_numeric_listWidget.itemSelectionChanged.connect(ColliderScopeUI.update_numeric_preview)
        self.script_run_toolButton.clicked.connect(ColliderScopeUI.script_run)
        self.script_load_toolButton.clicked.connect(ColliderScopeUI.script_open)
        self.script_save_toolButton.clicked.connect(ColliderScopeUI.script_save)
        self.add_to_script_toolButton.clicked.connect(ColliderScopeUI.add_to_script)
        self.triage_string_listWidget.itemDoubleClicked.connect(ColliderScopeUI.force_string_preview)
        self.triage_numeric_listWidget.itemDoubleClicked.connect(ColliderScopeUI.force_numeric_preview)
        self.triage_ignore_listWidget.currentItemChanged.connect(ColliderScopeUI.generic_slot)
        self.import_csv_two_row_header_comboBox.currentTextChanged.connect(ColliderScopeUI.load_file_preview)
        self.import_excel_two_row_header_comboBox.currentTextChanged.connect(ColliderScopeUI.load_file_preview)
        self.import_excel_sheet_comboBox.currentIndexChanged.connect(ColliderScopeUI.load_file_preview)
        self.preview_size_checkBox.stateChanged.connect(ColliderScopeUI.load_file_preview)
        self.preview_size_spinBox.editingFinished.connect(ColliderScopeUI.load_file_preview)
        self.import_csv_help_toolButton.clicked.connect(ColliderScopeUI.get_csv_help)
        self.import_excel_help_toolButton.clicked.connect(ColliderScopeUI.get_excel_help)

        self.tabWidget_main.setCurrentIndex(0)
        self.file_import_browse_pushButton.setDefault(True)
        self.file_import_tabWidget.setCurrentIndex(0)
        self.import_csv_encoding_comboBox.setCurrentIndex(0)
        self.import_csv_two_row_header_comboBox.setCurrentIndex(1)
        self.import_excel_two_row_header_comboBox.setCurrentIndex(1)
        self.import_excel_pushButton.setDefault(False)
        self.preview_tabWidget.setCurrentIndex(1)


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
        self.preview_size_checkBox.setText(QCoreApplication.translate("ColliderScopeUI", u"Limit", None))
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

        self.import_csv_two_row_header_lines_label.setText(QCoreApplication.translate("ColliderScopeUI", u"two-row header", None))
        self.import_csv_two_row_header_comboBox.setItemText(0, QCoreApplication.translate("ColliderScopeUI", u"True", None))
        self.import_csv_two_row_header_comboBox.setItemText(1, QCoreApplication.translate("ColliderScopeUI", u"False", None))

        self.import_csv_help_toolButton.setText(QCoreApplication.translate("ColliderScopeUI", u"...", None))
        self.import_csv_freeform_label.setText(QCoreApplication.translate("ColliderScopeUI", u"read_csv freeform options:", None))
        self.import_csv_freeform_options_plainTextEdit.setPlaceholderText(QCoreApplication.translate("ColliderScopeUI", u"e.g. nrows=100, engine=python, etc...", None))
        self.import_csv_pushButton.setText(QCoreApplication.translate("ColliderScopeUI", u"Import", None))
        self.file_import_tabWidget.setTabText(self.file_import_tabWidget.indexOf(self.import_csv_tab), QCoreApplication.translate("ColliderScopeUI", u"CSV", None))
        self.import_excel_skip_rows_label.setText(QCoreApplication.translate("ColliderScopeUI", u"skiprows", None))
        self.import_excel_skip_rows_lineEdit.setText(QCoreApplication.translate("ColliderScopeUI", u"0", None))
        self.import_excel_sheet_label.setText(QCoreApplication.translate("ColliderScopeUI", u"sheet", None))
        self.import_excel_header_label.setText(QCoreApplication.translate("ColliderScopeUI", u"header", None))
        self.import_excel_header_lineEdit.setText(QCoreApplication.translate("ColliderScopeUI", u"0", None))
        self.import_excel_two_row_header_lines_label.setText(QCoreApplication.translate("ColliderScopeUI", u"two-row header", None))
        self.import_excel_two_row_header_comboBox.setItemText(0, QCoreApplication.translate("ColliderScopeUI", u"True", None))
        self.import_excel_two_row_header_comboBox.setItemText(1, QCoreApplication.translate("ColliderScopeUI", u"False", None))

        self.import_excel_help_toolButton.setText(QCoreApplication.translate("ColliderScopeUI", u"...", None))
        self.label_2.setText(QCoreApplication.translate("ColliderScopeUI", u"read_excel freeform options:", None))
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("ColliderScopeUI", u"e.g. decimal=',' etc...", None))
        self.import_excel_pushButton.setText(QCoreApplication.translate("ColliderScopeUI", u"Import", None))
        self.file_import_tabWidget.setTabText(self.file_import_tabWidget.indexOf(self.import_excel_tab), QCoreApplication.translate("ColliderScopeUI", u"Excel", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.import_tab), QCoreApplication.translate("ColliderScopeUI", u"Import", None))
        self.label.setText(QCoreApplication.translate("ColliderScopeUI", u"Data Preview and Triage", None))
        self.label_numeric.setText(QCoreApplication.translate("ColliderScopeUI", u"Numeric (Plot Sources)", None))
        self.add_to_script_toolButton.setText(QCoreApplication.translate("ColliderScopeUI", u"Add\n"
"To\n"
"Script", None))
        self.label_string.setText(QCoreApplication.translate("ColliderScopeUI", u"Strings", None))
        self.ignore_pushButton.setText(QCoreApplication.translate("ColliderScopeUI", u">>>", None))
        self.unignore_pushButton.setText(QCoreApplication.translate("ColliderScopeUI", u"<<<", None))
        self.label_ignore.setText(QCoreApplication.translate("ColliderScopeUI", u"Ignore", None))
        self.preview_tabWidget.setTabText(self.preview_tabWidget.indexOf(self.text_preview_tab), QCoreApplication.translate("ColliderScopeUI", u"Text Preview", None))
        self.preview_tabWidget.setTabText(self.preview_tabWidget.indexOf(self.graphic_preview_tab), QCoreApplication.translate("ColliderScopeUI", u"Graphic Preview", None))
#if QT_CONFIG(tooltip)
        self.script_load_toolButton.setToolTip(QCoreApplication.translate("ColliderScopeUI", u"Load Script", None))
#endif // QT_CONFIG(tooltip)
        self.script_load_toolButton.setText(QCoreApplication.translate("ColliderScopeUI", u"Open", None))
#if QT_CONFIG(tooltip)
        self.script_save_toolButton.setToolTip(QCoreApplication.translate("ColliderScopeUI", u"Save Script", None))
#endif // QT_CONFIG(tooltip)
        self.script_save_toolButton.setText(QCoreApplication.translate("ColliderScopeUI", u"Save", None))
#if QT_CONFIG(tooltip)
        self.script_run_toolButton.setToolTip(QCoreApplication.translate("ColliderScopeUI", u"Run Script", None))
#endif // QT_CONFIG(tooltip)
        self.script_run_toolButton.setText(QCoreApplication.translate("ColliderScopeUI", u"Run", None))
        self.script_preview_plainTextEdit.setPlaceholderText(QCoreApplication.translate("ColliderScopeUI", u"print('hello world!')", None))
        self.preview_tabWidget.setTabText(self.preview_tabWidget.indexOf(self.script_preview_tab), QCoreApplication.translate("ColliderScopeUI", u"Preprocess Script", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.triage_tab), QCoreApplication.translate("ColliderScopeUI", u"Data Triage", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.plot_tab), QCoreApplication.translate("ColliderScopeUI", u"Plotting", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.export_tab), QCoreApplication.translate("ColliderScopeUI", u"Export", None))
        self.menuColliderScope2024.setTitle(QCoreApplication.translate("ColliderScopeUI", u"Menu", None))
    # retranslateUi

