import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('../cv_haarcascades/haarcascade_frontalface_default.xml')
body_cascade = cv2.CascadeClassifier('../cv_haarcascades/haarcascade_fullbody.xml')

cam = cv2.VideoCapture(0)

while True:

	ret, frame = cam.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
	  frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
	
	bodies = body_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in bodies:
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

	cv2.imshow('ImageWindow',frame)
	cv2.waitKey(1)
	
cv2.destroyAllWindows()
