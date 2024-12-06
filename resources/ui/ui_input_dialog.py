# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'input_dialogHmKQet.ui'
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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import resources.resources_rc

class Ui_InputDialog(object):
    def setupUi(self, InputDialog):
        if not InputDialog.objectName():
            InputDialog.setObjectName(u"InputDialog")
        InputDialog.setWindowModality(Qt.WindowModality.ApplicationModal)
        InputDialog.resize(328, 128)
        InputDialog.setMinimumSize(QSize(328, 128))
        InputDialog.setStyleSheet(u"QToolTip {\n"
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
"QLineEdit {\n"
"    background-color: #2e2e2e;\n"
"    color: #ffffff;\n"
"    border: 1px solid #5b5e60;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: #4a90e2;\n"
"    background-color: #333333;\n"
"}")
        InputDialog.setModal(True)
        self.verticalLayout = QVBoxLayout(InputDialog)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 3, 6, 3)
        self.title_label = QLabel(InputDialog)
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

        self.frame = QFrame(InputDialog)
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
        self.horizontalLayout.setContentsMargins(9, -1, -1, -1)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/ico/Icons/ico/phils-hub.ico"))

        self.horizontalLayout.addWidget(self.label)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 9, 6, 9)
        self.msg_label = QLabel(self.frame_2)
        self.msg_label.setObjectName(u"msg_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.msg_label.sizePolicy().hasHeightForWidth())
        self.msg_label.setSizePolicy(sizePolicy2)
        self.msg_label.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.msg_label)

        self.input_field = QLineEdit(self.frame_2)
        self.input_field.setObjectName(u"input_field")

        self.verticalLayout_2.addWidget(self.input_field)


        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame)

        self.frame_4 = QFrame(InputDialog)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QFrame {\n"
"	background: transparent;\n"
"	border-bottom-left-radius: 9px;\n"
"	border-bottom-right-radius: 9px;\n"
"}")
        self.frame_4.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.submit_btn = QPushButton(self.frame_4)
        self.submit_btn.setObjectName(u"submit_btn")
        self.submit_btn.setMinimumSize(QSize(0, 0))
        self.submit_btn.setStyleSheet(u"QPushButton {\n"
"	border-bottom-right-radius: 0px;\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 0px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.submit_btn)

        self.cancel_btn = QPushButton(self.frame_4)
        self.cancel_btn.setObjectName(u"cancel_btn")
        self.cancel_btn.setMinimumSize(QSize(0, 0))
        self.cancel_btn.setStyleSheet(u"QPushButton {\n"
"	border-bottom-left-radius: 0px;\n"
"	border-top-left-radius: 0px;\n"
"	border-top-right-radius: 0px;\n"
"}")

        self.horizontalLayout_3.addWidget(self.cancel_btn)


        self.verticalLayout.addWidget(self.frame_4)


        self.retranslateUi(InputDialog)

        QMetaObject.connectSlotsByName(InputDialog)
    # setupUi

    def retranslateUi(self, InputDialog):
        InputDialog.setWindowTitle(QCoreApplication.translate("InputDialog", u"Input Dialog", None))
        self.title_label.setText(QCoreApplication.translate("InputDialog", u"TextLabel", None))
        self.label.setText("")
        self.msg_label.setText(QCoreApplication.translate("InputDialog", u"Input Dialog...", None))
        self.submit_btn.setText(QCoreApplication.translate("InputDialog", u"SUBMIT", None))
        self.cancel_btn.setText(QCoreApplication.translate("InputDialog", u"CANCEL", None))
    # retranslateUi

