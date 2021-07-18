# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'History-Suspicious ActivityeRGuvm.ui'
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
        MainWindow.resize(874, 575)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.History = QFrame(self.centralwidget)
        self.History.setObjectName(u"History")
        self.History.setGeometry(QRect(-20, 0, 901, 581))
        self.History.setMaximumSize(QSize(16777215, 16777215))
        self.History.setStyleSheet(u"QFrame{\n"
"background-color: rgb(56, 58, 89);\n"
"color: rgb(59, 61, 157);\n"
"border-radius:10px;\n"
"}")
        self.History.setFrameShape(QFrame.StyledPanel)
        self.History.setFrameShadow(QFrame.Raised)
        self.title = QLabel(self.History)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(230, 10, 491, 101))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet(u"\n"
"background:transparent;\n"
"color: rgb(213, 217, 240);")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setWordWrap(True)
        self.logo = QLabel(self.History)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(20, 20, 151, 111))
        self.logo.setStyleSheet(u"border-radius:30px;\n"
"background: transparent;")
        self.logo.setFrameShape(QFrame.StyledPanel)
        self.logo.setFrameShadow(QFrame.Plain)
        self.logo.setPixmap(QPixmap(u"./robo.gif").scaled(128, 128))
        self.logo.setAlignment(Qt.AlignCenter)
        self.username = QLabel(self.History)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(550, 10, 331, 31))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setWeight(50)
        self.username.setFont(font1)
        self.username.setLayoutDirection(Qt.LeftToRight)
        self.username.setStyleSheet(u"\n"
"background:transparent;\n"
"color: rgb(213, 217, 240);")
        self.username.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.username.setWordWrap(True)
        self.subtitle = QLabel(self.History)
        self.subtitle.setObjectName(u"subtitle")
        self.subtitle.setGeometry(QRect(310, 90, 351, 31))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(15)
        font2.setBold(False)
        font2.setWeight(50)
        self.subtitle.setFont(font2)
        self.subtitle.setStyleSheet(u"\n"
"background:transparent;\n"
"color: rgb(213, 217, 240);")
        self.subtitle.setAlignment(Qt.AlignCenter)
        self.subtitle.setWordWrap(True)
        self.table = QTableWidget(self.History)
        self.table.setObjectName(u"table")
        self.table.setGeometry(QRect(155, 151, 691, 371))
        font3 = QFont()
        font3.setPointSize(12)
        self.table.setFont(font3)
        self.table.setStyleSheet(u"background-color:rgb(166, 144, 255);\n"
"color:rgb(0,0,0);\n"
"border-radius:10px;\n"
"border: 2px;\n"
"border-color:rgb(255, 170, 255)")
        self.back = QPushButton(self.History)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(800, 60, 71, 21))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(11)
        self.back.setFont(font4)
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
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u" SUSPICIOUS ACTIVITY DETECTOR", None))
        self.logo.setText("")
        self.username.setText(QCoreApplication.translate("MainWindow", u"Welcome ", None))
        self.subtitle.setText(QCoreApplication.translate("MainWindow", u"History of Suspicious Activities", None))
        self.back.setText(QCoreApplication.translate("MainWindow", u"Back", None))
    # retranslateUi

