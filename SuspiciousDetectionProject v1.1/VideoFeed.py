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

def ringAlarm():
        if not os.path.isfile('lastringtime.txt'):
            file = open("lastringtime.txt", "w") 
            file.write(str(int(datetime.now().timestamp())))
            f = 1
        else:
            file = open("lastringtime.txt", "r")
            if(int(datetime.now().timestamp())-int(file.read())>900):
                f=1
            else:
                f=0
        if f==1:
            p = multiprocessing.Process(target=playsound, args=("alarmFile.mp3",))
            p.start()
            input("press ENTER to stop playback")
            p.terminate()
        else:
            print("Sus Activity Found but Last Alarm rang in less than 15 mins. Alarm will not ring")
            
def FindFeedTimestamp(predictionList,timestampList):
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
        return ('No Suspicious Activity found in Video')

def VideoFeedAnalysis():
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
            
            
            if not ret:
                break
                
            F=frame
            #frames1.append(frame)
            
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
            print(category[max_index])
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
                ringAlarm()
                countSus = 0

    except Exception as e:
        print(str(e))
    finally:
        capture.release()
        cv2.destroyAllWindows()
    capture.release()
    
    return FindFeedTimestamp(predictionList,timestampList)
