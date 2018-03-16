import serial
import threading
from queue import Queue
import time
import sys



class Data:
    def __init__(self):
        self.gpsLat = 0
        self.gpsLong = 0
        self.gpsSpeed = 0
        self.gpsTime = 0
        self.gpsAlt = 0
        self.accelX = 0
        self.accelY = 0
        self.accelZ = 0
        self.accelX1 = 0
        self.accelY2 = 0
        self.accelZ2 = 0
        self.pressAlt = 0
        self.pressTemp = 0
        self.tempBattery = 0
        self.strainGauge = 0
        self.IRdistance = 0
    
    def setOnIndex(self,index,value):
        if index == 0:
            self.gpsLat = value
        elif index == 1:
            self.gpsLong = value
        elif index == 2:
            self.gpsSpeed = value
        elif index == 3:
            self.gpsTime = value
        elif index == 4:
            self.gpsAlt = value
        elif index == 5:
            self.accelX = value
        elif index == 6:
            self.accelY = value
        elif index == 7:
            self.accelZ = value
        elif index == 8:
            self.accelX1 = value
        elif index == 9:
            self.accelY2 = value
        elif index == 10:
            self.accelZ2 = value
        elif index == 11:
            self.pressAlt = value
        elif index == 12:
            self.pressTemp = value
        elif index == 13:
            self.tempBattery = value
        elif index == 14:
            self.strainGauge = value
        elif index == 15:
            self.IRdistance = value


dataList = Data()

class SerialCom:
    def __init__(self,baud):
        self.__port = 'ttyS0'
        self.__serial = serial.Serial('/dev/'+self.__port, baudrate=baud,
                                      parity=serial.PARITY_NONE,
                                      stopbits=serial.STOPBITS_ONE,
                                      bytesize=serial.EIGHTBITS)
        self.__start()
        
    def __start(self):
        #i = 0
        print("Starting to read")
        while True:
            #i += 1
            #print("\n",i)  
            data = self.__serial.read().decode('utf-8')
            #print(data)
            #sys.exit()
            if data=='\n':
                print("Starting")
                for n in range(0, 16):
                    dataList.setOnIndex(n, self.__readline())
                    #print(n)


            
    def __readline(self):
        rv = ""
        while True:
            
            ch = self.__serial.read().decode('utf-8')
            if ch=='\r':
                print(rv)
                return rv
            rv += ch
            
            

    def setPort(self,port):
        self.__port = port
        self.__serial = serial.Serial('/dev/'+self.__port, baudrate=baud,
                                      parity=serial.PARITY_NONE,
                                      stopbits=serial.STOPBITS_ONE,
                                      bytesize=serial.EIGHTBITS)
        

if __name__ == '__main__':
    SerialCom = SerialCom(57600)
