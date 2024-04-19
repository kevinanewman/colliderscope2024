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
    QFrame, QGraphicsView, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QTextBrowser, QTextEdit, QVBoxLayout, QWidget)

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
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
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
        self.tab_import = QWidget()
        self.tab_import.setObjectName(u"tab_import")
        self.horizontalLayout_12 = QHBoxLayout(self.tab_import)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.file_import_browse_horizontalLayout = QHBoxLayout()
        self.file_import_browse_horizontalLayout.setObjectName(u"file_import_browse_horizontalLayout")
        self.filepathname_label = QLabel(self.tab_import)
        self.filepathname_label.setObjectName(u"filepathname_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.filepathname_label.sizePolicy().hasHeightForWidth())
        self.filepathname_label.setSizePolicy(sizePolicy2)

        self.file_import_browse_horizontalLayout.addWidget(self.filepathname_label)

        self.filepathname_lineEdit = QLineEdit(self.tab_import)
        self.filepathname_lineEdit.setObjectName(u"filepathname_lineEdit")
        self.filepathname_lineEdit.setEnabled(True)
        self.filepathname_lineEdit.setClearButtonEnabled(True)

        self.file_import_browse_horizontalLayout.addWidget(self.filepathname_lineEdit)

        self.file_import_browse_pushButton = QPushButton(self.tab_import)
        self.file_import_browse_pushButton.setObjectName(u"file_import_browse_pushButton")

        self.file_import_browse_horizontalLayout.addWidget(self.file_import_browse_pushButton)


        self.verticalLayout_7.addLayout(self.file_import_browse_horizontalLayout)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.file_preview_horizontalLayout = QHBoxLayout()
        self.file_preview_horizontalLayout.setObjectName(u"file_preview_horizontalLayout")
        self.file_preview_label = QLabel(self.tab_import)
        self.file_preview_label.setObjectName(u"file_preview_label")
        self.file_preview_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.file_preview_horizontalLayout.addWidget(self.file_preview_label)

        self.file_preview_tableWidget = QTableWidget(self.tab_import)
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

        self.file_import_tabWidget = QTabWidget(self.tab_import)
        self.file_import_tabWidget.setObjectName(u"file_import_tabWidget")
        self.file_import_tabWidget.setEnabled(True)
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
        self.import_csv_pushButton.setAutoDefault(True)

        self.verticalLayout.addWidget(self.import_csv_pushButton)

        self.file_import_tabWidget.addTab(self.import_csv_tab, "")
        self.import_excel_tab = QWidget()
        self.import_excel_tab.setObjectName(u"import_excel_tab")
        self.verticalLayout_8 = QVBoxLayout(self.import_excel_tab)
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
        self.import_excel_pushButton.setAutoDefault(True)
        self.import_excel_pushButton.setFlat(False)

        self.verticalLayout_8.addWidget(self.import_excel_pushButton)

        self.file_import_tabWidget.addTab(self.import_excel_tab, "")

        self.file_preview_horizontalLayout.addWidget(self.file_import_tabWidget)


        self.horizontalLayout_7.addLayout(self.file_preview_horizontalLayout)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")

        self.horizontalLayout_7.addLayout(self.verticalLayout_6)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_12.addLayout(self.verticalLayout_7)

        self.tabWidget_main.addTab(self.tab_import, "")
        self.tab_triage = QWidget()
        self.tab_triage.setObjectName(u"tab_triage")
        self.verticalLayout_5 = QVBoxLayout(self.tab_triage)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.tab_triage)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.horizontalLayout_filter = QHBoxLayout()
        self.horizontalLayout_filter.setObjectName(u"horizontalLayout_filter")
        self.label_filter = QLabel(self.tab_triage)
        self.label_filter.setObjectName(u"label_filter")

        self.horizontalLayout_filter.addWidget(self.label_filter)

        self.lineEdit_filter = QLineEdit(self.tab_triage)
        self.lineEdit_filter.setObjectName(u"lineEdit_filter")

        self.horizontalLayout_filter.addWidget(self.lineEdit_filter)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_filter.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout_filter)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_numeric = QVBoxLayout()
#ifndef Q_OS_MAC
        self.verticalLayout_numeric.setSpacing(-1)
#endif
        self.verticalLayout_numeric.setObjectName(u"verticalLayout_numeric")
        self.verticalLayout_numeric.setContentsMargins(0, -1, -1, 0)
        self.label_numeric = QLabel(self.tab_triage)
        self.label_numeric.setObjectName(u"label_numeric")
        self.label_numeric.setAlignment(Qt.AlignCenter)

        self.verticalLayout_numeric.addWidget(self.label_numeric)

        self.listWidget_numeric = QListWidget(self.tab_triage)
        self.listWidget_numeric.setObjectName(u"listWidget_numeric")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.listWidget_numeric.sizePolicy().hasHeightForWidth())
        self.listWidget_numeric.setSizePolicy(sizePolicy7)
        self.listWidget_numeric.setMinimumSize(QSize(296, 202))
        self.listWidget_numeric.setStyleSheet(u"background-color: rgb(196, 242, 196);")
        self.listWidget_numeric.setSelectionMode(QAbstractItemView.MultiSelection)

        self.verticalLayout_numeric.addWidget(self.listWidget_numeric)

        self.pushButton_copytostring = QPushButton(self.tab_triage)
        self.pushButton_copytostring.setObjectName(u"pushButton_copytostring")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.pushButton_copytostring.sizePolicy().hasHeightForWidth())
        self.pushButton_copytostring.setSizePolicy(sizePolicy8)
        self.pushButton_copytostring.setAutoDefault(False)
        self.pushButton_copytostring.setFlat(False)

        self.verticalLayout_numeric.addWidget(self.pushButton_copytostring)


        self.horizontalLayout_4.addLayout(self.verticalLayout_numeric)

        self.pushButton_add2script = QPushButton(self.tab_triage)
        self.pushButton_add2script.setObjectName(u"pushButton_add2script")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.pushButton_add2script.sizePolicy().hasHeightForWidth())
        self.pushButton_add2script.setSizePolicy(sizePolicy9)
        self.pushButton_add2script.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(11)
        self.pushButton_add2script.setFont(font)
        self.pushButton_add2script.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_add2script.setAutoFillBackground(False)

        self.horizontalLayout_4.addWidget(self.pushButton_add2script)

        self.verticalLayout_string = QVBoxLayout()
        self.verticalLayout_string.setObjectName(u"verticalLayout_string")
        self.label_string = QLabel(self.tab_triage)
        self.label_string.setObjectName(u"label_string")
        self.label_string.setAlignment(Qt.AlignCenter)

        self.verticalLayout_string.addWidget(self.label_string)

        self.listWidget_string = QListWidget(self.tab_triage)
        self.listWidget_string.setObjectName(u"listWidget_string")
        self.listWidget_string.setMinimumSize(QSize(296, 202))
        self.listWidget_string.setStyleSheet(u"background-color: rgb(198, 244, 198);")
        self.listWidget_string.setFrameShape(QFrame.StyledPanel)

        self.verticalLayout_string.addWidget(self.listWidget_string)

        self.pushButton_convertonumeric = QPushButton(self.tab_triage)
        self.pushButton_convertonumeric.setObjectName(u"pushButton_convertonumeric")

        self.verticalLayout_string.addWidget(self.pushButton_convertonumeric)


        self.horizontalLayout_4.addLayout(self.verticalLayout_string)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.pushButton_ignore = QPushButton(self.tab_triage)
        self.pushButton_ignore.setObjectName(u"pushButton_ignore")
        self.pushButton_ignore.setAutoFillBackground(False)
        self.pushButton_ignore.setFlat(False)

        self.verticalLayout_2.addWidget(self.pushButton_ignore)

        self.pushButton_unignore = QPushButton(self.tab_triage)
        self.pushButton_unignore.setObjectName(u"pushButton_unignore")

        self.verticalLayout_2.addWidget(self.pushButton_unignore)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalLayout_ignore = QVBoxLayout()
        self.verticalLayout_ignore.setObjectName(u"verticalLayout_ignore")
        self.label_ignore = QLabel(self.tab_triage)
        self.label_ignore.setObjectName(u"label_ignore")
        self.label_ignore.setEnabled(True)
        self.label_ignore.setAlignment(Qt.AlignCenter)

        self.verticalLayout_ignore.addWidget(self.label_ignore)

        self.listWidget_ignore = QListWidget(self.tab_triage)
        self.listWidget_ignore.setObjectName(u"listWidget_ignore")
        self.listWidget_ignore.setStyleSheet(u"background-color: rgb(253, 223, 223);")

        self.verticalLayout_ignore.addWidget(self.listWidget_ignore)


        self.horizontalLayout_4.addLayout(self.verticalLayout_ignore)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.tabWidget_preview = QTabWidget(self.tab_triage)
        self.tabWidget_preview.setObjectName(u"tabWidget_preview")
        self.tabWidget_preview.setCursor(QCursor(Qt.ArrowCursor))
        self.tabWidget_preview.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget_preview.setDocumentMode(True)
        self.tabWidget_preview.setTabsClosable(False)
        self.tab_text = QWidget()
        self.tab_text.setObjectName(u"tab_text")
        self.horizontalLayout = QHBoxLayout(self.tab_text)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.textBrowser_preview = QTextBrowser(self.tab_text)
        self.textBrowser_preview.setObjectName(u"textBrowser_preview")

        self.horizontalLayout.addWidget(self.textBrowser_preview)

        self.tabWidget_preview.addTab(self.tab_text, "")
        self.tab_graphic = QWidget()
        self.tab_graphic.setObjectName(u"tab_graphic")
        self.horizontalLayout_5 = QHBoxLayout(self.tab_graphic)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.graphicsView = QGraphicsView(self.tab_graphic)
        self.graphicsView.setObjectName(u"graphicsView")

        self.horizontalLayout_5.addWidget(self.graphicsView)

        self.tabWidget_preview.addTab(self.tab_graphic, "")
        self.tab_script = QWidget()
        self.tab_script.setObjectName(u"tab_script")
        self.horizontalLayout_6 = QHBoxLayout(self.tab_script)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.textEdit_script = QTextEdit(self.tab_script)
        self.textEdit_script.setObjectName(u"textEdit_script")

        self.horizontalLayout_6.addWidget(self.textEdit_script)

        self.tabWidget_preview.addTab(self.tab_script, "")

        self.verticalLayout_5.addWidget(self.tabWidget_preview)

        self.tabWidget_main.addTab(self.tab_triage, "")
        self.tab_plot = QWidget()
        self.tab_plot.setObjectName(u"tab_plot")
        self.tab_plot.setEnabled(False)
        self.tabWidget_main.addTab(self.tab_plot, "")
        self.tab_export = QWidget()
        self.tab_export.setObjectName(u"tab_export")
        self.tab_export.setEnabled(False)
        self.tabWidget_main.addTab(self.tab_export, "")

        self.verticalLayout_4.addWidget(self.tabWidget_main)

        self.status_label = QLabel(self.centralwidget)
        self.status_label.setObjectName(u"status_label")

        self.verticalLayout_4.addWidget(self.status_label)

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

        self.tabWidget_main.setCurrentIndex(0)
        self.file_import_tabWidget.setCurrentIndex(1)
        self.import_excel_pushButton.setDefault(False)
        self.tabWidget_preview.setCurrentIndex(0)


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
        self.import_excel_header_lineEdit.setText(QCoreApplication.translate("ColliderScopeUI", u"None", None))
        self.import_excel_pushButton.setText(QCoreApplication.translate("ColliderScopeUI", u"Import", None))
        self.file_import_tabWidget.setTabText(self.file_import_tabWidget.indexOf(self.import_excel_tab), QCoreApplication.translate("ColliderScopeUI", u"Excel", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tab_import), QCoreApplication.translate("ColliderScopeUI", u"Import", None))
        self.label.setText(QCoreApplication.translate("ColliderScopeUI", u"Data Preview and Triage", None))
        self.label_filter.setText(QCoreApplication.translate("ColliderScopeUI", u"Filter", None))
        self.label_numeric.setText(QCoreApplication.translate("ColliderScopeUI", u"Numeric (Plot Sources)", None))
        self.pushButton_copytostring.setText(QCoreApplication.translate("ColliderScopeUI", u"Copy to String (update Script)", None))
        self.pushButton_add2script.setText(QCoreApplication.translate("ColliderScopeUI", u"A\n"
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
        self.pushButton_convertonumeric.setText(QCoreApplication.translate("ColliderScopeUI", u"Convert to Numeric (update Script)", None))
        self.pushButton_ignore.setText(QCoreApplication.translate("ColliderScopeUI", u">>>", None))
        self.pushButton_unignore.setText(QCoreApplication.translate("ColliderScopeUI", u"<<<", None))
        self.label_ignore.setText(QCoreApplication.translate("ColliderScopeUI", u"Ignore", None))
        self.tabWidget_preview.setTabText(self.tabWidget_preview.indexOf(self.tab_text), QCoreApplication.translate("ColliderScopeUI", u"Text Preview", None))
        self.tabWidget_preview.setTabText(self.tabWidget_preview.indexOf(self.tab_graphic), QCoreApplication.translate("ColliderScopeUI", u"Graphic Preview", None))
        self.tabWidget_preview.setTabText(self.tabWidget_preview.indexOf(self.tab_script), QCoreApplication.translate("ColliderScopeUI", u"Preprocess Script", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tab_triage), QCoreApplication.translate("ColliderScopeUI", u"Data Triage", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tab_plot), QCoreApplication.translate("ColliderScopeUI", u"Plotting", None))
        self.tabWidget_main.setTabText(self.tabWidget_main.indexOf(self.tab_export), QCoreApplication.translate("ColliderScopeUI", u"Export", None))
        self.status_label.setText("")
        self.menuColliderScope2024.setTitle(QCoreApplication.translate("ColliderScopeUI", u"Menu", None))
    # retranslateUi

