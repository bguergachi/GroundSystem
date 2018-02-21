import serial
import threading
from queue import Queue
import time

print_lock = threading.Lock()

class SerialCom:
    def __init__(self,port):
        self.__port = port

    def setPort(self,port):
        self.__port = port

if __name__ == '__main__':
    SerialCom = SerialCom(9600)