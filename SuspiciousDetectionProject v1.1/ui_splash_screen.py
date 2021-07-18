# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splash_screenPyNBgk.ui'
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
        MainWindow.resize(676, 348)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame1 = QFrame(self.centralwidget)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setEnabled(True)
        self.frame1.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame1.setMouseTracking(True)
        self.frame1.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(56, 58, 89);\n"
"	color: rgb(235, 10, 255);\n"
"	border-radius:10px;\n"
"}")
        self.frame1.setFrameShape(QFrame.StyledPanel)
        self.frame1.setFrameShadow(QFrame.Raised)
        self.label_title = QLabel(self.frame1)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(-50, 30, 731, 71))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(32)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"\n"
"color: rgb(254, 121,199);")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_description = QLabel(self.frame1)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(140, 100, 361, 91))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(16)
        font1.setBold(False)
        font1.setWeight(50)
        self.label_description.setFont(font1)
        self.label_description.setToolTipDuration(-1)
        self.label_description.setStyleSheet(u"color: rgb(166, 144, 255);")
        self.label_description.setAlignment(Qt.AlignCenter)
        self.label_description.setWordWrap(True)
        self.progressBar = QProgressBar(self.frame1)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 240, 611, 21))
        self.progressBar.setCursor(QCursor(Qt.PointingHandCursor))
        self.progressBar.setMouseTracking(False)
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	\n"
"	background-color: rgb(98, 114, 164);\n"
"    color: rgb(200, 200, 200);\n"
"    border-style:none;\n"
"	border-radius: 10px;\n"
"	text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.034, y1:0.448636, x2:1, y2:0.426, stop:0.0284091 rgba(245, 97, 221, 255), stop:0.971591 rgba(204, 51, 255, 255));\n"
"}")
        self.progressBar.setValue(24)
        self.label_loading = QLabel(self.frame1)
        self.label_loading.setObjectName(u"label_loading")
        self.label_loading.setGeometry(QRect(180, 270, 301, 20))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setWeight(50)
        self.label_loading.setFont(font2)
        self.label_loading.setToolTipDuration(-1)
        self.label_loading.setStyleSheet(u"color: rgb(166, 144, 255);")
        self.label_loading.setAlignment(Qt.AlignCenter)
        self.label_loading.setWordWrap(True)

        self.verticalLayout.addWidget(self.frame1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"Suspicious Activity Detector", None))
        self.label_description.setText(QCoreApplication.translate("MainWindow", u"This Application detects suspicious activity and informs the user accordingily.", None))
        self.label_loading.setText(QCoreApplication.translate("MainWindow", u"loading...", None))
    # retranslateUi

