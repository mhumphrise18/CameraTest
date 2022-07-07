import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

#This will read the input image
img = cv2.imread('/Users/dmc/Desktop/CameraTest-1/OpenCV_Image_0.png')

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

faces = face_cascade.detectMultiScale(gray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x + w, y+h), (255, 0,0) , 2)

cv2.imshow('Image Detect', img)
cv2.waitKey()
