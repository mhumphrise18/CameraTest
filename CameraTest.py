#Code to capture, filter and face ID from the Mac's Camera

#This will import the openCV to enable the code to run
import ctypes
from mailbox import mboxMessage
#from tkinter.tix import PopupMenu
import cv2

#this creating the value for the camera and calling on the first camera on the computer
camera =cv2.VideoCapture(0)
video = cv2.VideoCapture(0)

#Variable(s)
img_counter =0

#Camera Loop
while True:
    #Creates the Frame
    return_value, frame = camera.read()
    #If you are unable to show frame
    if not return_value:
        print("failed to grab frame")
        break
    #Displays the Frame
    cv2.imshow("Test Pic", frame)

    #for playing?
    k=cv2.waitKey(1)
    if k%256 ==27:
        #Closing the program using the ESC key
        print("Escape hit, closing time now...")
        break
    elif k%256==32:
        def mbox(title, text,style):
            return ctypes.MessageBoxW(0, text, title, style)
       
        #Take a picture using the Space Bar
        img_name = "OpenCV_Image_{}.png".format(img_counter)
        #for i in range(10):
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter+=1
        cv2.waitKey(0)
        break
    if k%256 ==97: 
        #change the filter using the 'a' Key
        #Changing from RGB to HSV
        img_name = "OpenCV_FilterChangeImage_{}.png".format(img_counter)
        HSV =cv2.cvtColor(frame,cv2.COLOR_RGB2HSV)
        print(HSV.shape)
        print("{} written!".format(img_name))
        h, s, v =cv2.split(HSV)
        cv2.imshow("HSV Image", s)
        cv2.waitKey(0)

        camera.release()
        cv2.destroyAllWindows()
        ##ITS FAILING TO GRAB THE BOTH FRAME
        #return_value, frame = camera.read()
        #cv2.imshow("Test Pic", frame)

# Code to record a 10sec video
video=cv2.VideoCapture(0)
vid_counter = 0
while(True):

    #capture the video frame
    ret, frame = video.read()

    #Display the frame
    cv2.imshow('Video frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        vid_name = "OpenCV_Video_{}.mov".format(vid_counter)
        cv2.imwrite(vid_name, frame)
        print("{} written!".format(vid_name))
        vid_counter +=1
        cv2.waitkey(0)
        break

    video.release()
    cv2.destroyAllWindows()
