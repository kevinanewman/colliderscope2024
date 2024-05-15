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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QButtonGroup,
    QCheckBox, QComboBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QPlainTextEdit,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QSpacerItem, QSpinBox, QSplitter, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QToolButton,
    QVBoxLayout, QWidget)

from filterwidget import FilterWidget
from pyqtgraph import PlotWidget
from pyqtgraph.console import ConsoleWidget

class Ui_ColliderScopeUI(object):
    def setupUi(self, ColliderScopeUI):
        if not ColliderScopeUI.objectName():
            ColliderScopeUI.setObjectName(u"ColliderScopeUI")
        ColliderScopeUI.resize(1055, 833)
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
        self.verticalLayout_21 = QVBoxLayout(self.import_tab)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
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


        self.verticalLayout_13.addLayout(self.file_import_browse_horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.preview_verticalLayout = QVBoxLayout()
        self.preview_verticalLayout.setObjectName(u"preview_verticalLayout")
        self.file_preview_label = QLabel(self.import_tab)
        self.file_preview_label.setObjectName(u"file_preview_label")
        self.file_preview_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.preview_verticalLayout.addWidget(self.file_preview_label)

        self.preview_size_checkBox = QCheckBox(self.import_tab)
        self.preview_size_checkBox.setObjectName(u"preview_size_checkBox")
        self.preview_size_checkBox.setChecked(True)

        self.preview_verticalLayout.addWidget(self.preview_size_checkBox)

        self.preview_size_spinBox = QSpinBox(self.import_tab)
        self.preview_size_spinBox.setObjectName(u"preview_size_spinBox")
        self.preview_size_spinBox.setWrapping(False)
        self.preview_size_spinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.preview_size_spinBox.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.preview_size_spinBox.setAccelerated(True)
        self.preview_size_spinBox.setMinimum(10)
        self.preview_size_spinBox.setMaximum(1000000)
        self.preview_size_spinBox.setSingleStep(100)
        self.preview_size_spinBox.setValue(100)

        self.preview_verticalLayout.addWidget(self.preview_size_spinBox)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.preview_verticalLayout.addItem(self.verticalSpacer_4)


        self.horizontalLayout_3.addLayout(self.preview_verticalLayout)

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


        self.verticalLayout_13.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_9.addLayout(self.verticalLayout_13)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 0, 5)
        self.file_import_tabWidget = QTabWidget(self.import_tab)
        self.file_import_tabWidget.setObjectName(u"file_import_tabWidget")
        self.file_import_tabWidget.setEnabled(False)
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.file_import_tabWidget.sizePolicy().hasHeightForWidth())
        self.file_import_tabWidget.setSizePolicy(sizePolicy4)
        self.file_import_tabWidget.setMinimumSize(QSize(275, 0))
        self.file_import_tabWidget.setMaximumSize(QSize(16777215, 600))
        self.file_import_tabWidget.setDocumentMode(True)
        self.import_csv_tab = QWidget()
        self.import_csv_tab.setObjectName(u"import_csv_tab")
        self.verticalLayout = QVBoxLayout(self.import_csv_tab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.import_csv_tab)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy5)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 273, 482))
        self.verticalLayout_20 = QVBoxLayout(self.scrollAreaWidgetContents)
#ifndef Q_OS_MAC
        self.verticalLayout_20.setSpacing(-1)
#endif
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.import_csv_encoding_horizontalLayout = QHBoxLayout()
        self.import_csv_encoding_horizontalLayout.setObjectName(u"import_csv_encoding_horizontalLayout")
        self.import_csv_encoding_label = QLabel(self.scrollAreaWidgetContents)
        self.import_csv_encoding_label.setObjectName(u"import_csv_encoding_label")
        self.import_csv_encoding_label.setMinimumSize(QSize(70, 0))

        self.import_csv_encoding_horizontalLayout.addWidget(self.import_csv_encoding_label)

        self.import_csv_encoding_comboBox = QComboBox(self.scrollAreaWidgetContents)
        self.import_csv_encoding_comboBox.addItem(u"utf_8")
        self.import_csv_encoding_comboBox.addItem(u"cp1253")
        self.import_csv_encoding_comboBox.setObjectName(u"import_csv_encoding_comboBox")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.import_csv_encoding_comboBox.sizePolicy().hasHeightForWidth())
        self.import_csv_encoding_comboBox.setSizePolicy(sizePolicy6)
        self.import_csv_encoding_comboBox.setMaximumSize(QSize(16777215, 16777215))

        self.import_csv_encoding_horizontalLayout.addWidget(self.import_csv_encoding_comboBox)


        self.verticalLayout_20.addLayout(self.import_csv_encoding_horizontalLayout)

        self.import_csv_header_row_horizontalLayout = QHBoxLayout()
        self.import_csv_header_row_horizontalLayout.setObjectName(u"import_csv_header_row_horizontalLayout")
        self.import_csv_header_row_label = QLabel(self.scrollAreaWidgetContents)
        self.import_csv_header_row_label.setObjectName(u"import_csv_header_row_label")
        self.import_csv_header_row_label.setMinimumSize(QSize(70, 0))

        self.import_csv_header_row_horizontalLayout.addWidget(self.import_csv_header_row_label)

        self.import_csv_header_row_spinBox = QSpinBox(self.scrollAreaWidgetContents)
        self.import_csv_header_row_spinBox.setObjectName(u"import_csv_header_row_spinBox")
        self.import_csv_header_row_spinBox.setWrapping(False)
        self.import_csv_header_row_spinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.import_csv_header_row_spinBox.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.import_csv_header_row_spinBox.setAccelerated(True)
        self.import_csv_header_row_spinBox.setMinimum(0)
        self.import_csv_header_row_spinBox.setMaximum(1000000)
        self.import_csv_header_row_spinBox.setSingleStep(1)
        self.import_csv_header_row_spinBox.setValue(0)

        self.import_csv_header_row_horizontalLayout.addWidget(self.import_csv_header_row_spinBox)


        self.verticalLayout_20.addLayout(self.import_csv_header_row_horizontalLayout)

        self.import_csv_units_row_horizontalLayout = QHBoxLayout()
        self.import_csv_units_row_horizontalLayout.setObjectName(u"import_csv_units_row_horizontalLayout")
        self.import_csv_units_row_checkBox = QCheckBox(self.scrollAreaWidgetContents)
        self.import_csv_units_row_checkBox.setObjectName(u"import_csv_units_row_checkBox")

        self.import_csv_units_row_horizontalLayout.addWidget(self.import_csv_units_row_checkBox)

        self.import_csv_units_row_spinBox = QSpinBox(self.scrollAreaWidgetContents)
        self.import_csv_units_row_spinBox.setObjectName(u"import_csv_units_row_spinBox")
        self.import_csv_units_row_spinBox.setEnabled(False)
        self.import_csv_units_row_spinBox.setWrapping(False)
        self.import_csv_units_row_spinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.import_csv_units_row_spinBox.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.import_csv_units_row_spinBox.setAccelerated(True)
        self.import_csv_units_row_spinBox.setMinimum(0)
        self.import_csv_units_row_spinBox.setMaximum(1000000)
        self.import_csv_units_row_spinBox.setSingleStep(1)
        self.import_csv_units_row_spinBox.setValue(1)

        self.import_csv_units_row_horizontalLayout.addWidget(self.import_csv_units_row_spinBox)


        self.verticalLayout_20.addLayout(self.import_csv_units_row_horizontalLayout)

        self.import_csv_delimiter_horizontalLayout = QHBoxLayout()
        self.import_csv_delimiter_horizontalLayout.setObjectName(u"import_csv_delimiter_horizontalLayout")
        self.import_csv_delimiter_label = QLabel(self.scrollAreaWidgetContents)
        self.import_csv_delimiter_label.setObjectName(u"import_csv_delimiter_label")
        self.import_csv_delimiter_label.setMinimumSize(QSize(70, 0))

        self.import_csv_delimiter_horizontalLayout.addWidget(self.import_csv_delimiter_label)

        self.import_csv_delimiter_comboBox = QComboBox(self.scrollAreaWidgetContents)
        self.import_csv_delimiter_comboBox.addItem("")
        self.import_csv_delimiter_comboBox.addItem("")
        self.import_csv_delimiter_comboBox.addItem("")
        self.import_csv_delimiter_comboBox.addItem("")
        self.import_csv_delimiter_comboBox.setObjectName(u"import_csv_delimiter_comboBox")
        sizePolicy6.setHeightForWidth(self.import_csv_delimiter_comboBox.sizePolicy().hasHeightForWidth())
        self.import_csv_delimiter_comboBox.setSizePolicy(sizePolicy6)
        self.import_csv_delimiter_comboBox.setMaximumSize(QSize(16777215, 16777215))

        self.import_csv_delimiter_horizontalLayout.addWidget(self.import_csv_delimiter_comboBox)


        self.verticalLayout_20.addLayout(self.import_csv_delimiter_horizontalLayout)

        self.import_csv_skip_blank_lines_horizontalLayout = QHBoxLayout()
        self.import_csv_skip_blank_lines_horizontalLayout.setObjectName(u"import_csv_skip_blank_lines_horizontalLayout")
        self.import_csv_skip_blank_lines_label = QLabel(self.scrollAreaWidgetContents)
        self.import_csv_skip_blank_lines_label.setObjectName(u"import_csv_skip_blank_lines_label")

        self.import_csv_skip_blank_lines_horizontalLayout.addWidget(self.import_csv_skip_blank_lines_label)

        self.import_csv_skip_blank_lines_comboBox = QComboBox(self.scrollAreaWidgetContents)
        self.import_csv_skip_blank_lines_comboBox.addItem("")
        self.import_csv_skip_blank_lines_comboBox.addItem("")
        self.import_csv_skip_blank_lines_comboBox.setObjectName(u"import_csv_skip_blank_lines_comboBox")

        self.import_csv_skip_blank_lines_horizontalLayout.addWidget(self.import_csv_skip_blank_lines_comboBox)


        self.verticalLayout_20.addLayout(self.import_csv_skip_blank_lines_horizontalLayout)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_12 = QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_16.addWidget(self.label_12)

        self.import_csv_skiprows_lineEdit = QLineEdit(self.scrollAreaWidgetContents)
        self.import_csv_skiprows_lineEdit.setObjectName(u"import_csv_skiprows_lineEdit")
        self.import_csv_skiprows_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.import_csv_skiprows_lineEdit.setClearButtonEnabled(True)

        self.horizontalLayout_16.addWidget(self.import_csv_skiprows_lineEdit)


        self.verticalLayout_20.addLayout(self.horizontalLayout_16)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.import_csv_help_toolButton = QToolButton(self.scrollAreaWidgetContents)
        self.import_csv_help_toolButton.setObjectName(u"import_csv_help_toolButton")
        icon = QIcon()
        icon.addFile(u"assets/info.png", QSize(), QIcon.Normal, QIcon.Off)
        self.import_csv_help_toolButton.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.import_csv_help_toolButton)

        self.import_csv_freeform_label = QLabel(self.scrollAreaWidgetContents)
        self.import_csv_freeform_label.setObjectName(u"import_csv_freeform_label")

        self.horizontalLayout_4.addWidget(self.import_csv_freeform_label)


        self.verticalLayout_19.addLayout(self.horizontalLayout_4)

        self.import_csv_parameter_tableWidget = QTableWidget(self.scrollAreaWidgetContents)
        if (self.import_csv_parameter_tableWidget.columnCount() < 2):
            self.import_csv_parameter_tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.import_csv_parameter_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.import_csv_parameter_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.import_csv_parameter_tableWidget.rowCount() < 25):
            self.import_csv_parameter_tableWidget.setRowCount(25)
        self.import_csv_parameter_tableWidget.setObjectName(u"import_csv_parameter_tableWidget")
        sizePolicy4.setHeightForWidth(self.import_csv_parameter_tableWidget.sizePolicy().hasHeightForWidth())
        self.import_csv_parameter_tableWidget.setSizePolicy(sizePolicy4)
        self.import_csv_parameter_tableWidget.setMinimumSize(QSize(0, 190))
        self.import_csv_parameter_tableWidget.setMaximumSize(QSize(300, 300))
        self.import_csv_parameter_tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.import_csv_parameter_tableWidget.setWordWrap(False)
        self.import_csv_parameter_tableWidget.setRowCount(25)
        self.import_csv_parameter_tableWidget.setColumnCount(2)
        self.import_csv_parameter_tableWidget.horizontalHeader().setVisible(True)
        self.import_csv_parameter_tableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.import_csv_parameter_tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.import_csv_parameter_tableWidget.horizontalHeader().setHighlightSections(False)
        self.import_csv_parameter_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.import_csv_parameter_tableWidget.verticalHeader().setVisible(False)
        self.import_csv_parameter_tableWidget.verticalHeader().setMinimumSectionSize(25)
        self.import_csv_parameter_tableWidget.verticalHeader().setDefaultSectionSize(25)
        self.import_csv_parameter_tableWidget.verticalHeader().setHighlightSections(False)
        self.import_csv_parameter_tableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_19.addWidget(self.import_csv_parameter_tableWidget)


        self.verticalLayout_20.addLayout(self.verticalLayout_19)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.import_csv_pushButton = QPushButton(self.import_csv_tab)
        self.import_csv_pushButton.setObjectName(u"import_csv_pushButton")
        sizePolicy6.setHeightForWidth(self.import_csv_pushButton.sizePolicy().hasHeightForWidth())
        self.import_csv_pushButton.setSizePolicy(sizePolicy6)
        self.import_csv_pushButton.setAutoDefault(True)

        self.verticalLayout.addWidget(self.import_csv_pushButton)

        self.file_import_tabWidget.addTab(self.import_csv_tab, "")
        self.import_excel_tab = QWidget()
        self.import_excel_tab.setObjectName(u"import_excel_tab")
        self.verticalLayout_22 = QVBoxLayout(self.import_excel_tab)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
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

        self.import_excel_header_row_horizontalLayout = QHBoxLayout()
        self.import_excel_header_row_horizontalLayout.setObjectName(u"import_excel_header_row_horizontalLayout")
        self.import_excel_header_row_label = QLabel(self.import_excel_tab)
        self.import_excel_header_row_label.setObjectName(u"import_excel_header_row_label")
        self.import_excel_header_row_label.setMinimumSize(QSize(70, 0))

        self.import_excel_header_row_horizontalLayout.addWidget(self.import_excel_header_row_label)

        self.import_excel_header_row_spinBox = QSpinBox(self.import_excel_tab)
        self.import_excel_header_row_spinBox.setObjectName(u"import_excel_header_row_spinBox")
        self.import_excel_header_row_spinBox.setWrapping(False)
        self.import_excel_header_row_spinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.import_excel_header_row_spinBox.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.import_excel_header_row_spinBox.setAccelerated(True)
        self.import_excel_header_row_spinBox.setMinimum(0)
        self.import_excel_header_row_spinBox.setMaximum(1000000)
        self.import_excel_header_row_spinBox.setSingleStep(1)
        self.import_excel_header_row_spinBox.setValue(0)

        self.import_excel_header_row_horizontalLayout.addWidget(self.import_excel_header_row_spinBox)


        self.verticalLayout_8.addLayout(self.import_excel_header_row_horizontalLayout)

        self.import_excel_units_row_horizontalLayout = QHBoxLayout()
        self.import_excel_units_row_horizontalLayout.setObjectName(u"import_excel_units_row_horizontalLayout")
        self.import_excel_units_row_checkBox = QCheckBox(self.import_excel_tab)
        self.import_excel_units_row_checkBox.setObjectName(u"import_excel_units_row_checkBox")

        self.import_excel_units_row_horizontalLayout.addWidget(self.import_excel_units_row_checkBox)

        self.import_excel_units_row_spinBox = QSpinBox(self.import_excel_tab)
        self.import_excel_units_row_spinBox.setObjectName(u"import_excel_units_row_spinBox")
        self.import_excel_units_row_spinBox.setEnabled(False)
        self.import_excel_units_row_spinBox.setWrapping(False)
        self.import_excel_units_row_spinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.import_excel_units_row_spinBox.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.import_excel_units_row_spinBox.setAccelerated(True)
        self.import_excel_units_row_spinBox.setMinimum(0)
        self.import_excel_units_row_spinBox.setMaximum(1000000)
        self.import_excel_units_row_spinBox.setSingleStep(1)
        self.import_excel_units_row_spinBox.setValue(1)

        self.import_excel_units_row_horizontalLayout.addWidget(self.import_excel_units_row_spinBox)


        self.verticalLayout_8.addLayout(self.import_excel_units_row_horizontalLayout)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_13 = QLabel(self.import_excel_tab)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_17.addWidget(self.label_13)

        self.import_excel_skiprows_lineEdit = QLineEdit(self.import_excel_tab)
        self.import_excel_skiprows_lineEdit.setObjectName(u"import_excel_skiprows_lineEdit")
        self.import_excel_skiprows_lineEdit.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.import_excel_skiprows_lineEdit.setClearButtonEnabled(True)

        self.horizontalLayout_17.addWidget(self.import_excel_skiprows_lineEdit)


        self.verticalLayout_8.addLayout(self.horizontalLayout_17)

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

        self.import_excel_parameter_tableWidget = QTableWidget(self.import_excel_tab)
        if (self.import_excel_parameter_tableWidget.columnCount() < 2):
            self.import_excel_parameter_tableWidget.setColumnCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.import_excel_parameter_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.import_excel_parameter_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        if (self.import_excel_parameter_tableWidget.rowCount() < 25):
            self.import_excel_parameter_tableWidget.setRowCount(25)
        self.import_excel_parameter_tableWidget.setObjectName(u"import_excel_parameter_tableWidget")
        sizePolicy4.setHeightForWidth(self.import_excel_parameter_tableWidget.sizePolicy().hasHeightForWidth())
        self.import_excel_parameter_tableWidget.setSizePolicy(sizePolicy4)
        self.import_excel_parameter_tableWidget.setMinimumSize(QSize(0, 190))
        self.import_excel_parameter_tableWidget.setMaximumSize(QSize(300, 190))
        self.import_excel_parameter_tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.import_excel_parameter_tableWidget.setWordWrap(False)
        self.import_excel_parameter_tableWidget.setRowCount(25)
        self.import_excel_parameter_tableWidget.setColumnCount(2)
        self.import_excel_parameter_tableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.import_excel_parameter_tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.import_excel_parameter_tableWidget.horizontalHeader().setHighlightSections(False)
        self.import_excel_parameter_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.import_excel_parameter_tableWidget.verticalHeader().setVisible(False)
        self.import_excel_parameter_tableWidget.verticalHeader().setMinimumSectionSize(25)
        self.import_excel_parameter_tableWidget.verticalHeader().setDefaultSectionSize(25)
        self.import_excel_parameter_tableWidget.verticalHeader().setHighlightSections(False)
        self.import_excel_parameter_tableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_8.addWidget(self.import_excel_parameter_tableWidget)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_5)

        self.import_excel_pushButton = QPushButton(self.import_excel_tab)
        self.import_excel_pushButton.setObjectName(u"import_excel_pushButton")
        sizePolicy6.setHeightForWidth(self.import_excel_pushButton.sizePolicy().hasHeightForWidth())
        self.import_excel_pushButton.setSizePolicy(sizePolicy6)
        self.import_excel_pushButton.setMinimumSize(QSize(252, 0))
        self.import_excel_pushButton.setAutoDefault(True)
        self.import_excel_pushButton.setFlat(False)

        self.verticalLayout_8.addWidget(self.import_excel_pushButton)


        self.verticalLayout_22.addLayout(self.verticalLayout_8)

        self.file_import_tabWidget.addTab(self.import_excel_tab, "")

        self.verticalLayout_6.addWidget(self.file_import_tabWidget)

        self.row_groupBox = QGroupBox(self.import_tab)
        self.row_groupBox.setObjectName(u"row_groupBox")
        self.row_groupBox.setEnabled(False)
        self.row_groupBox.setMaximumSize(QSize(16777215, 86))
        self.verticalLayout_15 = QVBoxLayout(self.row_groupBox)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.row_allow_nans = QRadioButton(self.row_groupBox)
        self.row_allow_nans.setObjectName(u"row_allow_nans")
        self.row_allow_nans.setChecked(True)

        self.verticalLayout_16.addWidget(self.row_allow_nans)

        self.row_drop_if_all_nans_radioButton = QRadioButton(self.row_groupBox)
        self.row_drop_if_all_nans_radioButton.setObjectName(u"row_drop_if_all_nans_radioButton")

        self.verticalLayout_16.addWidget(self.row_drop_if_all_nans_radioButton)

        self.row_drop_if_any_nans_radioButton = QRadioButton(self.row_groupBox)
        self.row_drop_if_any_nans_radioButton.setObjectName(u"row_drop_if_any_nans_radioButton")

        self.verticalLayout_16.addWidget(self.row_drop_if_any_nans_radioButton)


        self.verticalLayout_15.addLayout(self.verticalLayout_16)


        self.verticalLayout_6.addWidget(self.row_groupBox)

        self.column_groupBox = QGroupBox(self.import_tab)
        self.column_groupBox.setObjectName(u"column_groupBox")
        self.column_groupBox.setEnabled(False)
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.column_groupBox.sizePolicy().hasHeightForWidth())
        self.column_groupBox.setSizePolicy(sizePolicy7)
        self.column_groupBox.setMaximumSize(QSize(16777215, 86))
        self.verticalLayout_17 = QVBoxLayout(self.column_groupBox)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.column_allow_nans = QRadioButton(self.column_groupBox)
        self.column_allow_nans.setObjectName(u"column_allow_nans")
        self.column_allow_nans.setChecked(True)

        self.verticalLayout_18.addWidget(self.column_allow_nans)

        self.column_drop_if_all_nans_radioButton = QRadioButton(self.column_groupBox)
        self.column_drop_if_all_nans_radioButton.setObjectName(u"column_drop_if_all_nans_radioButton")

        self.verticalLayout_18.addWidget(self.column_drop_if_all_nans_radioButton)

        self.column_drop_if_any_nans_radioButton = QRadioButton(self.column_groupBox)
        self.column_drop_if_any_nans_radioButton.setObjectName(u"column_drop_if_any_nans_radioButton")

        self.verticalLayout_18.addWidget(self.column_drop_if_any_nans_radioButton)


        self.verticalLayout_17.addLayout(self.verticalLayout_18)


        self.verticalLayout_6.addWidget(self.column_groupBox)

        self.verticalSpacer_6 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_6.addItem(self.verticalSpacer_6)


        self.horizontalLayout_9.addLayout(self.verticalLayout_6)


        self.verticalLayout_21.addLayout(self.horizontalLayout_9)

        self.tabWidget_main.addTab(self.import_tab, "")
        self.triage_tab = QWidget()
        self.triage_tab.setObjectName(u"triage_tab")
        self.triage_tab.setEnabled(False)
        self.verticalLayout_2 = QVBoxLayout(self.triage_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.label = QLabel(self.triage_tab)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout_filter = QHBoxLayout()
        self.horizontalLayout_filter.setObjectName(u"horizontalLayout_filter")
        self.triage_filter_widget = FilterWidget(self.triage_tab)
        self.triage_filter_widget.setObjectName(u"triage_filter_widget")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.triage_filter_widget.sizePolicy().hasHeightForWidth())
        self.triage_filter_widget.setSizePolicy(sizePolicy8)
        self.triage_filter_widget.setMinimumSize(QSize(300, 0))
        self.triage_filter_widget.setMaximumSize(QSize(300, 25))

        self.horizontalLayout_filter.addWidget(self.triage_filter_widget)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_filter.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout_filter)

        self.triage_lists_horizontalLayout = QHBoxLayout()
        self.triage_lists_horizontalLayout.setSpacing(7)
        self.triage_lists_horizontalLayout.setObjectName(u"triage_lists_horizontalLayout")
        self.numeric_verticalLayout = QVBoxLayout()
        self.numeric_verticalLayout.setObjectName(u"numeric_verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.active_numeric_list_label = QLabel(self.triage_tab)
        self.active_numeric_list_label.setObjectName(u"active_numeric_list_label")
        self.active_numeric_list_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.active_numeric_list_label)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.active_numeric_count_label = QLabel(self.triage_tab)
        self.active_numeric_count_label.setObjectName(u"active_numeric_count_label")

        self.horizontalLayout_2.addWidget(self.active_numeric_count_label)


        self.numeric_verticalLayout.addLayout(self.horizontalLayout_2)

        self.triage_numeric_listWidget = QListWidget(self.triage_tab)
        self.triage_numeric_listWidget.setObjectName(u"triage_numeric_listWidget")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.triage_numeric_listWidget.sizePolicy().hasHeightForWidth())
        self.triage_numeric_listWidget.setSizePolicy(sizePolicy9)
        self.triage_numeric_listWidget.setMinimumSize(QSize(296, 202))
        self.triage_numeric_listWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.triage_numeric_listWidget.setStyleSheet(u"background-color: rgb(196, 242, 196);\n"
"color: black\n"
"")
        self.triage_numeric_listWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.triage_numeric_listWidget.setProperty("showDropIndicator", True)
        self.triage_numeric_listWidget.setDragEnabled(False)
        self.triage_numeric_listWidget.setDragDropMode(QAbstractItemView.DragOnly)
        self.triage_numeric_listWidget.setAlternatingRowColors(False)
        self.triage_numeric_listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.triage_numeric_listWidget.setSortingEnabled(True)

        self.numeric_verticalLayout.addWidget(self.triage_numeric_listWidget)


        self.triage_lists_horizontalLayout.addLayout(self.numeric_verticalLayout)

        self.add_to_script_verticalLayout = QVBoxLayout()
        self.add_to_script_verticalLayout.setObjectName(u"add_to_script_verticalLayout")
        self.ignore_deadvars_toolButton = QToolButton(self.triage_tab)
        self.ignore_deadvars_toolButton.setObjectName(u"ignore_deadvars_toolButton")
        icon1 = QIcon()
        icon1.addFile(u"assets/toolbarSkipped.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ignore_deadvars_toolButton.setIcon(icon1)
        self.ignore_deadvars_toolButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.add_to_script_verticalLayout.addWidget(self.ignore_deadvars_toolButton)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.add_to_script_verticalLayout.addItem(self.verticalSpacer_3)

        self.add_to_script_toolButton = QToolButton(self.triage_tab)
        self.add_to_script_toolButton.setObjectName(u"add_to_script_toolButton")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.add_to_script_toolButton.sizePolicy().hasHeightForWidth())
        self.add_to_script_toolButton.setSizePolicy(sizePolicy10)
        self.add_to_script_toolButton.setMinimumSize(QSize(63, 0))
        self.add_to_script_toolButton.setMaximumSize(QSize(40, 16777215))
        icon2 = QIcon()
        icon2.addFile(u"assets/addList.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.add_to_script_toolButton.setIcon(icon2)
        self.add_to_script_toolButton.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.add_to_script_verticalLayout.addWidget(self.add_to_script_toolButton)


        self.triage_lists_horizontalLayout.addLayout(self.add_to_script_verticalLayout)

        self.string_verticalLayout = QVBoxLayout()
        self.string_verticalLayout.setObjectName(u"string_verticalLayout")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_active_string_list = QLabel(self.triage_tab)
        self.label_active_string_list.setObjectName(u"label_active_string_list")
        self.label_active_string_list.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_active_string_list)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_5)

        self.active_string_count_label = QLabel(self.triage_tab)
        self.active_string_count_label.setObjectName(u"active_string_count_label")

        self.horizontalLayout_10.addWidget(self.active_string_count_label)


        self.string_verticalLayout.addLayout(self.horizontalLayout_10)

        self.triage_string_listWidget = QListWidget(self.triage_tab)
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
        self.triage_string_listWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.triage_string_listWidget.setDragEnabled(False)
        self.triage_string_listWidget.setDragDropMode(QAbstractItemView.DragOnly)
        self.triage_string_listWidget.setAlternatingRowColors(False)
        self.triage_string_listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.triage_string_listWidget.setSortingEnabled(True)

        self.string_verticalLayout.addWidget(self.triage_string_listWidget)


        self.triage_lists_horizontalLayout.addLayout(self.string_verticalLayout)

        self.send_buttons_verticalLayout = QVBoxLayout()
        self.send_buttons_verticalLayout.setObjectName(u"send_buttons_verticalLayout")
        self.send_buttons_verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.ignore_pushButton = QPushButton(self.triage_tab)
        self.ignore_pushButton.setObjectName(u"ignore_pushButton")
        sizePolicy.setHeightForWidth(self.ignore_pushButton.sizePolicy().hasHeightForWidth())
        self.ignore_pushButton.setSizePolicy(sizePolicy)
        self.ignore_pushButton.setMaximumSize(QSize(44, 32))
        self.ignore_pushButton.setAutoFillBackground(False)
        self.ignore_pushButton.setFlat(False)

        self.send_buttons_verticalLayout.addWidget(self.ignore_pushButton)

        self.unignore_pushButton = QPushButton(self.triage_tab)
        self.unignore_pushButton.setObjectName(u"unignore_pushButton")
        sizePolicy.setHeightForWidth(self.unignore_pushButton.sizePolicy().hasHeightForWidth())
        self.unignore_pushButton.setSizePolicy(sizePolicy)
        self.unignore_pushButton.setMaximumSize(QSize(44, 32))

        self.send_buttons_verticalLayout.addWidget(self.unignore_pushButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.send_buttons_verticalLayout.addItem(self.verticalSpacer)


        self.triage_lists_horizontalLayout.addLayout(self.send_buttons_verticalLayout)

        self.ignore_favorites_tabWidget = QTabWidget(self.triage_tab)
        self.ignore_favorites_tabWidget.setObjectName(u"ignore_favorites_tabWidget")
        self.ignore_favorites_tabWidget.setDocumentMode(True)
        self.ignore_tab = QWidget()
        self.ignore_tab.setObjectName(u"ignore_tab")
        self.verticalLayout_3 = QVBoxLayout(self.ignore_tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.ignore_count_label = QLabel(self.ignore_tab)
        self.ignore_count_label.setObjectName(u"ignore_count_label")

        self.horizontalLayout_12.addWidget(self.ignore_count_label)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_6)

        self.ignore_delete_toolButton = QToolButton(self.ignore_tab)
        self.ignore_delete_toolButton.setObjectName(u"ignore_delete_toolButton")
        icon3 = QIcon()
        icon3.addFile(u"assets/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ignore_delete_toolButton.setIcon(icon3)

        self.horizontalLayout_12.addWidget(self.ignore_delete_toolButton)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)

        self.triage_ignore_listWidget = QListWidget(self.ignore_tab)
        self.triage_ignore_listWidget.setObjectName(u"triage_ignore_listWidget")
        self.triage_ignore_listWidget.setStyleSheet(u"background-color: rgb(253, 223, 223);\n"
"color: black;")
        self.triage_ignore_listWidget.setDragEnabled(False)
        self.triage_ignore_listWidget.setDragDropMode(QAbstractItemView.DragDrop)
        self.triage_ignore_listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.triage_ignore_listWidget.setSortingEnabled(True)

        self.verticalLayout_3.addWidget(self.triage_ignore_listWidget)

        self.ignore_favorites_tabWidget.addTab(self.ignore_tab, "")
        self.favorites_tab = QWidget()
        self.favorites_tab.setObjectName(u"favorites_tab")
        self.verticalLayout_9 = QVBoxLayout(self.favorites_tab)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 15, 0, 0)
        self.triage_favorites_listWidget = QListWidget(self.favorites_tab)
        self.triage_favorites_listWidget.setObjectName(u"triage_favorites_listWidget")
        self.triage_favorites_listWidget.setStyleSheet(u"background-color: rgb(233, 255, 255);\n"
"color: black;")
        self.triage_favorites_listWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.triage_favorites_listWidget.setDragEnabled(False)
        self.triage_favorites_listWidget.setDragDropMode(QAbstractItemView.DragDrop)
        self.triage_favorites_listWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.triage_favorites_listWidget.setSortingEnabled(True)

        self.verticalLayout_9.addWidget(self.triage_favorites_listWidget)

        self.ignore_favorites_tabWidget.addTab(self.favorites_tab, "")

        self.triage_lists_horizontalLayout.addWidget(self.ignore_favorites_tabWidget)


        self.verticalLayout_2.addLayout(self.triage_lists_horizontalLayout)

        self.preview_tabWidget = QTabWidget(self.triage_tab)
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
        self.layoutWidget = QWidget(self.splitter)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.verticalLayout_5 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.script_load_toolButton = QToolButton(self.layoutWidget)
        self.script_load_toolButton.setObjectName(u"script_load_toolButton")
        icon4 = QIcon()
        icon4.addFile(u"assets/open_line.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.script_load_toolButton.setIcon(icon4)
        self.script_load_toolButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_6.addWidget(self.script_load_toolButton)

        self.script_save_toolButton = QToolButton(self.layoutWidget)
        self.script_save_toolButton.setObjectName(u"script_save_toolButton")
        icon5 = QIcon()
        icon5.addFile(u"assets/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.script_save_toolButton.setIcon(icon5)
        self.script_save_toolButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.script_save_toolButton.setArrowType(Qt.NoArrow)

        self.horizontalLayout_6.addWidget(self.script_save_toolButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.script_run_toolButton = QToolButton(self.layoutWidget)
        self.script_run_toolButton.setObjectName(u"script_run_toolButton")
        icon6 = QIcon()
        icon6.addFile(u"assets/run.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.script_run_toolButton.setIcon(icon6)
        self.script_run_toolButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_6.addWidget(self.script_run_toolButton)


        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.script_preview_plainTextEdit = QPlainTextEdit(self.layoutWidget)
        self.script_preview_plainTextEdit.setObjectName(u"script_preview_plainTextEdit")
        font = QFont()
        font.setFamilies([u"Courier New"])
        self.script_preview_plainTextEdit.setFont(font)
        self.script_preview_plainTextEdit.setPlainText(u"")
        self.script_preview_plainTextEdit.setTabStopDistance(32.000000000000000)

        self.verticalLayout_5.addWidget(self.script_preview_plainTextEdit)

        self.splitter.addWidget(self.layoutWidget)
        self.script_preview_consoleWidget = ConsoleWidget(self.splitter)
        self.script_preview_consoleWidget.setObjectName(u"script_preview_consoleWidget")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.script_preview_consoleWidget.sizePolicy().hasHeightForWidth())
        self.script_preview_consoleWidget.setSizePolicy(sizePolicy11)
        self.splitter.addWidget(self.script_preview_consoleWidget)

        self.verticalLayout_7.addWidget(self.splitter)

        self.preview_tabWidget.addTab(self.script_preview_tab, "")

        self.verticalLayout_2.addWidget(self.preview_tabWidget)

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
        self.verticalLayout_12 = QVBoxLayout(self.export_tab)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.export_options_groupBox = QGroupBox(self.export_tab)
        self.export_options_groupBox.setObjectName(u"export_options_groupBox")
        sizePolicy6.setHeightForWidth(self.export_options_groupBox.sizePolicy().hasHeightForWidth())
        self.export_options_groupBox.setSizePolicy(sizePolicy6)
        self.horizontalLayout_11 = QHBoxLayout(self.export_options_groupBox)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.nanhandler_widget = QWidget(self.export_options_groupBox)
        self.nanhandler_widget.setObjectName(u"nanhandler_widget")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.nanhandler_widget.sizePolicy().hasHeightForWidth())
        self.nanhandler_widget.setSizePolicy(sizePolicy12)

        self.horizontalLayout_11.addWidget(self.nanhandler_widget)

        self.export_signal_buttons_layout = QGroupBox(self.export_options_groupBox)
        self.export_signal_buttons_layout.setObjectName(u"export_signal_buttons_layout")
        self.verticalLayout_10 = QVBoxLayout(self.export_signal_buttons_layout)
#ifndef Q_OS_MAC
        self.verticalLayout_10.setSpacing(-1)
#endif
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setSizeConstraint(QLayout.SetFixedSize)
        self.export_all_radioButton = QRadioButton(self.export_signal_buttons_layout)
        self.export_options_buttonGroup = QButtonGroup(ColliderScopeUI)
        self.export_options_buttonGroup.setObjectName(u"export_options_buttonGroup")
        self.export_options_buttonGroup.addButton(self.export_all_radioButton)
        self.export_all_radioButton.setObjectName(u"export_all_radioButton")
        self.export_all_radioButton.setMaximumSize(QSize(173, 20))
        self.export_all_radioButton.setChecked(True)

        self.verticalLayout_10.addWidget(self.export_all_radioButton)

        self.export_all_but_ignored_radioButton = QRadioButton(self.export_signal_buttons_layout)
        self.export_options_buttonGroup.addButton(self.export_all_but_ignored_radioButton)
        self.export_all_but_ignored_radioButton.setObjectName(u"export_all_but_ignored_radioButton")
        self.export_all_but_ignored_radioButton.setMaximumSize(QSize(173, 20))

        self.verticalLayout_10.addWidget(self.export_all_but_ignored_radioButton)

        self.export_favorites_only_radioButton = QRadioButton(self.export_signal_buttons_layout)
        self.export_options_buttonGroup.addButton(self.export_favorites_only_radioButton)
        self.export_favorites_only_radioButton.setObjectName(u"export_favorites_only_radioButton")
        self.export_favorites_only_radioButton.setMaximumSize(QSize(173, 20))

        self.verticalLayout_10.addWidget(self.export_favorites_only_radioButton)


        self.horizontalLayout_11.addWidget(self.export_signal_buttons_layout)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_7)


        self.verticalLayout_12.addWidget(self.export_options_groupBox)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.export_data_prefix_lineEdit = QLineEdit(self.export_tab)
        self.export_data_prefix_lineEdit.setObjectName(u"export_data_prefix_lineEdit")
        self.export_data_prefix_lineEdit.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_8.addWidget(self.export_data_prefix_lineEdit)

        self.export_data_prefix_filler_comboBox = QComboBox(self.export_tab)
        self.export_data_prefix_filler_comboBox.addItem("")
        self.export_data_prefix_filler_comboBox.addItem("")
        self.export_data_prefix_filler_comboBox.addItem("")
        self.export_data_prefix_filler_comboBox.setObjectName(u"export_data_prefix_filler_comboBox")
        sizePolicy10.setHeightForWidth(self.export_data_prefix_filler_comboBox.sizePolicy().hasHeightForWidth())
        self.export_data_prefix_filler_comboBox.setSizePolicy(sizePolicy10)
        self.export_data_prefix_filler_comboBox.setEditable(True)
        self.export_data_prefix_filler_comboBox.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.export_data_prefix_filler_comboBox.setFrame(False)

        self.horizontalLayout_8.addWidget(self.export_data_prefix_filler_comboBox)

        self.export_data_lineEdit = QLineEdit(self.export_tab)
        self.export_data_lineEdit.setObjectName(u"export_data_lineEdit")

        self.horizontalLayout_8.addWidget(self.export_data_lineEdit)

        self.export_data_suffix_filler_comboBox = QComboBox(self.export_tab)
        self.export_data_suffix_filler_comboBox.addItem("")
        self.export_data_suffix_filler_comboBox.addItem("")
        self.export_data_suffix_filler_comboBox.addItem("")
        self.export_data_suffix_filler_comboBox.setObjectName(u"export_data_suffix_filler_comboBox")
        sizePolicy10.setHeightForWidth(self.export_data_suffix_filler_comboBox.sizePolicy().hasHeightForWidth())
        self.export_data_suffix_filler_comboBox.setSizePolicy(sizePolicy10)
        self.export_data_suffix_filler_comboBox.setEditable(True)
        self.export_data_suffix_filler_comboBox.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.export_data_suffix_filler_comboBox.setFrame(False)

        self.horizontalLayout_8.addWidget(self.export_data_suffix_filler_comboBox)

        self.export_data_suffix_lineEdit = QLineEdit(self.export_tab)
        self.export_data_suffix_lineEdit.setObjectName(u"export_data_suffix_lineEdit")
        self.export_data_suffix_lineEdit.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_8.addWidget(self.export_data_suffix_lineEdit)

        self.export_data_comboBox = QComboBox(self.export_tab)
        self.export_data_comboBox.addItem("")
        self.export_data_comboBox.addItem("")
        self.export_data_comboBox.setObjectName(u"export_data_comboBox")
        self.export_data_comboBox.setMinimumSize(QSize(0, 21))
        self.export_data_comboBox.setMaximumSize(QSize(16777215, 21))

        self.horizontalLayout_8.addWidget(self.export_data_comboBox)

        self.export_data_mode_comboBox = QComboBox(self.export_tab)
        self.export_data_mode_comboBox.addItem("")
        self.export_data_mode_comboBox.addItem("")
        self.export_data_mode_comboBox.setObjectName(u"export_data_mode_comboBox")

        self.horizontalLayout_8.addWidget(self.export_data_mode_comboBox)

        self.export_data_pushButton = QPushButton(self.export_tab)
        self.export_data_pushButton.setObjectName(u"export_data_pushButton")
        self.export_data_pushButton.setAutoDefault(True)

        self.horizontalLayout_8.addWidget(self.export_data_pushButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)


        self.verticalLayout_12.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_7)

        self.scrollArea_2 = QScrollArea(self.export_tab)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 1019, 266))
        self.verticalLayout_14 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_14.setSpacing(5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(5, 5, 5, 5)
        self.verticalSpacer_2 = QSpacerItem(20, 187, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_2)

        self.plot_inputs_label_gridLayout = QGridLayout()
        self.plot_inputs_label_gridLayout.setObjectName(u"plot_inputs_label_gridLayout")
        self.plot_inputs_label_gridLayout.setHorizontalSpacing(5)
        self.plot_inputs_label_gridLayout.setVerticalSpacing(-1)
        self.plot_inputs_label_gridLayout.setContentsMargins(5, 5, 5, 5)
        self.label_6 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.plot_inputs_label_gridLayout.addWidget(self.label_6, 0, 3, 1, 1)

        self.label_10 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.plot_inputs_label_gridLayout.addWidget(self.label_10, 0, 7, 1, 1)

        self.label_4 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 16777215))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.plot_inputs_label_gridLayout.addWidget(self.label_4, 0, 1, 1, 1)

        self.label_11 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 16777215))
        self.label_11.setAlignment(Qt.AlignCenter)

        self.plot_inputs_label_gridLayout.addWidget(self.label_11, 0, 8, 1, 1)

        self.label_9 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 16777215))
        self.label_9.setAlignment(Qt.AlignCenter)

        self.plot_inputs_label_gridLayout.addWidget(self.label_9, 0, 6, 1, 1)

        self.label_3 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 16777215))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.plot_inputs_label_gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_8 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.plot_inputs_label_gridLayout.addWidget(self.label_8, 0, 5, 1, 1)

        self.label_7 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 16777215))
        self.label_7.setAlignment(Qt.AlignCenter)

        self.plot_inputs_label_gridLayout.addWidget(self.label_7, 0, 4, 1, 1)

        self.label_5 = QLabel(self.scrollAreaWidgetContents_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 16777215))
        self.label_5.setAlignment(Qt.AlignCenter)

        self.plot_inputs_label_gridLayout.addWidget(self.label_5, 0, 2, 1, 1)


        self.verticalLayout_14.addLayout(self.plot_inputs_label_gridLayout)

        self.plot_inputs_gridLayout = QGridLayout()
        self.plot_inputs_gridLayout.setObjectName(u"plot_inputs_gridLayout")
        self.plot_inputs_gridLayout.setHorizontalSpacing(5)
        self.plot_inputs_gridLayout.setContentsMargins(5, -1, 5, -1)
        self.comboBox_5 = QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setMinimumSize(QSize(0, 0))

        self.plot_inputs_gridLayout.addWidget(self.comboBox_5, 0, 7, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_8 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_8)

        self.checkBox = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMaximumSize(QSize(19, 16777215))

        self.horizontalLayout_13.addWidget(self.checkBox)

        self.horizontalSpacer_9 = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_9)


        self.plot_inputs_gridLayout.addLayout(self.horizontalLayout_13, 0, 0, 1, 1)

        self.comboBox_2 = QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setMinimumSize(QSize(0, 0))

        self.plot_inputs_gridLayout.addWidget(self.comboBox_2, 0, 2, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_10 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_10)

        self.checkBox_4 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setMaximumSize(QSize(19, 16777215))

        self.horizontalLayout_14.addWidget(self.checkBox_4)

        self.horizontalSpacer_11 = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_11)


        self.plot_inputs_gridLayout.addLayout(self.horizontalLayout_14, 0, 4, 1, 1)

        self.comboBox = QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 0))

        self.plot_inputs_gridLayout.addWidget(self.comboBox, 0, 1, 1, 1)

        self.comboBox_3 = QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setMinimumSize(QSize(0, 0))

        self.plot_inputs_gridLayout.addWidget(self.comboBox_3, 0, 3, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_12 = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_12)

        self.checkBox_5 = QCheckBox(self.scrollAreaWidgetContents_2)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setMaximumSize(QSize(19, 16777215))

        self.horizontalLayout_15.addWidget(self.checkBox_5)

        self.horizontalSpacer_13 = QSpacerItem(10, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_13)


        self.plot_inputs_gridLayout.addLayout(self.horizontalLayout_15, 0, 6, 1, 1)

        self.comboBox_4 = QComboBox(self.scrollAreaWidgetContents_2)
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setMinimumSize(QSize(0, 0))

        self.plot_inputs_gridLayout.addWidget(self.comboBox_4, 0, 5, 1, 1)

        self.toolButton = QToolButton(self.scrollAreaWidgetContents_2)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setMinimumSize(QSize(40, 0))
        self.toolButton.setIcon(icon3)

        self.plot_inputs_gridLayout.addWidget(self.toolButton, 0, 8, 1, 1)

        self.plot_inputs_gridLayout.setColumnStretch(1, 1)
        self.plot_inputs_gridLayout.setColumnStretch(2, 1)
        self.plot_inputs_gridLayout.setColumnStretch(3, 1)
        self.plot_inputs_gridLayout.setColumnMinimumWidth(0, 41)
        self.plot_inputs_gridLayout.setColumnMinimumWidth(1, 100)
        self.plot_inputs_gridLayout.setColumnMinimumWidth(2, 100)
        self.plot_inputs_gridLayout.setColumnMinimumWidth(3, 100)
        self.plot_inputs_gridLayout.setColumnMinimumWidth(4, 41)
        self.plot_inputs_gridLayout.setColumnMinimumWidth(5, 100)
        self.plot_inputs_gridLayout.setColumnMinimumWidth(6, 41)
        self.plot_inputs_gridLayout.setColumnMinimumWidth(7, 100)
        self.plot_inputs_gridLayout.setColumnMinimumWidth(8, 41)

        self.verticalLayout_14.addLayout(self.plot_inputs_gridLayout)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_12.addWidget(self.scrollArea_2)

        self.tabWidget_main.addTab(self.export_tab, "")

        self.verticalLayout_11.addWidget(self.tabWidget_main)

        ColliderScopeUI.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ColliderScopeUI)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1055, 24))
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
        self.import_csv_delimiter_comboBox.activated.connect(ColliderScopeUI.load_file_preview)
        self.import_csv_encoding_comboBox.activated.connect(ColliderScopeUI.load_file_preview)
        self.import_csv_skip_blank_lines_comboBox.activated.connect(ColliderScopeUI.load_file_preview)
        self.triage_string_listWidget.itemSelectionChanged.connect(ColliderScopeUI.string_listwidget_selection_changed)
        self.triage_numeric_listWidget.itemSelectionChanged.connect(ColliderScopeUI.numeric_listwidget_selection_changed)
        self.script_run_toolButton.clicked.connect(ColliderScopeUI.script_run)
        self.script_load_toolButton.clicked.connect(ColliderScopeUI.script_open)
        self.script_save_toolButton.clicked.connect(ColliderScopeUI.script_save)
        self.add_to_script_toolButton.clicked.connect(ColliderScopeUI.add_to_script)
        self.triage_string_listWidget.itemDoubleClicked.connect(ColliderScopeUI.triage_doubleclick_selection_handler)
        self.triage_numeric_listWidget.itemDoubleClicked.connect(ColliderScopeUI.triage_doubleclick_selection_handler)
        self.import_excel_sheet_comboBox.activated.connect(ColliderScopeUI.load_file_preview)
        self.preview_size_checkBox.stateChanged.connect(ColliderScopeUI.load_file_preview)
        self.preview_size_spinBox.editingFinished.connect(ColliderScopeUI.load_file_preview)
        self.import_csv_help_toolButton.clicked.connect(ColliderScopeUI.get_csv_help)
        self.import_excel_help_toolButton.clicked.connect(ColliderScopeUI.get_excel_help)
        self.export_data_pushButton.clicked.connect(ColliderScopeUI.export_data)
        self.export_data_lineEdit.returnPressed.connect(ColliderScopeUI.export_data)
        self.import_csv_header_row_spinBox.editingFinished.connect(ColliderScopeUI.import_csv_header_row_changed)
        self.import_csv_units_row_checkBox.stateChanged.connect(ColliderScopeUI.load_file_preview)
        self.import_csv_units_row_spinBox.editingFinished.connect(ColliderScopeUI.load_file_preview)
        self.import_excel_header_row_spinBox.editingFinished.connect(ColliderScopeUI.import_excel_header_row_changed)
        self.import_excel_units_row_checkBox.stateChanged.connect(ColliderScopeUI.load_file_preview)
        self.import_excel_units_row_spinBox.editingFinished.connect(ColliderScopeUI.load_file_preview)
        self.import_csv_parameter_tableWidget.itemChanged.connect(ColliderScopeUI.import_csv_freeform_changed)
        self.import_excel_parameter_tableWidget.itemChanged.connect(ColliderScopeUI.import_excel_freeform_changed)
        self.ignore_pushButton.clicked.connect(ColliderScopeUI.send_right_pushbutton)
        self.unignore_pushButton.clicked.connect(ColliderScopeUI.send_left_pushbutton)
        self.column_drop_if_any_nans_radioButton.clicked.connect(ColliderScopeUI.load_file_preview)
        self.row_drop_if_all_nans_radioButton.clicked.connect(ColliderScopeUI.load_file_preview)
        self.column_allow_nans.clicked.connect(ColliderScopeUI.load_file_preview)
        self.column_drop_if_all_nans_radioButton.clicked.connect(ColliderScopeUI.load_file_preview)
        self.row_allow_nans.clicked.connect(ColliderScopeUI.load_file_preview)
        self.row_drop_if_any_nans_radioButton.clicked.connect(ColliderScopeUI.load_file_preview)
        self.ignore_deadvars_toolButton.clicked.connect(ColliderScopeUI.ignore_deadvars)
        self.triage_favorites_listWidget.itemDoubleClicked.connect(ColliderScopeUI.triage_doubleclick_selection_handler)
        self.triage_favorites_listWidget.itemSelectionChanged.connect(ColliderScopeUI.favorites_listwidget_selection_changed)
        self.triage_ignore_listWidget.itemSelectionChanged.connect(ColliderScopeUI.ignore_listwidget_selection_changed)
        self.triage_ignore_listWidget.itemDoubleClicked.connect(ColliderScopeUI.triage_doubleclick_selection_handler)
        self.ignore_delete_toolButton.clicked.connect(ColliderScopeUI.delete_ignores)
        self.export_data_mode_comboBox.activated.connect(ColliderScopeUI.update_export_mode)
        self.import_csv_skiprows_lineEdit.editingFinished.connect(ColliderScopeUI.load_file_preview)
        self.import_excel_skiprows_lineEdit.editingFinished.connect(ColliderScopeUI.load_file_preview)

        self.tabWidget_main.setCurrentIndex(0)
        self.file_import_browse_pushButton.setDefault(True)
        self.file_import_tabWidget.setCurrentIndex(0)
        self.import_csv_encoding_comboBox.setCurrentIndex(0)
        self.import_excel_pushButton.setDefault(False)
        self.ignore_favorites_tabWidget.setCurrentIndex(0)
        self.preview_tabWidget.setCurrentIndex(1)
        self.export_data_pushButton.setDefault(True)


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
        self.import_csv_encoding_label.setText(QCoreApplication.translate("ColliderScopeUI", u"encoding", None))

        self.import_csv_header_row_label.setText(QCoreApplication.translate("ColliderScopeUI", u"header row", None))
        self.import_csv_units_row_checkBox.setText(QCoreApplication.translate("ColliderScopeUI", u"units row", None))
        self.import_csv_delimiter_label.setText(QCoreApplication.translate("ColliderScopeUI", u"delimiter", None))
        self.import_csv_delimiter_comboBox.setItemText(0, QCoreApplication.translate("ColliderScopeUI", u"Auto", None))
        self.import_csv_delimiter_comboBox.setItemText(1, QCoreApplication.translate("ColliderScopeUI", u",", None))
        self.import_csv_delimiter_comboBox.setItemText(2, QCoreApplication.translate("ColliderScopeUI", u";", None))
        self.import_csv_delimiter_comboBox.setItemText(3, QCoreApplication.translate("ColliderScopeUI", u"\\t", None))

        self.import_csv_skip_blank_lines_label.setText(QCoreApplication.translate("ColliderScopeUI", u"skip_blank_lines", None))
        self.import_csv_skip_blank_lines_comboBox.setItemText(0, QCoreApplication.translate("ColliderScopeUI", u"True", None))
        self.import_csv_skip_blank_lines_comboBox.setItemText(1, QCoreApplication.translate("ColliderScopeUI", u"False", None))

        self.label_12.setText(QCoreApplication.translate("ColliderScopeUI", u"skiprows", None))
        self.import_csv_skiprows_lineEdit.setPlaceholderText(QCoreApplication.translate("ColliderScopeUI", u"0", None))
        self.import_csv_help_toolButton.setText(QCoreApplication.translate("ColliderScopeUI", u"...", None))
        self.import_csv_freeform_label.setText(QCoreApplication.translate("ColliderScopeUI", u"read_csv keyword arguments:", None))
        ___qtablewidgetitem = self.import_csv_parameter_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ColliderScopeUI", u"Parameter", None));
        ___qtablewidgetitem1 = self.import_csv_parameter_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ColliderScopeUI", u"Value", None));
        self.import_csv_pushButton.setText(QCoreApplication.translate("ColliderScopeUI", u"Import", None))
        self.file_import_tabWidget.setTabText(self.file_import_tabWidget.indexOf(self.import_csv_tab), QCoreApplication.translate("ColliderScopeUI", u"CSV", None))
        self.import_excel_skip_rows_label.setText(QCoreApplication.translate("ColliderScopeUI", u"skiprows", None))
        self.import_excel_skip_rows_lineEdit.setText(QCoreApplication.translate("ColliderScopeUI", u"0", None))
        self.import_excel_sheet_label.setText(QCoreApplication.translate("ColliderScopeUI", u"sheet", None))
        self.import_excel_header_row_label.setText(QCoreApplication.translate("ColliderScopeUI", u"header row", None))
        self.import_excel_units_row_checkBox.setText(QCoreApplication.translate("ColliderScopeUI", u"units row", None))
        self.label_13.setText(QCoreApplication.translate("ColliderScopeUI", u"skiprows", None))
        self.import_excel_skiprows_lineEdit.setPlaceholderText(QCoreApplication.translate("ColliderScopeUI", u"0", None))
        self.import_excel_help_toolButton.setText(QCoreApplication.translate("ColliderScopeUI", u"...", None))
        self.label_2.setText(QCoreApplication.translate("ColliderScopeUI", u"read_excel keyword arguments:", None))
        ___qtablewidgetitem2 = self.import_excel_parameter_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ColliderScopeUI", u"Parameter", None));
        ___qtablewidgetitem3 = self.import_excel_parameter_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ColliderScopeUI", u"Value", None));
        self.import_excel_pushButton.setText(QCoreApplication.translate("ColliderScopeUI", u"Import", None))
        self.file_import_tabWidget.setTabText(self.file_import_tabWidget.indexOf(self.import_excel_tab), QCoreApplication.translate("ColliderScopeUI", u"Excel", None))
        self.row_groupBox.setTitle(QCoreApplication.translate("ColliderScopeUI", u"Rows", None))
        self.row_allow_nans.setText(QCoreApplication.translate("ColliderScopeUI", u"Allow NANs", None))
        self.row_drop_if_all_nans_radioButton.setText(QCoreApplication.translate("ColliderScopeUI", u"Drop if all NANs", None))
        self.row_drop_if_any_nans_radioButton.setText(QCoreApplication.translate("ColliderScopeUI", u"Drop if any NANs", None))
        self.column_groupBox.setTitle(QCoreApplication.translate("ColliderScopeUI", u"Columns", None))
        self.column_allow_nans.setText(QCoreApplication.translate("ColliderScopeUI", u"Allow NANs", None))
        self.column_drop_if_all_nans_radioButton.setText(QCoreApplication.translate("ColliderScopeUI", u"Drop if all NANs", None))
        self.column_drop_if_any_nans_radioButton.setText(QCoreApplication.translate("ColliderScopeUI", u"Drop if any NANs", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.import_tab), QCoreApplication.translate("ColliderScopeUI", u"Import", None))
        self.label.setText(QCoreApplication.translate("ColliderScopeUI", u"Data Preview and Triage", None))
        self.active_numeric_list_label.setText(QCoreApplication.translate("ColliderScopeUI", u"Numeric (Plot Sources)", None))
        self.active_numeric_count_label.setText(QCoreApplication.translate("ColliderScopeUI", u"[0]", None))
        self.ignore_deadvars_toolButton.setText(QCoreApplication.translate("ColliderScopeUI", u"Ignore\n"
"Deadvars", None))
        self.add_to_script_toolButton.setText(QCoreApplication.translate("ColliderScopeUI", u"Add\n"
"To\n"
"Script", None))
        self.label_active_string_list.setText(QCoreApplication.translate("ColliderScopeUI", u"Strings", None))
        self.active_string_count_label.setText(QCoreApplication.translate("ColliderScopeUI", u"[0]", None))
#if QT_CONFIG(tooltip)
        self.ignore_pushButton.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.ignore_pushButton.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.ignore_pushButton.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.ignore_pushButton.setText(QCoreApplication.translate("ColliderScopeUI", u"->", None))
        self.unignore_pushButton.setText(QCoreApplication.translate("ColliderScopeUI", u"<-", None))
        self.ignore_count_label.setText(QCoreApplication.translate("ColliderScopeUI", u"[0]", None))
        self.ignore_delete_toolButton.setText("")
        self.ignore_favorites_tabWidget.setTabText(self.ignore_favorites_tabWidget.indexOf(self.ignore_tab), QCoreApplication.translate("ColliderScopeUI", u"Ignore", None))
        self.ignore_favorites_tabWidget.setTabText(self.ignore_favorites_tabWidget.indexOf(self.favorites_tab), QCoreApplication.translate("ColliderScopeUI", u"Favorites", None))
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
        self.export_options_groupBox.setTitle(QCoreApplication.translate("ColliderScopeUI", u"Export Options", None))
        self.export_signal_buttons_layout.setTitle(QCoreApplication.translate("ColliderScopeUI", u"Signals", None))
        self.export_all_radioButton.setText(QCoreApplication.translate("ColliderScopeUI", u"Export all", None))
        self.export_all_but_ignored_radioButton.setText(QCoreApplication.translate("ColliderScopeUI", u"Export all but Ignored", None))
        self.export_favorites_only_radioButton.setText(QCoreApplication.translate("ColliderScopeUI", u"Export Favorites only", None))
        self.export_data_prefix_lineEdit.setPlaceholderText(QCoreApplication.translate("ColliderScopeUI", u"prefix", None))
        self.export_data_prefix_filler_comboBox.setItemText(0, QCoreApplication.translate("ColliderScopeUI", u"None", None))
        self.export_data_prefix_filler_comboBox.setItemText(1, QCoreApplication.translate("ColliderScopeUI", u".", None))
        self.export_data_prefix_filler_comboBox.setItemText(2, QCoreApplication.translate("ColliderScopeUI", u"-", None))

        self.export_data_suffix_filler_comboBox.setItemText(0, QCoreApplication.translate("ColliderScopeUI", u"None", None))
        self.export_data_suffix_filler_comboBox.setItemText(1, QCoreApplication.translate("ColliderScopeUI", u".", None))
        self.export_data_suffix_filler_comboBox.setItemText(2, QCoreApplication.translate("ColliderScopeUI", u"-", None))

        self.export_data_suffix_lineEdit.setPlaceholderText(QCoreApplication.translate("ColliderScopeUI", u"suffix", None))
        self.export_data_comboBox.setItemText(0, QCoreApplication.translate("ColliderScopeUI", u"CSV", None))
        self.export_data_comboBox.setItemText(1, QCoreApplication.translate("ColliderScopeUI", u"Excel", None))

        self.export_data_mode_comboBox.setItemText(0, QCoreApplication.translate("ColliderScopeUI", u"Single", None))
        self.export_data_mode_comboBox.setItemText(1, QCoreApplication.translate("ColliderScopeUI", u"Batch Process", None))

        self.export_data_pushButton.setText(QCoreApplication.translate("ColliderScopeUI", u"Export", None))
        self.label_6.setText(QCoreApplication.translate("ColliderScopeUI", u"Z", None))
        self.label_10.setText(QCoreApplication.translate("ColliderScopeUI", u"Line", None))
        self.label_4.setText(QCoreApplication.translate("ColliderScopeUI", u"X", None))
        self.label_11.setText(QCoreApplication.translate("ColliderScopeUI", u"Delete", None))
        self.label_9.setText(QCoreApplication.translate("ColliderScopeUI", u"Fill", None))
        self.label_3.setText(QCoreApplication.translate("ColliderScopeUI", u"Enable", None))
        self.label_8.setText(QCoreApplication.translate("ColliderScopeUI", u"Symbol", None))
        self.label_7.setText(QCoreApplication.translate("ColliderScopeUI", u"Label", None))
        self.label_5.setText(QCoreApplication.translate("ColliderScopeUI", u"Y", None))
        self.checkBox.setText("")
        self.checkBox_4.setText("")
        self.checkBox_5.setText("")
        self.toolButton.setText(QCoreApplication.translate("ColliderScopeUI", u"...", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.export_tab), QCoreApplication.translate("ColliderScopeUI", u"Export", None))
        self.menuColliderScope2024.setTitle(QCoreApplication.translate("ColliderScopeUI", u"Menu", None))
    # retranslateUi

