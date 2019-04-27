import socket
import sys
import cv2
import pickle
import numpy as np
import struct ## new
import zlib
import time

# Welcome message
print('\nWelcome to PythonCam server!')

# ----- Selecting IP and PORT ----- #
HOST = input("Enter server IP (empty for default: 127.0.0.1):")
if (HOST == ''):
	HOST='127.0.0.1'
print('Selected: {}'.format(HOST))

PORT = input("Enter Port (empty for default: 5005):\n")
if (PORT == ''):
	PORT=5005
else:
	PORT=int(PORT)
print('Selected: {}'.format(PORT))


cam = cv2.VideoCapture(0)
img_counter = 0
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

# ----- Socket config and connect ----- #
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket created with IP: {} PORT: {}'.format(HOST, PORT))
s.bind((HOST,PORT))
print('Socket bind completed')
s.listen(10)
print('Socket now listening')
conn,addr=s.accept()
print('Client connected with IP: {}'.format(addr))

print('Transmitting...')
time.sleep(2)
while True:
    ret, frame = cam.read()
    result, frame = cv2.imencode('.jpg', frame, encode_param)
#    data = zlib.compress(pickle.dumps(frame, 0))
    data = pickle.dumps(frame, 0)
    size = len(data)


    #print("{}: {}".format(img_counter, size))
    conn.sendall(struct.pack(">L", size) + data)
    img_counter += 1

cam.release()
