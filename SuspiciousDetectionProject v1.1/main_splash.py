import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint,
    QRect, QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import *

##Splash Screen
#import ui_splash_screen
from ui_splash_screen import Ui_MainWindow

class SplashScreen(QMainWindow, Ui_MainWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self)
        super(SplashScreen, self).__init__(parent)
        self.setupUi(self)

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=SplashScreen()
    window.show()
    app.exec_()