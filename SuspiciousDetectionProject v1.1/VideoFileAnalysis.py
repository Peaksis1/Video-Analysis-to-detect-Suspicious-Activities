import cv2
import numpy as np
import keras
import tensorflow as tf
import datetime
model =  tf.keras.models.load_model('mymodelmain1.h5')

def FindTimestamp(fps,predictionList):
    startTime = endTime = 0
    timestampList = []
    count = 0
    z = 40
    for i in range(len(predictionList)):
        if (predictionList[i]=="Burglary" or predictionList[i]=="Theft" or predictionList[i]=="Violence") and i!=len(predictionList)-1:
            if startTime == 0:
                startTime = i
                endTime = i
            else:
                endTime = i
                
        else:
            if startTime != endTime:
                seconds = float((z)*startTime / fps)
                start_video_time = str(datetime.timedelta(seconds=seconds))
                seconds = float((z)*endTime / fps)
                end_video_time = str(datetime.timedelta(seconds=seconds))
                timestampList.append(str(str(start_video_time)[:10] +", "+ str(end_video_time)[:10]))
            startTime = 0
            endTime = 0
    if timestampList:
        return ('Suspicious Activity is Found !! \n\nPlease refer to the following timestamps to check the duration of such activities\n\n' + str(timestampList))
    
    else:
        return ('No Suspicious Activity found in Video')

def VideoAnalyzer(video_path):
    category =["Burglary","Normal","Theft","Non violence", "Violence"]
    
    suspicious = ["Burglary","Theft", "Violence"]
    
    frames,frames1,predictionList = [],[],[]
    
    font=cv2.FONT_HERSHEY_SIMPLEX
    frame_count,fps  = 0,0
    
    cv2.namedWindow ("Analyzing Your Video.... Please Wait !!!", 0);
    cv2.resizeWindow("Analyzing Your Video.... Please Wait !!!", 640,480)
    cv2.moveWindow("Analyzing Your Video.... Please Wait !!!", 700,30)

    
    try:
        
        capture = cv2.VideoCapture(video_path)
        
        fps += capture.get(cv2.CAP_PROP_FPS)      
        
        capture = cv2.VideoCapture(video_path)
        
        while (capture.isOpened()):
            
            ret, frame = capture.read()
            
            if not ret: break
            
            F=frame
            
            #frames1.append(frame)
            
            frame = cv2.resize(frame, (35,35))
            
            frame_count += 1
            
            frames.append(frame)
            
            if frame_count < 40: continue
                
            else: frame_count = 0

            
            ################################################################################## PREDICTION ####################
            prediction = model.predict(np.expand_dims(frames, axis=0))
            
            max_index = prediction[0].argmax(axis=0)
            
            #print(category[max_index])
            
            cv2.putText(F, str(category[max_index]), (50,50), font, 2, (0, 255, 255), 3, cv2.LINE_4)
            
            frames1.append(F)
           
            ################################################################################## DISPLAY VIDEO #################
            for i in frames1:
                
                if category[max_index] in suspicious:
                    
                    i = cv2.copyMakeBorder(i, 20, 20, 20, 20, cv2.BORDER_CONSTANT, None, [0,0,255])
                    
                else:
                    
                    i = cv2.copyMakeBorder(i, 20, 20, 20, 20, cv2.BORDER_CONSTANT,None, [0,255,0])
                
                
                cv2.imshow('Analyzing Your Video.... Please Wait !!!',i)
                
                
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    
                    capture.release()
                    
                    break
                    
            predictionList.append(category[max_index])
            
            frames = []
            
            frames1 = []

    except Exception as e: print(str(e))
        
    finally:
        capture.release()
        
        cv2.destroyAllWindows()
        
    return FindTimestamp(fps,predictionList)

