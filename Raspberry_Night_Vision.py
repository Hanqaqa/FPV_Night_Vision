import cv2
import sys
import numpy as np
import time

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")    

video_capture = cv2.VideoCapture(0)

def change_res(width, height):
    video_capture.set(3, width)
    video_capture.set(4, height)

#Uncomment the resolution you want to use, the one uncommented is the I used

#change_res(160,90)
#change_res(320,180)                        #16:9
change_res(640,360)                         #16:9

#change_res(1280,720)                       #16:9  
#change_res(640,480)                        #4:3
#change_res(320,240)                        #4:3
oldtime = time.time()

print(oldtime)

while True:
    ret, frame = video_capture.read()
    frame = cv2.flip(frame, -1);             #Refleja la webcam para que parezca un espejo

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,                     #Se usa un 30% de escala en cada paso de la cascada de Haar, si aumento a 1.5 es mas rapido pero menos exhaustivo
        minNeighbors=3,
        maxSize=(50, 50),                  #100, 100 va bien para mas de un metro de dsitancia
        minSize=(15, 15),                      #3, 3 ya no detecta a unos 3 metros
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
    cv2.namedWindow('Video', cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('Video', cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if time.time() - oldtime > 120:
        break

video_capture.release()
cv2.destroyAllWindows()
