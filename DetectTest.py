import cv2
import ctypes
#import sys


#sys.path.append('/usr/local/lib/python3.9/site-packages')
#cascPath = sys.argv[1]
#This will load the cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

video = cv2.VideoCapture(0)
img_counter = 0

while True: 

    return_value, frame = video.read()
#If you are unable to show frame
    if not return_value:
        print("failed to grab frame")
        break
#Displays the Frame
    #cv2.imshow("Detect Face", frame)
    #print("Successful frame grab")
    #return_value, frame = video.read()
    
## This will convert the video into a grayscale to be able to detect better
    HSV = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)

#this will then start the facial detection
    face = face_cascade.detectMultiScale(HSV, 1.3, 5)


#This will display the rectangle around the face once detected
    for (x, y, w, h) in face:
       cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 6)

    #cv2.waitKey(0)
#This will display the final product
    cv2.imshow('Face ID', frame)

    k=cv2.waitKey(1)
    if k & 0xFF == ord('q'): # q to actually quit the program
        break  
    elif k%256==32:
        def mbox(title, text,style):
            return ctypes.MessageBoxW(0, text, title, style)
       
    #Take a picture using the Space Bar
        img_name = "OpenCV_Image_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter+=1
        cv2.waitKey(0) # This will unfreeze the frame and let you continue to take pictures

video.release()
cv2.destroyAllWindows()
