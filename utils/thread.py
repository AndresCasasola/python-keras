
import threading
from threading import Thread

def MyThread (arg):
	print("Hello, i am a thread! :)")

thread = Thread(target = MyThread, args = (10, ))
thread.start()

thread.join()
