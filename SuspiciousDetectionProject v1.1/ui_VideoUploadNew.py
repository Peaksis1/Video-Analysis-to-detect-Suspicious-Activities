# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VideoUploadEanFHo.ui'
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

#------------------------------------------new------------------------------------
class ListBoxWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.resize(600, 600)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()

            links = []
            for url in event.mimeData().urls():
                # https://doc.qt.io/qt-5/qurl.html
                if url.isLocalFile():
                    links.append(str(url.toLocalFile()))
                else:
                    links.append(str(url.toString()))
            self.addItems(links)
        else:
            event.ignore()
#------------------------------------------------------------------------------

class Ui_Welcome(object):
    def setupUi(self, Welcome):
        if Welcome.objectName():
            Welcome.setObjectName(u"Welcome")
        Welcome.resize(900, 617)
        self.centralwidget = QWidget(Welcome)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-10, -10, 921, 631))
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
        self.label_logo.setPixmap(QPixmap(u"./robo.gif").scaled(128, 128))
        self.label_logo.setAlignment(Qt.AlignCenter)
        self.title = QLabel(self.frame)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(270, 40, 431, 51))
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
        self.label_drag = QLabel(self.frame)
        self.label_drag.setObjectName(u"label_drag")
        self.label_drag.setGeometry(QRect(410, 220, 181, 91))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_drag.setFont(font1)
        self.label_drag.setStyleSheet(u"background: transparent;\n"
"color: rgb(56, 58, 89)")
        self.label_drag.setAlignment(Qt.AlignCenter)
        self.label_drag.setWordWrap(True)

        
        #-------------------------------------new------------------------------------------
        self.listWidget = ListBoxWidget(self.frame)
        #-------------------------------------new-----------------------------------------
        
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(210, 110, 641, 311))
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.listWidget.setFont(font2)
        self.listWidget.setAcceptDrops(True)
        self.listWidget.setStyleSheet(u"background-color: rgb(166, 144, 255);\n"
"color: rgb(71, 63, 159);\n"
"border-radius:10px;\n"
"border: 4px dashed ;\n"
"border-color:rgb(255, 171, 215);")
        self.copy_path = QPushButton(self.frame)
        self.copy_path.setObjectName(u"copy_path")
        self.copy_path.setGeometry(QRect(50, 210, 91, 31))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(11)
        self.copy_path.setFont(font3)
        self.copy_path.setCursor(QCursor(Qt.PointingHandCursor))
        self.copy_path.setMouseTracking(True)
        self.copy_path.setStyleSheet(u"QPushButton{\n"
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
        self.PathCopiedMsg = QLabel(self.frame)
        self.PathCopiedMsg.setObjectName(u"PathCopiedMsg")
        self.PathCopiedMsg.setGeometry(QRect(20, 290, 151, 101))
        self.PathCopiedMsg.setFont(font2)
        self.PathCopiedMsg.setStyleSheet(u"color: rgb(166, 144, 255)")
        self.PathCopiedMsg.setAlignment(Qt.AlignCenter)
        self.PathCopiedMsg.setWordWrap(True)
        self.Start = QPushButton(self.frame)
        self.Start.setObjectName(u"Start")
        self.Start.setGeometry(QRect(50, 460, 91, 31))
        self.Start.setFont(font3)
        self.Start.setCursor(QCursor(Qt.PointingHandCursor))
        self.Start.setMouseTracking(True)
        self.Start.setStyleSheet(u"QPushButton{\n"
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
        self.output = QLabel(self.frame)
        self.output.setObjectName(u"output")
        self.output.setGeometry(QRect(200, 460, 651, 141))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(12)
        font4.setBold(True)
        font4.setWeight(75)
        self.output.setFont(font4)
        self.output.setStyleSheet(u"background-color: rgba(13,13,13, 110);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border: 4px dashed ;\n"
"border-color:rgb(166, 144, 255);")
        self.output.setAlignment(Qt.AlignCenter)
        self.output.setWordWrap(True)
        self.username = QLabel(self.frame)
        self.username.setObjectName(u"username")
        self.username.setGeometry(QRect(560, 10, 331, 31))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(12)
        font5.setBold(False)
        font5.setWeight(50)
        self.username.setFont(font5)
        self.username.setLayoutDirection(Qt.LeftToRight)
        self.username.setStyleSheet(u"\n"
"background:transparent;\n"
"color: rgb(213, 217, 240);")
        self.username.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.username.setWordWrap(True)
        self.back = QPushButton(self.frame)
        self.back.setObjectName(u"back")
        self.back.setGeometry(QRect(830, 60, 61, 21))
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
        self.listWidget.raise_()
        self.title.raise_()
        self.label_logo.raise_()
        self.label_drag.raise_()
        self.copy_path.raise_()
        self.PathCopiedMsg.raise_()
        self.Start.raise_()
        self.output.raise_()
        self.username.raise_()
        self.back.raise_()
        Welcome.setCentralWidget(self.centralwidget)

        self.retranslateUi(Welcome)

        QMetaObject.connectSlotsByName(Welcome)
    # setupUi

    def retranslateUi(self, Welcome):
        Welcome.setWindowTitle(QCoreApplication.translate("Welcome", u"MainWindow", None))
        self.label_logo.setText("")
        self.title.setText(QCoreApplication.translate("Welcome", u"Video Analysis", None))
        self.label_drag.setText("")
        self.copy_path.setText(QCoreApplication.translate("Welcome", u"Copy Path", None))
        self.PathCopiedMsg.setText("")
        self.Start.setText(QCoreApplication.translate("Welcome", u"Start", None))
        self.output.setText(QCoreApplication.translate("Welcome", u"Output will be shown here ", None))
        self.username.setText(QCoreApplication.translate("Welcome", u"Welcome ", None))
        self.back.setText(QCoreApplication.translate("Welcome", u"Back", None))
    # retranslateUi

