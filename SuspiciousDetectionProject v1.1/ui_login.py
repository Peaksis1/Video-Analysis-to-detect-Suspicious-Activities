# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginZMSVyQ.ui'
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(917, 585)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setEnabled(True)
        self.frame_main.setMinimumSize(QSize(0, 567))
        self.frame_main.setMaximumSize(QSize(16777215, 16777215))
        self.frame_main.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(56, 58, 89);\n"
"	color: rgb(59, 61, 157);\n"
"   	border-radius:10px;\n"
"}")
        self.frame_main.setFrameShape(QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.frame_main)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(-20, 0, 551, 181))
        self.label_title.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"\n"
"color: rgb(254, 121,199);\n"
"color: rgb(213, 217, 240);")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_title.setWordWrap(True)
        self.frame_Login = QFrame(self.frame_main)
        self.frame_Login.setObjectName(u"frame_Login")
        self.frame_Login.setGeometry(QRect(510, 20, 371, 531))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.frame_Login.setFont(font1)
        self.frame_Login.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_Login.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(166, 144, 255);\n"
"	color: rgb(96, 98, 189);\n"
"	border-radius:10px;\n"
"}\n"
"")
        self.frame_Login.setFrameShape(QFrame.StyledPanel)
        self.frame_Login.setFrameShadow(QFrame.Raised)
        self.label_LOGIN = QLabel(self.frame_Login)
        self.label_LOGIN.setObjectName(u"label_LOGIN")
        self.label_LOGIN.setGeometry(QRect(90, 130, 201, 41))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_LOGIN.setFont(font2)
        self.label_LOGIN.setStyleSheet(u"color: rgb(56, 58, 89);\n"
"background:transparent;")
        self.label_LOGIN.setAlignment(Qt.AlignCenter)
        self.formGroupBox = QGroupBox(self.frame_Login)
        self.formGroupBox.setObjectName(u"formGroupBox")
        self.formGroupBox.setGeometry(QRect(10, 180, 351, 141))
        self.Login_form = QFormLayout(self.formGroupBox)
        self.Login_form.setObjectName(u"Login_form")
        self.Login_form.setHorizontalSpacing(10)
        self.Login_form.setVerticalSpacing(10)
        self.Login_form.setContentsMargins(5, 30, 5, 1)
        self.label_id = QLabel(self.formGroupBox)
        self.label_id.setObjectName(u"label_id")
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_id.setFont(font3)
        self.label_id.setStyleSheet(u"color: rgb(56, 58, 89);\n"
"background: transparent;")
        self.label_id.setAlignment(Qt.AlignCenter)

        self.Login_form.setWidget(0, QFormLayout.LabelRole, self.label_id)

        self.lineEdit_id = QLineEdit(self.formGroupBox)
        self.lineEdit_id.setObjectName(u"lineEdit_id")
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(12)
        self.lineEdit_id.setFont(font4)
        self.lineEdit_id.setAutoFillBackground(False)
        self.lineEdit_id.setStyleSheet(u"border-radius:10px;")
        self.lineEdit_id.setAlignment(Qt.AlignCenter)
        self.lineEdit_id.setClearButtonEnabled(True)

        self.Login_form.setWidget(0, QFormLayout.FieldRole, self.lineEdit_id)

        self.label_pwd = QLabel(self.formGroupBox)
        self.label_pwd.setObjectName(u"label_pwd")
        self.label_pwd.setFont(font3)
        self.label_pwd.setStyleSheet(u"color: rgb(56, 58, 89);")
        self.label_pwd.setAlignment(Qt.AlignCenter)

        self.Login_form.setWidget(1, QFormLayout.LabelRole, self.label_pwd)

        self.lineEdit_pwd = QLineEdit(self.formGroupBox)
        self.lineEdit_pwd.setObjectName(u"lineEdit_pwd")
        self.lineEdit_pwd.setFont(font4)
        self.lineEdit_pwd.setStyleSheet(u"border-radius:10px;")
        self.lineEdit_pwd.setMaxLength(8)
        self.lineEdit_pwd.setEchoMode(QLineEdit.Password)
        self.lineEdit_pwd.setAlignment(Qt.AlignCenter)
        self.lineEdit_pwd.setClearButtonEnabled(True)

        self.Login_form.setWidget(1, QFormLayout.FieldRole, self.lineEdit_pwd)

        self.signup_Button = QPushButton(self.frame_Login)
        self.signup_Button.setObjectName(u"signup_Button")
        self.signup_Button.setGeometry(QRect(200, 434, 71, 31))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(12)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(9)
        self.signup_Button.setFont(font5)
        self.signup_Button.setCursor(QCursor(Qt.PointingHandCursor))
        self.signup_Button.setMouseTracking(True)
        self.signup_Button.setFocusPolicy(Qt.StrongFocus)
        self.signup_Button.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"	background-color: rgb(56, 58, 87);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 12pt \"Segoe UI\";\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(13, 13, 13);\n"
"	background-color: rgb(255, 171, 215);\n"
"	font: 90 12pt \"Segoe UI\";\n"
"}")
        self.label_newuser = QLabel(self.frame_Login)
        self.label_newuser.setObjectName(u"label_newuser")
        self.label_newuser.setGeometry(QRect(110, 434, 91, 25))
        self.label_newuser.setFont(font1)
        self.label_newuser.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_newuser.setStyleSheet(u"color: rgb(56, 58, 89);")
        self.label_newuser.setAlignment(Qt.AlignCenter)
        self.Submit_Button = QPushButton(self.frame_Login)
        self.Submit_Button.setObjectName(u"Submit_Button")
        self.Submit_Button.setGeometry(QRect(150, 340, 71, 31))
        self.Submit_Button.setFont(font5)
        self.Submit_Button.setCursor(QCursor(Qt.PointingHandCursor))
        self.Submit_Button.setMouseTracking(True)
        self.Submit_Button.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"	background-color: rgb(56, 58, 87);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 12pt \"Segoe UI\";\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(13, 13, 13);\n"
"	background-color: rgb(255, 171, 215);\n"
"	font: 90 12pt \"Segoe UI\";\n"
"}")
        self.label_2 = QLabel(self.frame_Login)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 0, 151, 141))
        self.label_2.setStyleSheet(u"border-radius:30px;")
        self.label_2.setFrameShape(QFrame.StyledPanel)
        self.label_2.setFrameShadow(QFrame.Plain)
        self.label_2.setPixmap(QPixmap(u"./robo.gif").scaled(128, 128))
        self.label_2.setAlignment(Qt.AlignCenter)
        self.error = QLabel(self.frame_Login)
        self.error.setObjectName(u"error")
        self.error.setGeometry(QRect(30, 290, 301, 21))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(11)
        font6.setBold(False)
        font6.setWeight(50)
        self.error.setFont(font6)
        self.error.setStyleSheet(u"color: rgb(217, 21, 41);\n"
"background:transparent;")
        self.error.setAlignment(Qt.AlignCenter)
        self.error.setWordWrap(True)
        self.Forgot_pwd = QPushButton(self.frame_Login)
        self.Forgot_pwd.setObjectName(u"Forgot_pwd")
        self.Forgot_pwd.setGeometry(QRect(110, 380, 161, 31))
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(12)
        font7.setBold(True)
        font7.setItalic(False)
        font7.setWeight(75)
        self.Forgot_pwd.setFont(font7)
        self.Forgot_pwd.setCursor(QCursor(Qt.PointingHandCursor))
        self.Forgot_pwd.setMouseTracking(True)
        self.Forgot_pwd.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"	background-color: none;\n"
"	color: rgb(56, 58, 87);\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"	\n"
"	color: rgb(255, 171, 215);\n"
"	background-color: none;\n"
"\n"
"}")
        self.label_2.raise_()
        self.formGroupBox.raise_()
        self.signup_Button.raise_()
        self.label_newuser.raise_()
        self.Submit_Button.raise_()
        self.label_LOGIN.raise_()
        self.error.raise_()
        self.Forgot_pwd.raise_()
        self.label = QLabel(self.frame_main)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-130, -20, 47, 13))
        self.label_image = QLabel(self.frame_main)
        self.label_image.setObjectName(u"label_image")
        self.label_image.setGeometry(QRect(70, 190, 341, 321))
        self.label_image.setStyleSheet(u"QLabel{\n"
"   border-radius:20px;\n"
"	border-color: rgb(0, 0, 0);\n"
"}")
        self.label_image.setPixmap(QPixmap(u"./theft.jpg"))
        self.label_image.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.frame_main, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"Suspicious Activity Detector", None))
        self.label_LOGIN.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.label_id.setText(QCoreApplication.translate("MainWindow", u"User Id", None))
        self.lineEdit_id.setText("")
        self.lineEdit_id.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email-id", None))
        self.label_pwd.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.lineEdit_pwd.setText("")
        self.lineEdit_pwd.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.signup_Button.setText(QCoreApplication.translate("MainWindow", u"Sign up", None))
        self.label_newuser.setText(QCoreApplication.translate("MainWindow", u"New User?", None))
        self.Submit_Button.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.label_2.setText("")
        self.error.setText("")
        self.Forgot_pwd.setText(QCoreApplication.translate("MainWindow", u"Forgot password?", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_image.setText("")
    # retranslateUi

