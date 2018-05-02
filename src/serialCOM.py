import serial
import threading
import time, sys
import src.DataSave as DataSave



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

    def getOnIndex(self,index):
        if index == 0:
            return self.gpsLat
        elif index == 1:
            return self.gpsLong
        elif index == 2:
            return self.gpsSpeed
        elif index == 3:
            return self.gpsTime
        elif index == 4:
            return self.gpsAlt
        elif index == 5:
            return self.accelX
        elif index == 6:
            return self.accelY
        elif index == 7:
            return self.accelZ
        elif index == 8:
            return self.accelX1
        elif index == 9:
            return self.accelY2
        elif index == 10:
            return self.accelZ2
        elif index == 11:
            return self.pressAlt
        elif index == 12:
            return self.pressTemp
        elif index == 13:
            return self.tempBattery
        elif index == 14:
            return self.IRdistance

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
            self.IRdistance = value




class SerialCom:
    def __init__(self,baud,port):
        self.dataList = Data()
        self.lock = threading.Lock()
        self.__baud = baud
        self.__port = port
        self.__serial = serial.Serial('/dev/'+self.__port, baudrate=self.__baud,
                                      parity=serial.PARITY_NONE,
                                      stopbits=serial.STOPBITS_ONE,
                                      bytesize=serial.EIGHTBITS)
        self.__fileSaver = DataSave()

    def startThread(self):
        t = threading.Thread(target=self.__start, args= self.dataList)
        t.daemon = True
        t.start()
        
    def __start(self,dataList):
        #i = 0
        print("Starting to read")
        while True:
            #i += 1
            #print("\n",i)  
            data = self.__serial.read().decode('utf-8')
            self.__fileSaver.addToTelemetry(data)
            #print(data)
            #sys.exit()
            if data=='\n':
                print("Starting")
                for n in range(0, 15):
                    with self.lock:
                        dataList.setOnIndex(n, self.__readline())
                    #print(n)
        self.__fileSaver.addToCSV(dataList)


            
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
        self.__serial = serial.Serial('/dev/'+self.__port, baudrate=self.__baud,
                                      parity=serial.PARITY_NONE,
                                      stopbits=serial.STOPBITS_ONE,
                                      bytesize=serial.EIGHTBITS)
        

if __name__ == '__main__':
    SerialCom = SerialCom(57600,'ttyS0')
