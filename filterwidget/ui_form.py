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
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLineEdit,
    QSizePolicy, QToolButton, QWidget)

class Ui_FilterWidget(object):
    def setupUi(self, FilterWidget):
        if not FilterWidget.objectName():
            FilterWidget.setObjectName(u"FilterWidget")
        FilterWidget.resize(401, 36)
        self.horizontalLayout = QHBoxLayout(FilterWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.toolButton = QToolButton(FilterWidget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setCheckable(True)
        self.toolButton.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout.addWidget(self.toolButton)

        self.comboBox = QComboBox(FilterWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMaximumSize(QSize(106, 16777215))
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.comboBox.setFrame(True)

        self.horizontalLayout.addWidget(self.comboBox)

        self.lineEdit = QLineEdit(FilterWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)

        self.toolButton_2 = QToolButton(FilterWidget)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setAutoFillBackground(False)
        icon = QIcon()
        icon.addFile(u"assets/matchCaseHovered.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u"assets/matchCaseSelected.svg", QSize(), QIcon.Active, QIcon.On)
        self.toolButton_2.setIcon(icon)
        self.toolButton_2.setCheckable(True)
        self.toolButton_2.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.horizontalLayout.addWidget(self.toolButton_2)

        self.toolButton_3 = QToolButton(FilterWidget)
        self.toolButton_3.setObjectName(u"toolButton_3")
        icon1 = QIcon()
        icon1.addFile(u"assets/words.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u"assets/wordsSelected.svg", QSize(), QIcon.Active, QIcon.On)
        self.toolButton_3.setIcon(icon1)
        self.toolButton_3.setCheckable(True)
        self.toolButton_3.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.horizontalLayout.addWidget(self.toolButton_3)


        self.retranslateUi(FilterWidget)

        QMetaObject.connectSlotsByName(FilterWidget)
    # setupUi

    def retranslateUi(self, FilterWidget):
        FilterWidget.setWindowTitle(QCoreApplication.translate("FilterWidget", u"FilterWidget", None))
        self.toolButton.setText(QCoreApplication.translate("FilterWidget", u"not", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("FilterWidget", u"contains", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("FilterWidget", u"starts with", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("FilterWidget", u"ends with", None))

        self.lineEdit.setPlaceholderText(QCoreApplication.translate("FilterWidget", u"filter", None))
        self.toolButton_2.setText(QCoreApplication.translate("FilterWidget", u"Match Case", None))
        self.toolButton_3.setText(QCoreApplication.translate("FilterWidget", u"Whole Words", None))
    # retranslateUi

