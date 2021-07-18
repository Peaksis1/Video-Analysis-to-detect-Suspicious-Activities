# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ForgotPasswordSrLvVn.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *



def setupUi(self, Dialog):
    if Dialog.objectName():
        Dialog.setObjectName(u"Dialog")
    Dialog.resize(503, 394)
    Dialog.setFocusPolicy(Qt.StrongFocus)
    Dialog.setStyleSheet(u"	background-color: rgb(56, 58, 89);\n"
"	color: rgb(59, 61, 157);\n"
"   	border-radius:10px;\n"
"")
    self.frame = QFrame(Dialog)
    self.frame.setObjectName(u"frame")
    self.frame.setGeometry(QRect(20, 19, 461, 301))
    self.frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(166, 144, 255);\n"
"	color: rgb(96, 98, 189);\n"
"	border-radius:10px;\n"
"}\n"
"")
    self.frame.setFrameShape(QFrame.StyledPanel)
    self.frame.setFrameShadow(QFrame.Raised)
    self.LabelNewPwd = QLabel(self.frame)
    self.LabelNewPwd.setObjectName(u"LabelNewPwd")
    self.LabelNewPwd.setGeometry(QRect(38, 195, 111, 41))
    font = QFont()
    font.setFamily(u"Segoe UI")
    font.setPointSize(11)
    self.LabelNewPwd.setFont(font)
    self.LabelNewPwd.setStyleSheet(u"color: rgb(56, 58, 89);\n"
"background:transparent;")
    self.LabelNewPwd.setAlignment(Qt.AlignCenter)
    self.LabelConfPwd = QLabel(self.frame)
    self.LabelConfPwd.setObjectName(u"LabelConfPwd")
    self.LabelConfPwd.setGeometry(QRect(33, 235, 131, 41))
    self.LabelConfPwd.setFont(font)
    self.LabelConfPwd.setStyleSheet(u"color: rgb(56, 58, 89);\n"
"background:transparent;")
    self.LabelConfPwd.setAlignment(Qt.AlignCenter)
    self.ConfirmPwd = QLineEdit(self.frame)
    self.ConfirmPwd.setObjectName(u"ConfirmPwd")
    self.ConfirmPwd.setGeometry(QRect(173, 245, 244, 23))
    font1 = QFont()
    font1.setFamily(u"Segoe UI")
    font1.setPointSize(12)
    self.ConfirmPwd.setFont(font1)
    self.ConfirmPwd.setFocusPolicy(Qt.StrongFocus)
    self.ConfirmPwd.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 255, 255);")
    self.ConfirmPwd.setMaxLength(8)
    self.ConfirmPwd.setEchoMode(QLineEdit.Password)
    self.ConfirmPwd.setAlignment(Qt.AlignCenter)
    self.ConfirmPwd.setClearButtonEnabled(True)
    self.NewPassword = QLineEdit(self.frame)
    self.NewPassword.setObjectName(u"NewPassword")
    self.NewPassword.setGeometry(QRect(173, 205, 244, 23))
    self.NewPassword.setFont(font1)
    self.NewPassword.setFocusPolicy(Qt.StrongFocus)
    self.NewPassword.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 255, 255);")
    self.NewPassword.setMaxLength(8)
    self.NewPassword.setEchoMode(QLineEdit.Password)
    self.NewPassword.setAlignment(Qt.AlignCenter)
    self.NewPassword.setClearButtonEnabled(True)
    self.VerifyCode = QLineEdit(self.frame)
    self.VerifyCode.setObjectName(u"VerifyCode")
    self.VerifyCode.setGeometry(QRect(178, 165, 244, 23))
    self.VerifyCode.setFont(font1)
    self.VerifyCode.setFocusPolicy(Qt.StrongFocus)
    self.VerifyCode.setAutoFillBackground(False)
    self.VerifyCode.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 255, 255);")
    self.VerifyCode.setAlignment(Qt.AlignCenter)
    self.VerifyCode.setClearButtonEnabled(True)
    self.EnterCode = QLabel(self.frame)
    self.EnterCode.setObjectName(u"EnterCode")
    self.EnterCode.setGeometry(QRect(38, 155, 121, 31))
    self.EnterCode.setFont(font)
    self.EnterCode.setStyleSheet(u"color: rgb(56, 58, 89);\n"
"background:transparent;")
    self.EnterCode.setAlignment(Qt.AlignCenter)
    self.Status = QLabel(self.frame)
    self.Status.setObjectName(u"Status")
    self.Status.setGeometry(QRect(60, 90, 341, 71))
    font2 = QFont()
    font2.setFamily(u"Segoe UI")
    font2.setPointSize(11)
    font2.setBold(True)
    font2.setWeight(75)
    font2.setKerning(True)
    self.Status.setFont(font2)
    self.Status.setStyleSheet(u"color: rgb(202, 5, 31);\n"
"background:transparent;")
    self.Status.setAlignment(Qt.AlignCenter)
    self.Status.setWordWrap(True)
    self.EmailId = QLineEdit(self.frame)
    self.EmailId.setObjectName(u"EmailId")
    self.EmailId.setGeometry(QRect(170, 20, 244, 23))
    self.EmailId.setFont(font1)
    self.EmailId.setFocusPolicy(Qt.StrongFocus)
    self.EmailId.setStyleSheet(u"border-radius:10px;\n"
"background-color: rgb(255, 255, 255);")
    self.EmailId.setMaxLength(8)
    self.EmailId.setEchoMode(QLineEdit.Normal)
    self.EmailId.setAlignment(Qt.AlignCenter)
    self.EmailId.setClearButtonEnabled(True)
    self.LabelEmail = QLabel(self.frame)
    self.LabelEmail.setObjectName(u"LabelEmail")
    self.LabelEmail.setGeometry(QRect(30, 13, 111, 41))
    self.LabelEmail.setFont(font)
    self.LabelEmail.setStyleSheet(u"color: rgb(56, 58, 89);\n"
"background:transparent;")
    self.LabelEmail.setAlignment(Qt.AlignCenter)
    self.send = QPushButton(self.frame)
    self.send.setObjectName(u"send")
    self.send.setGeometry(QRect(200, 60, 71, 31))
    font3 = QFont()
    font3.setFamily(u"Segoe UI")
    font3.setPointSize(12)
    font3.setBold(False)
    font3.setItalic(False)
    font3.setWeight(9)
    self.send.setFont(font3)
    self.send.setCursor(QCursor(Qt.PointingHandCursor))
    self.send.setMouseTracking(True)
    self.send.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"	background-color: rgb(56,58,89);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 12pt \"Segoe UI\";\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	color:  rgb(13,13,13);\n"
"	background-color: rgb(255, 171, 215);\n"
"	font: 90 12pt \"Segoe UI\";\n"
"}")
    self.Ok = QPushButton(Dialog)
    self.Ok.setObjectName(u"Ok")
    self.Ok.setGeometry(QRect(170, 350, 71, 31))
    self.Ok.setFont(font3)
    self.Ok.setCursor(QCursor(Qt.PointingHandCursor))
    self.Ok.setMouseTracking(True)
    self.Ok.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"	background-color: rgb(255, 171, 215);\n"
"	color: rgb(13,13,13);\n"
"	font: 75 12pt \"Segoe UI\";\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	color:  rgb(255, 255, 255);\n"
"	background-color: rgb(166, 144, 255);\n"
"	font: 90 12pt \"Segoe UI\";\n"
"}")
    self.Cancel = QPushButton(Dialog)
    self.Cancel.setObjectName(u"Cancel")
    self.Cancel.setGeometry(QRect(260, 350, 71, 31))
    self.Cancel.setFont(font3)
    self.Cancel.setCursor(QCursor(Qt.PointingHandCursor))
    self.Cancel.setMouseTracking(True)
    self.Cancel.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"	background-color: rgb(255, 171, 215);\n"
"	color: rgb(13,13,13);\n"
"	font: 75 12pt \"Segoe UI\";\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	color:  rgb(255, 255, 255);\n"
"	background-color: rgb(166, 144, 255);\n"
"	font: 90 12pt \"Segoe UI\";\n"
"}")

    self.retranslateUi(Dialog)

    QMetaObject.connectSlotsByName(Dialog)
# setupUi

def retranslateUi(self, Dialog):
    Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
    self.LabelNewPwd.setText(QCoreApplication.translate("Dialog", u"New Password", None))
    self.LabelConfPwd.setText(QCoreApplication.translate("Dialog", u"Confirm Password", None))
    self.ConfirmPwd.setText("")
    self.ConfirmPwd.setPlaceholderText(QCoreApplication.translate("Dialog", u"Confirm Password", None))
    self.NewPassword.setText("")
    self.NewPassword.setPlaceholderText(QCoreApplication.translate("Dialog", u"Password", None))
    self.VerifyCode.setText("")
    self.VerifyCode.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter Code", None))
    self.EnterCode.setText(QCoreApplication.translate("Dialog", u"Verification Code", None))
    self.Status.setText(QCoreApplication.translate("Dialog", u"Verification Code will be sent to your registered Email address", None))
    self.EmailId.setText("")
    self.EmailId.setPlaceholderText(QCoreApplication.translate("Dialog", u"Email-id", None))
    self.LabelEmail.setText(QCoreApplication.translate("Dialog", u"Email ID", None))
    self.send.setText(QCoreApplication.translate("Dialog", u"Send", None))
    self.Ok.setText(QCoreApplication.translate("Dialog", u"Submit", None))
    self.Cancel.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
# retranslateUi

