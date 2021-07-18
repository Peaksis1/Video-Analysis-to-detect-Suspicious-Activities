# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DashboardNPwdvR.ui'
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

EMail=1 #changed 

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
        self.title.setGeometry(QRect(210, 30, 491, 101))
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
        self.videoAnalysis = QPushButton(self.Dashboard)
        self.videoAnalysis.setObjectName(u"videoAnalysis")
        self.videoAnalysis.setGeometry(QRect(540, 160, 311, 291))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(11)
        self.videoAnalysis.setFont(font1)
        self.videoAnalysis.setCursor(QCursor(Qt.PointingHandCursor))
        self.videoAnalysis.setMouseTracking(True)
        self.videoAnalysis.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"	color: rgb(13, 13, 13);\n"
"	background-image : url(detective.jpg);\n"
"	background-repeat: no-repeat;\n"
"	font: 90 12pt \"Segoe UI\";\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(62, 61, 106);\n"
"	background-color: rgb(166, 144, 255);\n"
"	font: 90 12pt \"Segoe UI\";	\n"
"}")
        self.liveFeed = QPushButton(self.Dashboard)
        self.liveFeed.setObjectName(u"liveFeed")
        self.liveFeed.setGeometry(QRect(90, 160, 311, 291))
        self.liveFeed.setFont(font1)
        self.liveFeed.setCursor(QCursor(Qt.PointingHandCursor))
        self.liveFeed.setMouseTracking(True)
        self.liveFeed.setStyleSheet(u"QPushButton{\n"
"border-radius:10px;\n"
"	color: rgb(13, 13, 13);\n"
"	background-image: url(detective.png) ;\n"
"	background-repeat: no-repeat;\n"
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
        self.logo.setGeometry(QRect(20, 20, 161, 121))
        self.logo.setStyleSheet(u"border-radius:30px;\n"
"background: transparent;")
        self.logo.setFrameShape(QFrame.StyledPanel)
        self.logo.setFrameShadow(QFrame.Plain)
        self.logo.setPixmap(QPixmap(u"./robo.gif").scaled(128, 128))
        self.logo.setAlignment(Qt.AlignCenter)
        self.username = QLabel(self.Dashboard)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(570, 20, 331, 31))
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
        self.label_analysis = QLabel(self.Dashboard)
        self.label_analysis.setObjectName(u"label_analysis")
        self.label_analysis.setGeometry(QRect(560, 470, 281, 31))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(15)
        font3.setBold(False)
        font3.setWeight(50)
        self.label_analysis.setFont(font3)
        self.label_analysis.setStyleSheet(u"\n"
"background:transparent;\n"
"color: rgb(213, 217, 240);")
        self.label_analysis.setAlignment(Qt.AlignCenter)
        self.label_analysis.setWordWrap(True)
        self.label_cctv = QLabel(self.Dashboard)
        self.label_cctv.setObjectName(u"label_cctv")
        self.label_cctv.setGeometry(QRect(60, 470, 351, 31))
        self.label_cctv.setFont(font3)
        self.label_cctv.setStyleSheet(u"\n"
"background:transparent;\n"
"color: rgb(213, 217, 240);")
        self.label_cctv.setAlignment(Qt.AlignCenter)
        self.label_cctv.setWordWrap(True)
        self.logout = QPushButton(self.Dashboard)
        self.logout.setObjectName(u"logout")
        self.logout.setGeometry(QRect(830, 110, 71, 21))
        self.logout.setFont(font1)
        self.logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.logout.setMouseTracking(True)
        self.logout.setStyleSheet(u"QPushButton{\n"
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
        #-----------------------------------------------------------------------------
        self.history = QPushButton(self.Dashboard)
        self.history.setObjectName(u"history")
        self.history.setGeometry(QRect(810, 70, 101, 21))
        self.history.setFont(font1)
        self.history.setCursor(QCursor(Qt.PointingHandCursor))
        self.history.setMouseTracking(True)
        self.history.setStyleSheet(u"QPushButton{\n"
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
        #---------------------------------------------------------------------------------------------------
        self.userOptions = QGroupBox(self.Dashboard)
        self.userOptions.setObjectName(u"userOptions")
        self.userOptions.setGeometry(QRect(86, 540, 771, 111))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(14)
        font4.setBold(True)
        font4.setWeight(75)
        self.userOptions.setFont(font4)
        self.userOptions.setLayoutDirection(Qt.LeftToRight)
        self.userOptions.setStyleSheet(u"color: rgb(255, 171, 215);\n"
"border-color: rgb(255, 171, 215);\n"
"background:transparent;\n"
"")
        self.userOptions.setAlignment(Qt.AlignCenter)
        self.userOptions.setFlat(False)
        self.userOptions.setCheckable(False)
        self.Yes = QRadioButton(self.userOptions)
        self.Yes.setObjectName(u"Yes")
        self.Yes.setGeometry(QRect(530, 40, 51, 41))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(12)
        self.Yes.setFont(font5)
        self.Yes.setChecked(True)
        self.receiveEmail = QLabel(self.userOptions)
        self.receiveEmail.setObjectName(u"receiveEmail")
        self.receiveEmail.setGeometry(QRect(10, 40, 501, 41))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(13)
        self.receiveEmail.setFont(font6)
        self.receiveEmail.setAlignment(Qt.AlignCenter)
        self.No = QRadioButton(self.userOptions)
        self.No.setObjectName(u"No")
        self.No.setGeometry(QRect(630, 40, 51, 41))
        self.No.setFont(font5)
        
        Welcome.setCentralWidget(self.centralwidget)

        self.retranslateUi(Welcome)

        QMetaObject.connectSlotsByName(Welcome)
        
        #-------------------------------------------------------------------------
        
        self.Yes.toggled.connect(lambda : self.btnstate(self.Yes))
        self.No.toggled.connect(lambda : self.btnstate(self.No))
            
        #-------------------------------------------------------------------------
    
    #-------------------------------------------------------------------------
    def btnstate(self,B):
        
        global EMail
        if B.text() == "Yes":
            if B.isChecked():
                EMail=1
                
        if B.text() == "No":
            if B.isChecked():
                EMail=0
                
    #-------------------------------------------------------------------------
    
    # setupUi

    def retranslateUi(self, Welcome):
        Welcome.setWindowTitle(QCoreApplication.translate("Welcome", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("Welcome", u" SUSPICIOUS ACTIVITY DETECTOR", None))
        self.videoAnalysis.setText("")
        self.liveFeed.setText("")
        self.logo.setText("")
        self.username.setText(QCoreApplication.translate("Welcome", u"Welcome ", None))
        self.label_analysis.setText(QCoreApplication.translate("Welcome", u"Video Analysis", None))
        self.label_cctv.setText(QCoreApplication.translate("Welcome", u"CCTV Live Feed Analysis", None))
        self.logout.setText(QCoreApplication.translate("Welcome", u"Logout", None))
        self.history.setText(QCoreApplication.translate("Welcome", u"Check History", None))
        self.userOptions.setTitle(QCoreApplication.translate("Welcome", u"USER OPTIONS", None))
        self.Yes.setText(QCoreApplication.translate("Welcome", u"Yes", None))
        self.receiveEmail.setText(QCoreApplication.translate("Welcome", u"Do you want to receive notifications through email ?", None))
        self.No.setText(QCoreApplication.translate("Welcome", u"No", None))
    # retranslateUi

