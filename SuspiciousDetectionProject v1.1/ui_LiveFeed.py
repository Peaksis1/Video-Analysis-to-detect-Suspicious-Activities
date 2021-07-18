# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LiveFeedbwAvVr.ui'
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


class Ui_Welcome(object):
    def setupUi(self, Welcome):
        if Welcome.objectName():
            Welcome.setObjectName(u"Welcome")
        Welcome.resize(810, 598)
        self.centralwidget = QWidget(Welcome)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-10, -10, 901, 611))
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(56, 58, 89);\n"
"color: rgb(59, 61, 157);\n"
"border-radius:10px;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_logo = QLabel(self.frame)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setGeometry(QRect(20, 20, 151, 141))
        self.label_logo.setStyleSheet(u"border-radius:30px;")
        self.label_logo.setFrameShape(QFrame.StyledPanel)
        self.label_logo.setFrameShadow(QFrame.Plain)
        self.label_logo.setPixmap(QPixmap(u"../../../../../../../../OneDrive/Pictures/robo.gif").scaled(128, 128))
        self.label_logo.setAlignment(Qt.AlignCenter)
        self.title = QLabel(self.frame)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(250, 40, 361, 101))
        font = QFont()
        font.setFamily(u"Segoe UI Semibold")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet(u"\n"
"background:transparent;\n"
"color: rgb(213, 217, 240);")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setWordWrap(True)
        self.Start = QPushButton(self.frame)
        self.Start.setObjectName(u"Start")
        self.Start.setGeometry(QRect(30, 260, 91, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(13)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(12)
        self.Start.setFont(font1)
        self.Start.setCursor(QCursor(Qt.PointingHandCursor))
        self.Start.setMouseTracking(True)
        self.Start.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"	color: rgb(13, 13, 13);\n"
"	background-color: rgb(255, 171, 215);\n"
"	font: 100 13pt \"Segoe UI\";\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(62, 61, 106);\n"
"	background-color: rgb(166, 144, 255);\n"
"	font: 90 12pt \"Segoe UI\";	\n"
"}")
        self.output = QLabel(self.frame)
        self.output.setObjectName(u"output")
        self.output.setGeometry(QRect(160, 360, 581, 221))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.output.setFont(font2)
        self.output.setStyleSheet(u"background-color: rgba(13,13,13, 110);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border: 4px dashed ;\n"
"border-color:rgb(166, 144, 255);")
        self.output.setAlignment(Qt.AlignCenter)
        self.output.setWordWrap(True)
        self.updateBox = QGroupBox(self.frame)
        self.updateBox.setObjectName(u"updateBox")
        self.updateBox.setGeometry(QRect(160, 160, 581, 151))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setWeight(75)
        self.updateBox.setFont(font3)
        self.updateBox.setLayoutDirection(Qt.LeftToRight)
        self.updateBox.setStyleSheet(u"color: rgb(255, 171, 215);\n"
"border-color: rgb(255, 171, 215);")
        self.updateBox.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.updateBox.setFlat(False)
        self.updateBox.setCheckable(False)
        self.username = QLabel(self.frame)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(470, 20, 331, 31))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setWeight(50)
        self.username.setFont(font4)
        self.username.setLayoutDirection(Qt.LeftToRight)
        self.username.setStyleSheet(u"\n"
"background:transparent;\n"
"color: rgb(213, 217, 240);")
        self.username.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.username.setWordWrap(True)
        self.back = QPushButton(self.frame)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(730, 70, 71, 21))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(12)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(11)
        self.back.setFont(font5)
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
        self.update = QLabel(self.frame)
        self.update.setObjectName(u"update")
        self.update.setGeometry(QRect(240, 190, 441, 91))
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(True)
        font6.setWeight(75)
        self.update.setFont(font6)
        self.update.setLayoutDirection(Qt.LeftToRight)
        self.update.setStyleSheet(u"color: rgb(166, 144, 255);\n"
"background: transparent;")
        self.update.setAlignment(Qt.AlignCenter)
        self.update.setWordWrap(True)
        self.StopAlarm = QPushButton(self.frame)
        self.StopAlarm.setObjectName(u"StopAlarm")
        self.StopAlarm.setGeometry(QRect(30, 380, 91, 31))
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(12)
        font7.setBold(False)
        font7.setItalic(False)
        font7.setWeight(12)
        self.StopAlarm.setFont(font7)
        self.StopAlarm.setCursor(QCursor(Qt.PointingHandCursor))
        self.StopAlarm.setMouseTracking(True)
        self.StopAlarm.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"	color: rgb(13, 13, 13);\n"
"	background-color: rgb(255, 171, 215);\n"
"	font: 100 12pt \"Segoe UI\";\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(62, 61, 106);\n"
"	background-color: rgb(166, 144, 255);\n"
"	font: 90 12pt \"Segoe UI\";	\n"
"}")
        self.title.raise_()
        self.label_logo.raise_()
        self.Start.raise_()
        self.output.raise_()
        self.updateBox.raise_()
        self.username.raise_()
        self.back.raise_()
        self.update.raise_()
        self.StopAlarm.raise_()
        Welcome.setCentralWidget(self.centralwidget)

        self.retranslateUi(Welcome)

        QMetaObject.connectSlotsByName(Welcome)
    # setupUi

    def retranslateUi(self, Welcome):
        Welcome.setWindowTitle(QCoreApplication.translate("Welcome", u"MainWindow", None))
        self.label_logo.setText("")
        self.title.setText(QCoreApplication.translate("Welcome", u"Live Feed Analysis", None))
        self.Start.setText(QCoreApplication.translate("Welcome", u"Start", None))
        self.output.setText(QCoreApplication.translate("Welcome", u"Output will be shown here ", None))
        self.updateBox.setTitle(QCoreApplication.translate("Welcome", u"STATUS UPDATE", None))
        self.username.setText(QCoreApplication.translate("Welcome", u"Username:", None))
        self.back.setText(QCoreApplication.translate("Welcome", u"Back", None))
        self.update.setText(QCoreApplication.translate("Welcome", u"Press START to begin the Live Feed Analysis..", None))
        self.StopAlarm.setText(QCoreApplication.translate("Welcome", u"Stop Alarm", None))
    # retranslateUi

