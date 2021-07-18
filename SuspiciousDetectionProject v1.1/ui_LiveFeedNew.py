import cv2
import numpy as np
import keras
from datetime import datetime
import tensorflow as tf

model =  tf.keras.models.load_model('mymodelmain1.h5')

from playsound import playsound
import os
from datetime import datetime
import multiprocessing
from PyQt5 import QtCore, QtGui, QtWidgets

from ui_DashboardNew import EMail
######################################################## NO CHANGE #####################################################################

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
        self.label_logo.setPixmap(QPixmap(u"./robo.gif").scaled(128, 128))
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
        self.username.setText(QCoreApplication.translate("Welcome", u"Welcome ", None))
        self.back.setText(QCoreApplication.translate("Welcome", u"Back", None))
        self.update.setText(QCoreApplication.translate("Welcome", u"Press START to begin the Live Feed Analysis..", None))
        self.StopAlarm.setText(QCoreApplication.translate("Welcome", u"Stop Alarm", None))
    # retranslateUi

############################################# NO CHANGE ###############################################################

    def ringAlarm(self):
        
        self.AlarmPlaying=0
        self.StopAlarm.clicked.connect(self.terminateAlarm)
            
        if not os.path.isfile('lastringtime.txt'):
            file = open("lastringtime.txt", "w") 
            file.write(str(int(datetime.now().timestamp())))
            f = 1
        else:
            file = open("lastringtime.txt", "r+")
            if(int(datetime.now().timestamp())-int(file.read())>900):
                f=1
            else:
                f=0
            
            file.close()
            
        
        if f==1:
            self.p = multiprocessing.Process(target=playsound, args=("alarmFile.mp3",))
            
            self.update.setText("Ringing Alarm....")
            self.p.start()
            
            self.AlarmPlaying=1
            
            file = open("lastringtime.txt", "w") 
            file.write(str(int(datetime.now().timestamp())))
            
        else:
            self.AlarmPlaying=0
            self.update.setText("Suspicious Activity Found but Last Alarm rang in less than 15 mins. So, Alarm will not ring again")
            QtCore.QTimer.singleShot(10000, lambda: self.update.setText("Analyzing..."))
            
    def terminateAlarm(self):
        if self.AlarmPlaying==0:
            self.update.setText("No Alarm is Ringing") # if alarm is not ringing and button is clicked 
            QtCore.QTimer.singleShot(10000, lambda: self.update.setText("Analyzing..."))
        else:
            self.p.terminate()
            self.update.setText("Alarm stopped..")
            QtCore.QTimer.singleShot(10000, lambda: self.update.setText("Analyzing..."))
    
            
    def FindFeedTimestamp(self,predictionList,timestampList):
        print(predictionList)
        print(timestampList)

        finalTimestamp = []
        start = end = -1
        for i in range(len(predictionList)):
            if (predictionList[i]=="Burglary" or predictionList[i]=="Theft" or predictionList[i]=="Violence") and  i!=len(predictionList)-1:
                if start == -1:
                    start = i
                    end = i
                else:
                    end = i
            else:
                if start != end:
                    finalTimestamp.append(str(timestampList[start])+" , "+str(timestampList[end]))
                start = end = -1
                
        if finalTimestamp:

            return ('Suspicious Activity Found !!! Please refer to the following timestamps to check the duration of such activities\n')+str(finalTimestamp)
        
        else:
            self.update.setText('No Suspicious Activity found in Video !!')
            return ('No Suspicious Activity found in Video')

    def VideoFeedAnalysis(self):
        category =["Burglary","Normal","Theft","Non violence", "Violence"]
        frames = []
        countSus = 0
        frame_count = 0

        font=cv2.FONT_HERSHEY_SIMPLEX

        predictionList,timestampList,frames1 = [],[],[]
        cv2.namedWindow ("Analyzing Your Video.... Please Wait !!!", 0);
        cv2.resizeWindow("Analyzing Your Video.... Please Wait !!!", 640,480)
        cv2.moveWindow("Analyzing Your Video.... Please Wait !!!", 700,30)
        try:
            capture = cv2.VideoCapture(0)
            while (capture.isOpened()):
                ret, frame = capture.read()
                # Bail out when the video file ends
                #QtCore.QTimer.singleShot(20000, lambda: self.update.setText("Analyzing..."))

                if not ret:
                    break

                F=frame

                frame = cv2.resize(frame, (35,35))
            # Save each frame of the video to a list
                frame_count += 1

                frames.append(frame)

                if frame_count < 40:
                    continue # capture frames until you get the required number for sequence
                else:
                    frame_count = 0
            # For each frame, extract feature and prepare it for classification
                prediction = model.predict(np.expand_dims(frames, axis=0))
                max_index = prediction[0].argmax(axis=0) 
                #print(category[max_index])
                if category[max_index]=="Violence" or category[max_index]=="Burglary" or category[max_index]=="Theft":
                    countSus +=1
                else:
                    countSus =0

                cv2.putText(F, str(category[max_index]), (50,50), font, 2, (0, 255, 255), 3, cv2.LINE_4)

                frames1.append(F)

                #####################################################################

                for i in frames1:

                    if category[max_index]=="Violence" or category[max_index]=="Burglary" or category[max_index]=="Theft":

                        i = cv2.copyMakeBorder(i, 20, 20, 20, 20, cv2.BORDER_CONSTANT, None, [0,0,255])
                    else:

                        i = cv2.copyMakeBorder(i, 20, 20, 20, 20, cv2.BORDER_CONSTANT,None, [0,255,0])


                    cv2.imshow('Analyzing Your Video.... Please Wait !!!',i)


                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        
                        capture.release()

                        break
                predictionList.append(category[max_index])
                s = datetime.now()
                dt_string = s.strftime("%d/%m/%Y %H:%M:%S")
                timestampList.append(dt_string)
                frames = []
                frames1 = []
                if countSus > 3:
                    self.update.setText("Suspicious activity detected")
                    self.StopAlarm.show()
                    self.ringAlarm()
                    countSus = 0

        except Exception as e:
            print(str(e))
        finally:
            capture.release()
            cv2.destroyAllWindows()
        capture.release()

        return self.FindFeedTimestamp(predictionList,timestampList)