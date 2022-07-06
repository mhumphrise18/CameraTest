from datetime import datetime as dt
from sys import flags
from tkinter import Frame
import logging as log
import cv2
import sys

sys.path.append('/usr/local/lib/python3.9/site-packages')
cascPath = sys.argv[1]
#This will load the cascade
face_cascade = cv2.CascadeClassifier(cascPath)
log.basicConfig(filename='webcam.log', level=log.INFO)

video = cv2.VideoCapture(0)
#This will read the input video
#vid = cv2.imread('TestVideo.mov')
ANTERIOR = 0


while True: 

#If you are unable to show frame
    if not return_value:
        print("failed to grab frame")
        break
#Displays the Frame
    #cv2.imshow("Detect Face", frame)
    print("Successful frame grab")
    return_value, frame = video.read()
#print(HSV.shape)
#h, s, v = cv2.split(HSV)

#This will convert the video into a grayscale to be able to detect better
    HSV = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)

#this will then start the facial detection
    face = face_cascade.detectMultiScale(
        HSV,
        scalefactor = 1.1,
        minNeighbors = 5,
        minSize = (30,30),
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE
    )

#This will display the rectangle around the face once detected
    for (x, y, w, h) in face:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 2)

    if anterior != len(face):
        anterior = len(face)
        log.info("faces: " +str(len(face))+" at "+str(dt.datetime.now()))



#This will display the final product
    cv2.imshow('video', frame)
#cv2.waitKey()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
