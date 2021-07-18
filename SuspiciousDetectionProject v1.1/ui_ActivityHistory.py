# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ActivityHistoryYedFuC.ui'
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
        Welcome.resize(882, 672)
        self.centralwidget = QWidget(Welcome)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Dashboard = QFrame(self.centralwidget)
        self.Dashboard.setObjectName(u"Dashboard")
        self.Dashboard.setGeometry(QRect(-30, -10, 1031, 721))
        self.Dashboard.setMaximumSize(QSize(16777215, 16777215))
        self.Dashboard.setStyleSheet(u"QFrame{\n"
"background-color: rgb(56, 58, 89);\n"
"color: rgb(59, 61, 157);\n"
"border-radius:10px;\n"
"}")
        self.Dashboard.setFrameShape(QFrame.StyledPanel)
        self.Dashboard.setFrameShadow(QFrame.Raised)
        self.title = QLabel(self.Dashboard)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(250, 50, 491, 101))
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
        self.videofile = QPushButton(self.Dashboard)
        self.videofile.setObjectName(u"videofile")
        self.videofile.setGeometry(QRect(550, 210, 311, 291))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(11)
        self.videofile.setFont(font1)
        self.videofile.setCursor(QCursor(Qt.PointingHandCursor))
        self.videofile.setMouseTracking(True)
        self.videofile.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"	color: rgb(13, 13, 13);\n"
"	background-image : url(detective.jpg);\n"
"	font: 90 12pt \"Segoe UI\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(62, 61, 106);\n"
"	background-color: rgb(166, 144, 255);\n"
"	font: 90 12pt \"Segoe UI\";	\n"
"}")
        self.videofeed = QPushButton(self.Dashboard)
        self.videofeed.setObjectName(u"videofeed")
        self.videofeed.setGeometry(QRect(140, 210, 321, 291))
        self.videofeed.setFont(font1)
        self.videofeed.setCursor(QCursor(Qt.PointingHandCursor))
        self.videofeed.setMouseTracking(True)
        self.videofeed.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"	color: rgb(13, 13, 13);\n"
"	background-image: url(detective.png) ;\n"
"	font: 90 12pt \"Segoe UI\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(62, 61, 106);\n"
"	background-color: rgb(166, 144, 255);\n"
"	font: 90 12pt \"Segoe UI\";	\n"
"}")
        self.logo = QLabel(self.Dashboard)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(30, 30, 161, 121))
        self.logo.setStyleSheet(u"border-radius:30px;\n"
"background: transparent;")
        self.logo.setFrameShape(QFrame.StyledPanel)
        self.logo.setFrameShadow(QFrame.Plain)
        self.logo.setPixmap(QPixmap(u"./robo.gif").scaled(128, 128))
        self.logo.setAlignment(Qt.AlignCenter)
        self.username = QLabel(self.Dashboard)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(560, 30, 331, 31))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setWeight(50)
        self.username.setFont(font2)
        self.username.setLayoutDirection(Qt.LeftToRight)
        self.username.setStyleSheet(u"\n"
"background:transparent;\n"
"color: rgb(213, 217, 240);")
        self.username.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.username.setWordWrap(True)
        
        #---------------------------------------------------------------------
        self.back = QPushButton(self.Dashboard)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(830, 110, 71, 21))
        self.back.setFont(font1)
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
        #--------------------------------------------------------------------------
        self.label_file = QLabel(self.Dashboard)
        self.label_file.setObjectName(u"label_file")
        self.label_file.setGeometry(QRect(560, 530, 271, 41))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(20)
        font3.setBold(False)
        font3.setWeight(50)
        self.label_file.setFont(font3)
        self.label_file.setStyleSheet(u"\n"
"background:transparent;\n"
"color: rgb(213, 217, 240);")
        self.label_file.setAlignment(Qt.AlignCenter)
        self.label_file.setWordWrap(True)
        self.label_file.setOpenExternalLinks(False)
        self.label_feed = QLabel(self.Dashboard)
        self.label_feed.setObjectName(u"label_feed")
        self.label_feed.setGeometry(QRect(110, 530, 351, 41))
        self.label_feed.setFont(font3)
        self.label_feed.setStyleSheet(u"\n"
"background:transparent;\n"
"color: rgb(213, 217, 240);")
        self.label_feed.setAlignment(Qt.AlignCenter)
        self.label_feed.setWordWrap(True)
        Welcome.setCentralWidget(self.centralwidget)

        self.retranslateUi(Welcome)

        QMetaObject.connectSlotsByName(Welcome)
    # setupUi

    def retranslateUi(self, Welcome):
        Welcome.setWindowTitle(QCoreApplication.translate("Welcome", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("Welcome", u" HISTORY OF SUSPICIOUS ACTIVITIES ", None))
        self.videofile.setText("")
        self.videofeed.setText("")
        self.logo.setText("")
        self.username.setText(QCoreApplication.translate("Welcome", u"Username: ", None))
        self.back.setText(QCoreApplication.translate("Welcome", u"Back", None))
        self.label_file.setText(QCoreApplication.translate("Welcome", u"Video History", None))
        self.label_feed.setText(QCoreApplication.translate("Welcome", u"Live Feed History", None))
    # retranslateUi

