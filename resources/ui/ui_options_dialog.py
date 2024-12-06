# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'options_dialogGNLbCX.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QPushButton, QRadioButton, QSizePolicy,
    QVBoxLayout, QWidget)
import resources.resources_rc

class Ui_OptionsDialog(object):
    def setupUi(self, OptionsDialog):
        if not OptionsDialog.objectName():
            OptionsDialog.setObjectName(u"OptionsDialog")
        OptionsDialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        OptionsDialog.resize(328, 128)
        OptionsDialog.setMinimumSize(QSize(328, 128))
        OptionsDialog.setStyleSheet(u"QToolTip {\n"
"    background-color: #2e2e2e;\n"
"    color: #ffffff;\n"
"    border: 1px solid #5b5e60;\n"
"    padding: 4px;\n"
"    border-radius: 4px;\n"
"    opacity: 200;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #ffffff;\n"
"}\n"
"\n"
"QFrame {\n"
"    background-color: #2e2e2e;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #3c3f41;\n"
"    color: #ffffff;\n"
"    border: 1px solid #5b5e60;\n"
"    border-radius: 4px;\n"
"	padding: 0px 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-color: #4a90e2;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3d78b2;\n"
"    border-color: #2a5f92;\n"
"}\n"
"\n"
"QRadioButton {\n"
"    color: #ffffff;\n"
"    spacing: 5px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 12px;\n"
"    height: 12px;\n"
"    background-color: #2e2e2e;\n"
"    border: 1px solid #5b5e60;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover {\n"
"    background-color: #4a90e2;\n"
"    border-color: #3d78b2;\n"
""
                        "}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #4a90e2;\n"
"    border-color: #3d78b2;\n"
"}\n"
"\n"
"QRadioButton::indicator:pressed {\n"
"    background-color: #3d78b2;\n"
"    border-color: #2a5f92;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:pressed {\n"
"    background-color: #3d78b2;\n"
"    border-color: #2a5f92;\n"
"}")
        OptionsDialog.setModal(True)
        self.verticalLayout = QVBoxLayout(OptionsDialog)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 3, 6, 3)
        self.title_label = QLabel(OptionsDialog)
        self.title_label.setObjectName(u"title_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_label.sizePolicy().hasHeightForWidth())
        self.title_label.setSizePolicy(sizePolicy)
        self.title_label.setMinimumSize(QSize(0, 18))
        self.title_label.setStyleSheet(u"QLabel {\n"
"	background-color: #3c3f41;\n"
"	border-top-left-radius: 4px;\n"
"	border-top-right-radius: 4px;\n"
"	padding-left: 5px;\n"
"}")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.frame = QFrame(OptionsDialog)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 6, -1, 6)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/ico/Icons/ico/phils-hub.ico"))

        self.horizontalLayout.addWidget(self.label)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 0, 0, 0)
        self.msg_label = QLabel(self.frame_3)
        self.msg_label.setObjectName(u"msg_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.msg_label.sizePolicy().hasHeightForWidth())
        self.msg_label.setSizePolicy(sizePolicy3)
        self.msg_label.setMaximumSize(QSize(16777215, 16))
        self.msg_label.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.msg_label)

        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QFrame {\n"
"	background: transparent;\n"
"	border-bottom-left-radius: 9px;\n"
"	border-bottom-right-radius: 9px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.option1 = QRadioButton(self.frame_2)
        self.option1.setObjectName(u"option1")
        self.option1.setChecked(True)

        self.verticalLayout_2.addWidget(self.option1)

        self.option2 = QRadioButton(self.frame_2)
        self.option2.setObjectName(u"option2")

        self.verticalLayout_2.addWidget(self.option2)

        self.option3 = QRadioButton(self.frame_2)
        self.option3.setObjectName(u"option3")
        self.option3.setChecked(False)

        self.verticalLayout_2.addWidget(self.option3)


        self.verticalLayout_3.addWidget(self.frame_2, 0, Qt.AlignmentFlag.AlignVCenter)


        self.horizontalLayout.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)

        self.submit_btn = QPushButton(OptionsDialog)
        self.submit_btn.setObjectName(u"submit_btn")
        self.submit_btn.setMinimumSize(QSize(0, 0))
        self.submit_btn.setStyleSheet(u"QPushButton {\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 0px;\n"
"}")

        self.verticalLayout.addWidget(self.submit_btn)


        self.retranslateUi(OptionsDialog)

        QMetaObject.connectSlotsByName(OptionsDialog)
    # setupUi

    def retranslateUi(self, OptionsDialog):
        OptionsDialog.setWindowTitle(QCoreApplication.translate("OptionsDialog", u"Options Dialog", None))
        self.title_label.setText(QCoreApplication.translate("OptionsDialog", u"TextLabel", None))
        self.label.setText("")
        self.msg_label.setText(QCoreApplication.translate("OptionsDialog", u"Options Dialog...", None))
        self.option1.setText(QCoreApplication.translate("OptionsDialog", u"RadioButton", None))
        self.option2.setText(QCoreApplication.translate("OptionsDialog", u"RadioButton", None))
        self.option3.setText(QCoreApplication.translate("OptionsDialog", u"RadioButton", None))
        self.submit_btn.setText(QCoreApplication.translate("OptionsDialog", u"Submit", None))
    # retranslateUi

