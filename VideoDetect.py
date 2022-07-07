import cv2
import numpy

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

## Need to fix reading the .mov file in order for it to work!
vid = cv2.VideoCapture('/Users/dmc/Desktop/CameraTest-1/TestVideo.mov')

while True:
    _, img = vid.read()
    HSV = cv2.cvtColor(vid, cv2.COLOR_RGB2HSV)

    faces = face_cascade.detectMultiScale(HSV, 1.1, 4)

    for (x, y,w, h) in faces:
        cv2.circle(vid, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow("VideoDetect", vid)

    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

vid.release()
