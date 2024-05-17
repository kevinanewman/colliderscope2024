# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nanhandler_horizontal.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QGroupBox, QHBoxLayout,
    QRadioButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_NanHandlerHorizontal(object):
    def setupUi(self, NanHandlerHorizontal):
        if not NanHandlerHorizontal.objectName():
            NanHandlerHorizontal.setObjectName(u"NanHandlerHorizontal")
        NanHandlerHorizontal.resize(319, 103)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NanHandlerHorizontal.sizePolicy().hasHeightForWidth())
        NanHandlerHorizontal.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(NanHandlerHorizontal)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 5, 5, 5)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.column_groupBox = QGroupBox(NanHandlerHorizontal)
        self.column_groupBox.setObjectName(u"column_groupBox")
        sizePolicy.setHeightForWidth(self.column_groupBox.sizePolicy().hasHeightForWidth())
        self.column_groupBox.setSizePolicy(sizePolicy)
        self.column_groupBox.setMinimumSize(QSize(145, 93))
        self.verticalLayout_2 = QVBoxLayout(self.column_groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.column_allow_nans = QRadioButton(self.column_groupBox)
        self.col_buttonGroup = QButtonGroup(NanHandlerHorizontal)
        self.col_buttonGroup.setObjectName(u"col_buttonGroup")
        self.col_buttonGroup.addButton(self.column_allow_nans)
        self.column_allow_nans.setObjectName(u"column_allow_nans")
        self.column_allow_nans.setChecked(True)

        self.verticalLayout_3.addWidget(self.column_allow_nans)

        self.column_drop_if_all_nans_radioButton = QRadioButton(self.column_groupBox)
        self.col_buttonGroup.addButton(self.column_drop_if_all_nans_radioButton)
        self.column_drop_if_all_nans_radioButton.setObjectName(u"column_drop_if_all_nans_radioButton")

        self.verticalLayout_3.addWidget(self.column_drop_if_all_nans_radioButton)

        self.column_drop_if_any_nans_radioButton = QRadioButton(self.column_groupBox)
        self.col_buttonGroup.addButton(self.column_drop_if_any_nans_radioButton)
        self.column_drop_if_any_nans_radioButton.setObjectName(u"column_drop_if_any_nans_radioButton")

        self.verticalLayout_3.addWidget(self.column_drop_if_any_nans_radioButton)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)


        self.horizontalLayout.addWidget(self.column_groupBox)

        self.row_groupBox = QGroupBox(NanHandlerHorizontal)
        self.row_groupBox.setObjectName(u"row_groupBox")
        sizePolicy.setHeightForWidth(self.row_groupBox.sizePolicy().hasHeightForWidth())
        self.row_groupBox.setSizePolicy(sizePolicy)
        self.row_groupBox.setMinimumSize(QSize(145, 93))
        self.verticalLayout_4 = QVBoxLayout(self.row_groupBox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.row_allow_nans = QRadioButton(self.row_groupBox)
        self.row_buttonGroup = QButtonGroup(NanHandlerHorizontal)
        self.row_buttonGroup.setObjectName(u"row_buttonGroup")
        self.row_buttonGroup.addButton(self.row_allow_nans)
        self.row_allow_nans.setObjectName(u"row_allow_nans")
        self.row_allow_nans.setChecked(True)

        self.verticalLayout.addWidget(self.row_allow_nans)

        self.row_drop_if_all_nans_radioButton = QRadioButton(self.row_groupBox)
        self.row_buttonGroup.addButton(self.row_drop_if_all_nans_radioButton)
        self.row_drop_if_all_nans_radioButton.setObjectName(u"row_drop_if_all_nans_radioButton")

        self.verticalLayout.addWidget(self.row_drop_if_all_nans_radioButton)

        self.row_drop_if_any_nans_radioButton = QRadioButton(self.row_groupBox)
        self.row_buttonGroup.addButton(self.row_drop_if_any_nans_radioButton)
        self.row_drop_if_any_nans_radioButton.setObjectName(u"row_drop_if_any_nans_radioButton")

        self.verticalLayout.addWidget(self.row_drop_if_any_nans_radioButton)


        self.verticalLayout_4.addLayout(self.verticalLayout)


        self.horizontalLayout.addWidget(self.row_groupBox)


        self.verticalLayout_5.addLayout(self.horizontalLayout)


        self.retranslateUi(NanHandlerHorizontal)

        QMetaObject.connectSlotsByName(NanHandlerHorizontal)
    # setupUi

    def retranslateUi(self, NanHandlerHorizontal):
        NanHandlerHorizontal.setWindowTitle(QCoreApplication.translate("NanHandlerHorizontal", u"Form", None))
        self.column_groupBox.setTitle(QCoreApplication.translate("NanHandlerHorizontal", u"Columns", None))
        self.column_allow_nans.setText(QCoreApplication.translate("NanHandlerHorizontal", u"Allow NANs", None))
        self.column_drop_if_all_nans_radioButton.setText(QCoreApplication.translate("NanHandlerHorizontal", u"Drop if all NANs", None))
        self.column_drop_if_any_nans_radioButton.setText(QCoreApplication.translate("NanHandlerHorizontal", u"Drop if any NANs", None))
        self.row_groupBox.setTitle(QCoreApplication.translate("NanHandlerHorizontal", u"Rows", None))
        self.row_allow_nans.setText(QCoreApplication.translate("NanHandlerHorizontal", u"Allow NANs", None))
        self.row_drop_if_all_nans_radioButton.setText(QCoreApplication.translate("NanHandlerHorizontal", u"Drop if all NANs", None))
        self.row_drop_if_any_nans_radioButton.setText(QCoreApplication.translate("NanHandlerHorizontal", u"Drop if any NANs", None))
    # retranslateUi

