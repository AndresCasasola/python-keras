import cv2

cam = cv2.VideoCapture(0)
for i in range(10):
    ret, frame = cam.read()
    cv2.imwrite('image'+str(i)+'.png', frame)
del(cam)
