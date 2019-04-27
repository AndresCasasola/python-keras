import cv2
import io
import socket
import struct
import time
import pickle
import zlib

# Welcome message
print('\nWelcome to PythonCam client!')

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

# ----- Socket config and connect ----- #
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Client connecting to IP: {} PORT: {}'.format(HOST, PORT))
client_socket.connect((HOST, PORT))
print('Connected')
connection = client_socket.makefile('wb')

img_counter = 0
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

data = b""
payload_size = struct.calcsize(">L")

print('Receiving...')
time.sleep(2)
while True:
	while len(data) < payload_size:
		#print("Recv: {}".format(len(data)))
		data += client_socket.recv(4096)

	#print("Done Recv: {}".format(len(data)))
	packed_msg_size = data[:payload_size]
	data = data[payload_size:]
	msg_size = struct.unpack(">L", packed_msg_size)[0]
	#print("msg_size: {}".format(msg_size))
	while len(data) < msg_size:
		data += client_socket.recv(4096)
	frame_data = data[:msg_size]
	data = data[msg_size:]

	frame=pickle.loads(frame_data, fix_imports=True, encoding="bytes")
	frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
	cv2.imshow('ImageWindow',frame)
	cv2.waitKey(1)
