import ctypes
from mailbox import mboxMessage
import cv2
import numpy as np

####### I NEED TO FIX Pulling in a video ###########

# Code to record a 10sec video
video = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#width = int(video.get(cv2.VIDEO_PROP_FRAME_WIDTH, 1000))
#height = int(video.get(cv2.VIDEO_PROP_FRAME_HEIGHT, 600))
output = cv2.VideoWriter('output.mov', fourcc , 20.0, (400,400))

vid_count = 0
k=cv2.waitKey(1)

while (video.isOpened()):

    #capture the video frame
    return_value, frame = video.read()

    #If you are unable to show frame
    if not return_value:
        print("failed to grab frame")
        break

    if return_value == True:
        output.write(cv2.cvtColor(frame, cv2.COLOR_RGB2HSV))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Escape hit, closing time now...")
        break
    elif k%256==32:
        def mbox(title, text, style):
            return ctypes.MessageBoxW(0, text, title, style)

        cv2.imshow('frame', frame)
        vid_name = "OpenCV_Video_{}.mp4".format(vid_count)
        cv2.imwrite(vid_name, frame)
        print("{} written!".format(vid_name))
        vid_count+=1
        cv2.waitKey(0)
        break

    
    #Display the frame
    #cv2.imshow('Video frame', frame)

    
    #if k%256 ==27:
        #Closing the program using the ESC key
        #print("Escape hit, closing time now...")
        #break

    #video.release()
    #output.release()
    #cv2.destroyAllWindows()