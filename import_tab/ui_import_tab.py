# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'import_tab.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QCheckBox,
    QComboBox, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QPushButton,
    QRadioButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSpinBox, QTabWidget, QTableWidget, QTableWidgetItem,
    QToolButton, QVBoxLayout, QWidget)

class Ui_ImportTabWidget(object):
    def setupUi(self, ImportTabWidget):
        if not ImportTabWidget.objectName():
            ImportTabWidget.setObjectName(u"ImportTabWidget")
        self.verticalLayout_21 = QVBoxLayout(ImportTabWidget)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.file_import_browse_horizontalLayout = QHBoxLayout()
        self.file_import_browse_horizontalLayout.setObjectName(u"file_import_browse_horizontalLayout")
        self.filepathname_label = QLabel(ImportTabWidget)
        self.filepathname_label.setObjectName(u"filepathname_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filepathname_label.sizePolicy().hasHeightForWidth())
        self.filepathname_label.setSizePolicy(sizePolicy)

        self.file_import_browse_horizontalLayout.addWidget(self.filepathname_label)

        self.filepathname_lineEdit = QLineEdit(ImportTabWidget)
        self.filepathname_lineEdit.setObjectName(u"filepathname_lineEdit")
        self.filepathname_lineEdit.setEnabled(False)
        self.filepathname_lineEdit.setClearButtonEnabled(False)

        self.file_import_browse_horizontalLayout.addWidget(self.filepathname_lineEdit)

        self.file_import_browse_pushButton = QPushButton(ImportTabWidget)
        self.file_import_browse_pushButton.setObjectName(u"file_import_browse_pushButton")
        self.file_import_browse_pushButton.setAutoDefault(True)

        self.file_import_browse_horizontalLayout.addWidget(self.file_import_browse_pushButton)


        self.verticalLayout_13.addLayout(self.file_import_browse_horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.preview_verticalLayout = QVBoxLayout()
        self.preview_verticalLayout.setObjectName(u"preview_verticalLayout")
        self.file_preview_label = QLabel(ImportTabWidget)
        self.file_preview_label.setObjectName(u"file_preview_label")
        self.file_preview_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.preview_verticalLayout.addWidget(self.file_preview_label)

        self.raw_file_preview_checkBox = QCheckBox(ImportTabWidget)
        self.raw_file_preview_checkBox.setObjectName(u"raw_file_preview_checkBox")

        self.preview_verticalLayout.addWidget(self.raw_file_preview_checkBox)

        self.preview_size_checkBox = QCheckBox(ImportTabWidget)
        self.preview_size_checkBox.setObjectName(u"preview_size_checkBox")
        self.preview_size_checkBox.setChecked(True)

        self.preview_verticalLayout.addWidget(self.preview_size_checkBox)

        self.preview_size_spinBox = QSpinBox(ImportTabWidget)
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

        self.file_preview_tableWidget = QTableWidget(ImportTabWidget)
        if (self.file_preview_tableWidget.columnCount() < 1):
            self.file_preview_tableWidget.setColumnCount(1)
        self.file_preview_tableWidget.setObjectName(u"file_preview_tableWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.file_preview_tableWidget.sizePolicy().hasHeightForWidth())
        self.file_preview_tableWidget.setSizePolicy(sizePolicy1)
        self.file_preview_tableWidget.setMinimumSize(QSize(0, 0))
        self.file_preview_tableWidget.setMaximumSize(QSize(16777215, 16777208))
        font = QFont()
        font.setFamilies([u"Courier New"])
        font.setPointSize(13)
        self.file_preview_tableWidget.setFont(font)
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
        self.file_import_tabWidget = QTabWidget(ImportTabWidget)
        self.file_import_tabWidget.setObjectName(u"file_import_tabWidget")
        self.file_import_tabWidget.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.file_import_tabWidget.sizePolicy().hasHeightForWidth())
        self.file_import_tabWidget.setSizePolicy(sizePolicy2)
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
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy3)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 274, 521))
        self.verticalLayout_20 = QVBoxLayout(self.scrollAreaWidgetContents)
#ifndef Q_OS_MAC
        self.verticalLayout_20.setSpacing(-1)
#endif
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_20.setContentsMargins(5, 5, 5, 5)
        self.import_csv_encoding_horizontalLayout = QHBoxLayout()
        self.import_csv_encoding_horizontalLayout.setObjectName(u"import_csv_encoding_horizontalLayout")
        self.import_csv_encoding_label = QLabel(self.scrollAreaWidgetContents)
        self.import_csv_encoding_label.setObjectName(u"import_csv_encoding_label")
        self.import_csv_encoding_label.setMinimumSize(QSize(70, 0))

        self.import_csv_encoding_horizontalLayout.addWidget(self.import_csv_encoding_label)

        self.import_csv_encoding_comboBox = QComboBox(self.scrollAreaWidgetContents)
        self.import_csv_encoding_comboBox.addItem(u"utf_8")
        self.import_csv_encoding_comboBox.addItem(u"cp1253")
        self.import_csv_encoding_comboBox.addItem("")
        self.import_csv_encoding_comboBox.setObjectName(u"import_csv_encoding_comboBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.import_csv_encoding_comboBox.sizePolicy().hasHeightForWidth())
        self.import_csv_encoding_comboBox.setSizePolicy(sizePolicy4)
        self.import_csv_encoding_comboBox.setMaximumSize(QSize(16777215, 16777215))
        self.import_csv_encoding_comboBox.setEditable(True)

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
        sizePolicy4.setHeightForWidth(self.import_csv_delimiter_comboBox.sizePolicy().hasHeightForWidth())
        self.import_csv_delimiter_comboBox.setSizePolicy(sizePolicy4)
        self.import_csv_delimiter_comboBox.setMaximumSize(QSize(16777215, 16777215))
        self.import_csv_delimiter_comboBox.setEditable(True)

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
        sizePolicy2.setHeightForWidth(self.import_csv_parameter_tableWidget.sizePolicy().hasHeightForWidth())
        self.import_csv_parameter_tableWidget.setSizePolicy(sizePolicy2)
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
        sizePolicy4.setHeightForWidth(self.import_csv_pushButton.sizePolicy().hasHeightForWidth())
        self.import_csv_pushButton.setSizePolicy(sizePolicy4)
        self.import_csv_pushButton.setAutoDefault(True)

        self.verticalLayout.addWidget(self.import_csv_pushButton)

        self.file_import_tabWidget.addTab(self.import_csv_tab, "")
        self.import_excel_tab = QWidget()
        self.import_excel_tab.setObjectName(u"import_excel_tab")
        self.verticalLayout_22 = QVBoxLayout(self.import_excel_tab)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(5, 5, 5, 5)
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
        sizePolicy2.setHeightForWidth(self.import_excel_parameter_tableWidget.sizePolicy().hasHeightForWidth())
        self.import_excel_parameter_tableWidget.setSizePolicy(sizePolicy2)
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
        sizePolicy4.setHeightForWidth(self.import_excel_pushButton.sizePolicy().hasHeightForWidth())
        self.import_excel_pushButton.setSizePolicy(sizePolicy4)
        self.import_excel_pushButton.setMinimumSize(QSize(252, 0))
        self.import_excel_pushButton.setAutoDefault(True)
        self.import_excel_pushButton.setFlat(False)

        self.verticalLayout_8.addWidget(self.import_excel_pushButton)


        self.verticalLayout_22.addLayout(self.verticalLayout_8)

        self.file_import_tabWidget.addTab(self.import_excel_tab, "")

        self.verticalLayout_6.addWidget(self.file_import_tabWidget)

        self.column_groupBox = QGroupBox(ImportTabWidget)
        self.column_groupBox.setObjectName(u"column_groupBox")
        self.column_groupBox.setEnabled(False)
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.column_groupBox.sizePolicy().hasHeightForWidth())
        self.column_groupBox.setSizePolicy(sizePolicy5)
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

        self.row_groupBox = QGroupBox(ImportTabWidget)
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

        self.verticalSpacer_6 = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_6.addItem(self.verticalSpacer_6)


        self.horizontalLayout_9.addLayout(self.verticalLayout_6)


        self.verticalLayout_21.addLayout(self.horizontalLayout_9)


        self.retranslateUi(ImportTabWidget)
        self.import_excel_pushButton.clicked.connect(ImportTabWidget.import_excel_file)
        self.filepathname_lineEdit.returnPressed.connect(ImportTabWidget.filepathname_changed)
        self.import_csv_pushButton.clicked.connect(ImportTabWidget.import_csv_file)
        self.file_import_browse_pushButton.clicked.connect(ImportTabWidget.import_filebrowse)
        self.import_excel_skip_rows_lineEdit.editingFinished.connect(ImportTabWidget.load_file_preview)
        self.import_csv_delimiter_comboBox.activated.connect(ImportTabWidget.load_file_preview)
        self.import_csv_encoding_comboBox.activated.connect(ImportTabWidget.load_file_preview)
        self.import_csv_skip_blank_lines_comboBox.activated.connect(ImportTabWidget.load_file_preview)
        self.import_excel_sheet_comboBox.activated.connect(ImportTabWidget.load_file_preview)
        self.preview_size_checkBox.stateChanged.connect(ImportTabWidget.load_file_preview)
        self.preview_size_spinBox.editingFinished.connect(ImportTabWidget.load_file_preview)
        self.import_csv_help_toolButton.clicked.connect(ImportTabWidget.get_csv_help)
        self.import_excel_help_toolButton.clicked.connect(ImportTabWidget.get_excel_help)
        self.import_csv_header_row_spinBox.editingFinished.connect(ImportTabWidget.import_csv_header_row_changed)
        self.import_csv_units_row_checkBox.stateChanged.connect(ImportTabWidget.load_file_preview)
        self.import_csv_units_row_spinBox.editingFinished.connect(ImportTabWidget.load_file_preview)
        self.import_excel_header_row_spinBox.editingFinished.connect(ImportTabWidget.import_excel_header_row_changed)
        self.import_excel_units_row_checkBox.stateChanged.connect(ImportTabWidget.load_file_preview)
        self.import_excel_units_row_spinBox.editingFinished.connect(ImportTabWidget.load_file_preview)
        self.import_csv_parameter_tableWidget.itemChanged.connect(ImportTabWidget.import_csv_freeform_changed)
        self.import_excel_parameter_tableWidget.itemChanged.connect(ImportTabWidget.import_excel_freeform_changed)
        self.column_drop_if_any_nans_radioButton.clicked.connect(ImportTabWidget.load_file_preview)
        self.row_drop_if_all_nans_radioButton.clicked.connect(ImportTabWidget.load_file_preview)
        self.column_allow_nans.clicked.connect(ImportTabWidget.load_file_preview)
        self.column_drop_if_all_nans_radioButton.clicked.connect(ImportTabWidget.load_file_preview)
        self.row_allow_nans.clicked.connect(ImportTabWidget.load_file_preview)
        self.row_drop_if_any_nans_radioButton.clicked.connect(ImportTabWidget.load_file_preview)
        self.import_csv_skiprows_lineEdit.editingFinished.connect(ImportTabWidget.load_file_preview)
        self.import_excel_skiprows_lineEdit.editingFinished.connect(ImportTabWidget.load_file_preview)
        self.raw_file_preview_checkBox.clicked.connect(ImportTabWidget.load_file_preview)

        self.file_import_browse_pushButton.setDefault(True)
        self.file_import_tabWidget.setCurrentIndex(0)
        self.import_csv_encoding_comboBox.setCurrentIndex(0)
        self.import_excel_pushButton.setDefault(False)


        QMetaObject.connectSlotsByName(ImportTabWidget)
    # setupUi

    def retranslateUi(self, ImportTabWidget):
        self.filepathname_label.setText(QCoreApplication.translate("ImportTabWidget", u"Filename", None))
        self.filepathname_lineEdit.setPlaceholderText(QCoreApplication.translate("ImportTabWidget", u"path/to/input_file", None))
        self.file_import_browse_pushButton.setText(QCoreApplication.translate("ImportTabWidget", u"Select File ...", None))
        self.file_preview_label.setText(QCoreApplication.translate("ImportTabWidget", u"File\n"
"Preview", None))
        self.raw_file_preview_checkBox.setText(QCoreApplication.translate("ImportTabWidget", u"Raw", None))
        self.preview_size_checkBox.setText(QCoreApplication.translate("ImportTabWidget", u"Limit", None))
        self.import_csv_encoding_label.setText(QCoreApplication.translate("ImportTabWidget", u"encoding", None))
        self.import_csv_encoding_comboBox.setItemText(2, QCoreApplication.translate("ImportTabWidget", u"cp437", None))

        self.import_csv_header_row_label.setText(QCoreApplication.translate("ImportTabWidget", u"header row", None))
        self.import_csv_units_row_checkBox.setText(QCoreApplication.translate("ImportTabWidget", u"units row", None))
        self.import_csv_delimiter_label.setText(QCoreApplication.translate("ImportTabWidget", u"delimiter", None))
        self.import_csv_delimiter_comboBox.setItemText(0, QCoreApplication.translate("ImportTabWidget", u"Auto", None))
        self.import_csv_delimiter_comboBox.setItemText(1, QCoreApplication.translate("ImportTabWidget", u",", None))
        self.import_csv_delimiter_comboBox.setItemText(2, QCoreApplication.translate("ImportTabWidget", u";", None))
        self.import_csv_delimiter_comboBox.setItemText(3, QCoreApplication.translate("ImportTabWidget", u"\\t", None))

        self.import_csv_skip_blank_lines_label.setText(QCoreApplication.translate("ImportTabWidget", u"skip_blank_lines", None))
        self.import_csv_skip_blank_lines_comboBox.setItemText(0, QCoreApplication.translate("ImportTabWidget", u"False", None))
        self.import_csv_skip_blank_lines_comboBox.setItemText(1, QCoreApplication.translate("ImportTabWidget", u"True", None))

        self.label_12.setText(QCoreApplication.translate("ImportTabWidget", u"skiprows", None))
        self.import_csv_skiprows_lineEdit.setPlaceholderText(QCoreApplication.translate("ImportTabWidget", u"0", None))
        self.import_csv_help_toolButton.setText(QCoreApplication.translate("ImportTabWidget", u"...", None))
        self.import_csv_freeform_label.setText(QCoreApplication.translate("ImportTabWidget", u"read_csv keyword arguments:", None))
        ___qtablewidgetitem = self.import_csv_parameter_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ImportTabWidget", u"Parameter", None));
        ___qtablewidgetitem1 = self.import_csv_parameter_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ImportTabWidget", u"Value", None));
        self.import_csv_pushButton.setText(QCoreApplication.translate("ImportTabWidget", u"Import", None))
        self.file_import_tabWidget.setTabText(self.file_import_tabWidget.indexOf(self.import_csv_tab), QCoreApplication.translate("ImportTabWidget", u"CSV", None))
        self.import_excel_skip_rows_label.setText(QCoreApplication.translate("ImportTabWidget", u"skiprows", None))
        self.import_excel_skip_rows_lineEdit.setText(QCoreApplication.translate("ImportTabWidget", u"0", None))
        self.import_excel_sheet_label.setText(QCoreApplication.translate("ImportTabWidget", u"sheet", None))
        self.import_excel_header_row_label.setText(QCoreApplication.translate("ImportTabWidget", u"header row", None))
        self.import_excel_units_row_checkBox.setText(QCoreApplication.translate("ImportTabWidget", u"units row", None))
        self.label_13.setText(QCoreApplication.translate("ImportTabWidget", u"skiprows", None))
        self.import_excel_skiprows_lineEdit.setPlaceholderText(QCoreApplication.translate("ImportTabWidget", u"0", None))
        self.import_excel_help_toolButton.setText(QCoreApplication.translate("ImportTabWidget", u"...", None))
        self.label_2.setText(QCoreApplication.translate("ImportTabWidget", u"read_excel keyword arguments:", None))
        ___qtablewidgetitem2 = self.import_excel_parameter_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ImportTabWidget", u"Parameter", None));
        ___qtablewidgetitem3 = self.import_excel_parameter_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ImportTabWidget", u"Value", None));
        self.import_excel_pushButton.setText(QCoreApplication.translate("ImportTabWidget", u"Import", None))
        self.file_import_tabWidget.setTabText(self.file_import_tabWidget.indexOf(self.import_excel_tab), QCoreApplication.translate("ImportTabWidget", u"Excel", None))
        self.column_groupBox.setTitle(QCoreApplication.translate("ImportTabWidget", u"Columns", None))
        self.column_allow_nans.setText(QCoreApplication.translate("ImportTabWidget", u"Allow NANs", None))
        self.column_drop_if_all_nans_radioButton.setText(QCoreApplication.translate("ImportTabWidget", u"Drop if all NANs", None))
        self.column_drop_if_any_nans_radioButton.setText(QCoreApplication.translate("ImportTabWidget", u"Drop if any NANs", None))
        self.row_groupBox.setTitle(QCoreApplication.translate("ImportTabWidget", u"Rows", None))
        self.row_allow_nans.setText(QCoreApplication.translate("ImportTabWidget", u"Allow NANs", None))
        self.row_drop_if_all_nans_radioButton.setText(QCoreApplication.translate("ImportTabWidget", u"Drop if all NANs", None))
        self.row_drop_if_any_nans_radioButton.setText(QCoreApplication.translate("ImportTabWidget", u"Drop if any NANs", None))
        pass
    # retranslateUi

