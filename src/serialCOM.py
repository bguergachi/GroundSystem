import serial

class SerialCom:
    def __init__(self,port):
        self.__port = port

    def setPort(self,port):
        self.__port = port

