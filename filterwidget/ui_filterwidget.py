# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'filterwidget.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QToolButton, QWidget)

class Ui_FilterWidget(object):
    def setupUi(self, FilterWidget):
        if not FilterWidget.objectName():
            FilterWidget.setObjectName(u"FilterWidget")
        FilterWidget.resize(301, 38)
        FilterWidget.setMaximumSize(QSize(16777215, 38))
        self.horizontalLayout_3 = QHBoxLayout(FilterWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(FilterWidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMaximumSize(QSize(16777215, 25))
        self.filter_page = QWidget()
        self.filter_page.setObjectName(u"filter_page")
        self.horizontalLayout_2 = QHBoxLayout(self.filter_page)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 0, 5, 0)
        self.not_pushButton = QPushButton(self.filter_page)
        self.not_pushButton.setObjectName(u"not_pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.not_pushButton.sizePolicy().hasHeightForWidth())
        self.not_pushButton.setSizePolicy(sizePolicy)
        self.not_pushButton.setMinimumSize(QSize(20, 0))
        self.not_pushButton.setMaximumSize(QSize(30, 25))
        self.not_pushButton.setCheckable(True)
        self.not_pushButton.setChecked(False)
        self.not_pushButton.setAutoDefault(True)
        self.not_pushButton.setFlat(True)

        self.horizontalLayout_2.addWidget(self.not_pushButton)

        self.lineEdit = QLineEdit(self.filter_page)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.settings_toolButton = QToolButton(self.filter_page)
        self.settings_toolButton.setObjectName(u"settings_toolButton")

        self.horizontalLayout_2.addWidget(self.settings_toolButton)

        self.stackedWidget.addWidget(self.filter_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.settings_page.setMaximumSize(QSize(16777215, 25))
        self.horizontalLayout_4 = QHBoxLayout(self.settings_page)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.comboBox = QComboBox(self.settings_page)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMaximumSize(QSize(106, 20))
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.comboBox.setFrame(True)

        self.horizontalLayout.addWidget(self.comboBox)

        self.cc_pushButton = QPushButton(self.settings_page)
        self.cc_pushButton.setObjectName(u"cc_pushButton")
        sizePolicy.setHeightForWidth(self.cc_pushButton.sizePolicy().hasHeightForWidth())
        self.cc_pushButton.setSizePolicy(sizePolicy)
        self.cc_pushButton.setAutoFillBackground(False)
        icon = QIcon()
        icon.addFile(u"assets/matchCaseHovered.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u"assets/matchCaseSelected.svg", QSize(), QIcon.Active, QIcon.On)
        self.cc_pushButton.setIcon(icon)
        self.cc_pushButton.setCheckable(True)
        self.cc_pushButton.setFlat(True)

        self.horizontalLayout.addWidget(self.cc_pushButton)

        self.w_pushButton = QPushButton(self.settings_page)
        self.w_pushButton.setObjectName(u"w_pushButton")
        sizePolicy.setHeightForWidth(self.w_pushButton.sizePolicy().hasHeightForWidth())
        self.w_pushButton.setSizePolicy(sizePolicy)
        icon1 = QIcon()
        icon1.addFile(u"assets/words.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u"assets/wordsSelected.svg", QSize(), QIcon.Active, QIcon.On)
        self.w_pushButton.setIcon(icon1)
        self.w_pushButton.setCheckable(True)
        self.w_pushButton.setFlat(True)

        self.horizontalLayout.addWidget(self.w_pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.back_toolButton = QToolButton(self.settings_page)
        self.back_toolButton.setObjectName(u"back_toolButton")
        icon2 = QIcon(QIcon.fromTheme(u"applications-engineering"))
        self.back_toolButton.setIcon(icon2)

        self.horizontalLayout.addWidget(self.back_toolButton)


        self.horizontalLayout_4.addLayout(self.horizontalLayout)

        self.stackedWidget.addWidget(self.settings_page)

        self.horizontalLayout_3.addWidget(self.stackedWidget)


        self.retranslateUi(FilterWidget)
        self.lineEdit.textChanged.connect(FilterWidget.inputChanged)
        self.settings_toolButton.clicked.connect(FilterWidget.goto_settings)
        self.back_toolButton.clicked.connect(FilterWidget.goto_filter)
        self.not_pushButton.clicked.connect(FilterWidget.inputChanged)
        self.cc_pushButton.clicked.connect(FilterWidget.inputChanged)
        self.w_pushButton.clicked.connect(FilterWidget.inputChanged)
        self.comboBox.currentTextChanged.connect(FilterWidget.inputChanged)

        self.stackedWidget.setCurrentIndex(0)
        self.not_pushButton.setDefault(True)


        QMetaObject.connectSlotsByName(FilterWidget)
    # setupUi

    def retranslateUi(self, FilterWidget):
        FilterWidget.setWindowTitle(QCoreApplication.translate("FilterWidget", u"FilterWidget", None))
        self.not_pushButton.setText(QCoreApplication.translate("FilterWidget", u"not", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("FilterWidget", u"filter", None))
        self.settings_toolButton.setText(QCoreApplication.translate("FilterWidget", u"...", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("FilterWidget", u"contains", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("FilterWidget", u"starts with", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("FilterWidget", u"ends with", None))

        self.cc_pushButton.setText("")
        self.w_pushButton.setText("")
        self.back_toolButton.setText(QCoreApplication.translate("FilterWidget", u"<", None))
    # retranslateUi

