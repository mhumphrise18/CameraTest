import cv2
import ctypes
import numpy as np
#import dlib
#import faceBlendCommon as face
#import sys


#sys.path.append('/usr/local/lib/python3.9/site-packages')
#cascPath = sys.argv[1]
#This will load the cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


img = cv2.imread('/Users/dmc/Desktop/CameraTest-1/OpenCV_Image_0.png')


#while True: 

    #return_value, frame = img.read()
#If you are unable to show frame
 #   if not return_value:
  #      print("failed to grab frame")
   #     break
#Displays the Frame
    #cv2.imshow("Detect Face", frame)
    #print("Successful frame grab")
    #return_value, frame = video.read()
    
## This will convert the video into a grayscale to be able to detect better
HSV = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
## This will detect cirlces within the facial recognition
#HSV_blurred = cv2.blur(HSV, (3,3))
img = cv2.medianBlur(img,5)

#this will then start the facial detection
face = face_cascade.detectMultiScale(HSV, 1.3, 5)
detected_circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 10, param1=50, param2=30, minRadius=0, maxRadius=0)

detected_circles = np.uint16(np.around(detected_circles))
#This will display the rectangle around the face once detected
#for (x, y, w, h) in face:
 #   cv2.rectangle(img_blur, (x,y), (x+w, y+h), (0, 255, 0), 6)


for pt in detected_circles[0, :]:
    a, b, r = pt[0], pt[1], pt[2]
    cv2.circle(HSV, (a, b), r, (0, 0, 255), 2)
    cv2.circle(HSV, (a, b), r, (0, 0, 255), 3)

        #cv2.waitKey(0)
#This will display the final product
    cv2.imshow('Face Iris ID', img)

    #k=cv2.waitKey(1)
    #if k & 0xFF == ord('q'): # q to actually quit the program
     #   break  
    #elif k%256==32:
     #   def mbox(title, text,style):
      #      return ctypes.MessageBoxW(0, text, title, style)
       
 
img.release()
cv2.destroyAllWindows()
