# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RegisterhJsTIL.ui'
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


class Ui_SignUpWindow(object):
    def setupUi(self, SignUpWindow):
        if SignUpWindow.objectName():
            SignUpWindow.setObjectName(u"SignUpWindow")
        SignUpWindow.resize(854, 572)
        self.centralwidget = QWidget(SignUpWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(56, 58, 89);\n"
"	color: rgb(59, 61, 157);\n"
"	border-radius:10px;\n"
"}")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.innerframe = QFrame(self.main_frame)
        self.innerframe.setObjectName(u"innerframe")
        self.innerframe.setGeometry(QRect(10, 60, 811, 461))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.innerframe.setFont(font)
        self.innerframe.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(166, 144, 255);\n"
"	color: rgb(96, 98, 189);\n"
"	border-radius:10px;\n"
"}\n"
"")
        self.innerframe.setFrameShape(QFrame.StyledPanel)
        self.innerframe.setFrameShadow(QFrame.Raised)
        self.formGroupBox = QGroupBox(self.innerframe)
        self.formGroupBox.setObjectName(u"formGroupBox")
        self.formGroupBox.setGeometry(QRect(110, 100, 611, 241))
        self.Login_form = QFormLayout(self.formGroupBox)
        self.Login_form.setObjectName(u"Login_form")
        self.Login_form.setHorizontalSpacing(10)
        self.Login_form.setVerticalSpacing(10)
        self.Login_form.setContentsMargins(20, 30, 20, 1)
        self.label_name = QLabel(self.formGroupBox)
        self.label_name.setObjectName(u"label_name")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_name.setFont(font1)
        self.label_name.setStyleSheet(u"color: rgb(56, 58, 89);\n"
"background: transparent;")
        self.label_name.setAlignment(Qt.AlignCenter)

        self.Login_form.setWidget(0, QFormLayout.LabelRole, self.label_name)

        self.Name = QLineEdit(self.formGroupBox)
        self.Name.setObjectName(u"Name")
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        self.Name.setFont(font2)
        self.Name.setAutoFillBackground(False)
        self.Name.setStyleSheet(u"border-radius:10px;")
        self.Name.setAlignment(Qt.AlignCenter)

        self.Login_form.setWidget(0, QFormLayout.FieldRole, self.Name)

        self.label_emailid = QLabel(self.formGroupBox)
        self.label_emailid.setObjectName(u"label_emailid")
        self.label_emailid.setFont(font1)
        self.label_emailid.setStyleSheet(u"color: rgb(56, 58, 89);\n"
"background: transparent;")
        self.label_emailid.setAlignment(Qt.AlignCenter)

        self.Login_form.setWidget(1, QFormLayout.LabelRole, self.label_emailid)

        self.Email_id = QLineEdit(self.formGroupBox)
        self.Email_id.setObjectName(u"Email_id")
        self.Email_id.setFont(font2)
        self.Email_id.setAutoFillBackground(False)
        self.Email_id.setStyleSheet(u"border-radius:10px;")
        self.Email_id.setAlignment(Qt.AlignCenter)

        self.Login_form.setWidget(1, QFormLayout.FieldRole, self.Email_id)

        self.label_password = QLabel(self.formGroupBox)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setFont(font1)
        self.label_password.setStyleSheet(u"color: rgb(56, 58, 89);")
        self.label_password.setAlignment(Qt.AlignCenter)

        self.Login_form.setWidget(2, QFormLayout.LabelRole, self.label_password)

        self.Password = QLineEdit(self.formGroupBox)
        self.Password.setObjectName(u"Password")
        self.Password.setFont(font2)
        self.Password.setStyleSheet(u"border-radius:10px;")
        self.Password.setMaxLength(8)
        self.Password.setEchoMode(QLineEdit.Password)
        self.Password.setAlignment(Qt.AlignCenter)

        self.Login_form.setWidget(2, QFormLayout.FieldRole, self.Password)

        self.label_confirmpwd = QLabel(self.formGroupBox)
        self.label_confirmpwd.setObjectName(u"label_confirmpwd")
        self.label_confirmpwd.setFont(font1)
        self.label_confirmpwd.setStyleSheet(u"color: rgb(56, 58, 89);")
        self.label_confirmpwd.setAlignment(Qt.AlignCenter)
        self.label_confirmpwd.setWordWrap(True)

        self.Login_form.setWidget(3, QFormLayout.LabelRole, self.label_confirmpwd)

        self.Confirm_pwd = QLineEdit(self.formGroupBox)
        self.Confirm_pwd.setObjectName(u"Confirm_pwd")
        self.Confirm_pwd.setFont(font2)
        self.Confirm_pwd.setStyleSheet(u"border-radius:10px;")
        self.Confirm_pwd.setMaxLength(8)
        self.Confirm_pwd.setEchoMode(QLineEdit.Password)
        self.Confirm_pwd.setAlignment(Qt.AlignCenter)

        self.Login_form.setWidget(3, QFormLayout.FieldRole, self.Confirm_pwd)

        self.pwd_detail = QLabel(self.formGroupBox)
        self.pwd_detail.setObjectName(u"pwd_detail")
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setWeight(50)
        self.pwd_detail.setFont(font3)
        self.pwd_detail.setStyleSheet(u"color: rgb(56, 58, 89);")
        self.pwd_detail.setAlignment(Qt.AlignCenter)
        self.pwd_detail.setWordWrap(True)

        self.Login_form.setWidget(4, QFormLayout.FieldRole, self.pwd_detail)

        self.SignupButton = QPushButton(self.innerframe)
        self.SignupButton.setObjectName(u"SignupButton")
        self.SignupButton.setGeometry(QRect(450, 370, 71, 31))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(9)
        self.SignupButton.setFont(font4)
        self.SignupButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.SignupButton.setMouseTracking(True)
        self.SignupButton.setStyleSheet(u"QPushButton{\n"
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
        self.back = QPushButton(self.innerframe)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(730, 380, 61, 21))
        self.back.setFont(font3)
        self.back.setCursor(QCursor(Qt.PointingHandCursor))
        self.back.setMouseTracking(True)
        self.back.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"	color: rgb(13, 13, 13);\n"
"	background-color: rgb(255, 171, 215);\n"
"	font: 90 12pt \"Segoe UI\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(62, 61, 106);\n"
"	background-color: rgb(166, 144, 255);\n"
"	font: 90 12pt \"Segoe UI\";	\n"
"}")
        self.label_signup = QLabel(self.innerframe)
        self.label_signup.setObjectName(u"label_signup")
        self.label_signup.setGeometry(QRect(300, 30, 201, 41))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(20)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_signup.setFont(font5)
        self.label_signup.setStyleSheet(u"color: rgb(56, 58, 89);\n"
"background:transparent;")
        self.label_signup.setAlignment(Qt.AlignCenter)
        self.label_warning = QLabel(self.innerframe)
        self.label_warning.setObjectName(u"label_warning")
        self.label_warning.setGeometry(QRect(150, 70, 541, 20))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(11)
        font6.setBold(False)
        font6.setWeight(50)
        self.label_warning.setFont(font6)
        self.label_warning.setStyleSheet(u"color: rgb(217, 21, 41);\n"
"background:transparent;")
        self.label_warning.setAlignment(Qt.AlignCenter)
        self.Reset = QPushButton(self.innerframe)
        self.Reset.setObjectName(u"Reset")
        self.Reset.setGeometry(QRect(320, 370, 71, 31))
        self.Reset.setFont(font4)
        self.Reset.setCursor(QCursor(Qt.PointingHandCursor))
        self.Reset.setMouseTracking(True)
        self.Reset.setStyleSheet(u"QPushButton{\n"
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
        self.label = QLabel(self.main_frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-130, -20, 47, 13))
        self.label_logo = QLabel(self.main_frame)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setGeometry(QRect(20, 0, 151, 141))
        self.label_logo.setStyleSheet(u"border-radius:30px;")
        self.label_logo.setFrameShape(QFrame.StyledPanel)
        self.label_logo.setFrameShadow(QFrame.Plain)
        self.label_logo.setPixmap(QPixmap(u"./robo.gif").scaled(128, 128))
        self.label_logo.setAlignment(Qt.AlignCenter)
        self.title = QLabel(self.main_frame)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(180, 10, 431, 31))
        self.title.setFont(font5)
        self.title.setStyleSheet(u"\n"
"background:transparent;\n"
"color: rgb(213, 217, 240);")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setWordWrap(True)

        self.gridLayout_2.addWidget(self.main_frame, 0, 0, 1, 1)

        SignUpWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SignUpWindow)

        QMetaObject.connectSlotsByName(SignUpWindow)
    # setupUi

    def retranslateUi(self, SignUpWindow):
        SignUpWindow.setWindowTitle(QCoreApplication.translate("SignUpWindow", u"MainWindow", None))
        self.label_name.setText(QCoreApplication.translate("SignUpWindow", u"Name", None))
        self.Name.setText("")
        self.Name.setPlaceholderText(QCoreApplication.translate("SignUpWindow", u"Full Name", None))
        self.label_emailid.setText(QCoreApplication.translate("SignUpWindow", u"Email-id", None))
        self.Email_id.setText("")
        self.Email_id.setPlaceholderText(QCoreApplication.translate("SignUpWindow", u"Email-id", None))
        self.label_password.setText(QCoreApplication.translate("SignUpWindow", u"Password", None))
        self.Password.setText("")
        self.Password.setPlaceholderText(QCoreApplication.translate("SignUpWindow", u"Password", None))
        self.label_confirmpwd.setText(QCoreApplication.translate("SignUpWindow", u"Confirm Password", None))
        self.Confirm_pwd.setText("")
        self.Confirm_pwd.setPlaceholderText(QCoreApplication.translate("SignUpWindow", u"Confirm Password", None))
        self.pwd_detail.setText(QCoreApplication.translate("SignUpWindow", u"Password must contain 8 alphanumeric characters, ' @ ' and ' _ '  also allowed", None))
        self.SignupButton.setText(QCoreApplication.translate("SignUpWindow", u"Submit", None))
        self.label_signup.setText(QCoreApplication.translate("SignUpWindow", u"Sign Up", None))
        self.label_warning.setText("")
        self.Reset.setText(QCoreApplication.translate("SignUpWindow", u"Reset", None))
        self.label.setText(QCoreApplication.translate("SignUpWindow", u"TextLabel", None))
        self.label_logo.setText("")
        self.title.setText(QCoreApplication.translate("SignUpWindow", u"Suspicious Activity Detector", None))
        self.back.setText(QCoreApplication.translate("Welcome", u"Back", None))
    # retranslateUi

