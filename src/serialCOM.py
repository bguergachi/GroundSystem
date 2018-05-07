import serial
import threading
import time, sys
#sys.path.append("..")
import src.DataSave as DataSave


#Class used to store temporally all values
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
        self.accelY1 = 0
        self.accelZ1 = 0
        self.pressAlt = 0
        self.pressTemp = 0
        self.tempBattery = 0
        self.IRdistance = 0
        self.pressure = 0

    #Get function to get value of stored data
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
            return self.accelY1
        elif index == 10:
            return self.accelZ1
        elif index == 11:
            return self.pressAlt
        elif index == 12:
            return self.pressTemp
        elif index == 13:
            return self.tempBattery
        elif index == 14:
            return self.IRdistance
        elif index == 15:
            return self.pressure

    #set function to set value of data
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
            self.accelY1 = value
        elif index == 10:
            self.accelZ1 = value
        elif index == 11:
            self.pressAlt = value
        elif index == 12:
            self.pressTemp = value
        elif index == 13:
            self.tempBattery = value
        elif index == 14:
            self.IRdistance = value
        elif index == 15:
            self.pressure = value



#Class to start serial communication
class SerialCom:
    

    
    def __init__(self,baud,port):
        #Create new data object to start saving data
        self.dataList = Data()
        #Create lock for threading
        self.lock = threading.Lock()
        #Set communication settings
        self.__baud = baud
        self.__port = port
        self.__serial = serial.Serial('/dev/'+self.__port, baudrate=self.__baud,
                                      parity=serial.PARITY_NONE,
                                      stopbits=serial.STOPBITS_ONE,
                                      bytesize=serial.EIGHTBITS)

        self.lastTimeDataReceived = time.strftime("%I:%M:%S")
        self.lastTimeDataRecivedNumber = time.time()
        self.__fileSaver = DataSave.DataSave()
        if __name__ == '__main__':
            self.__start(self.dataList)

    def startThread(self,dataList):
        print("Started Thread")
        t = threading.Thread(target=self.__start, args= (dataList,))
        t.daemon = True
        t.start()
        
    def __start(self,dataList):
        #Start reading data
        print("Starting to read")
        while True:
            data = self.__serial.read().decode('utf-8')
            #save data to txt file
            self.__fileSaver.addToTelemetry(data)
            if data=='\n':
                print("Starting")
                for n in range(0, 16):
                    with self.lock:
                        self.dataList.setOnIndex(n, self.__readline())
                    #print(n)

            #Save Graph data to files
            self.__fileSaver.addToCSV(dataList)
            self.__fileSaver.addToAltitude(dataList)
            self.__fileSaver.addToPressure(dataList)
            self.__fileSaver.addToDistance(dataList)
            self.__fileSaver.addToTemperature(dataList)
            self.__fileSaver.addToAcceleration(dataList)


    #This function will data char for what ever amount is needed
    def __readline(self):
        rv = ""
        while True:
            ch = self.__serial.read().decode('utf-8')
            if ch=='\r':
                print(rv)
                self.lastTimeDataReceived = time.strftime("%I:%M:%S")
                self.lastTimeDataRecivedNumber = time.time()
                return float(rv)
            rv += ch

            
            #recived
    #public api to change port
    def setPort(self,port):
        self.__port = port
        self.__serial = serial.Serial('/dev/'+self.__port, baudrate=self.__baud,
                                      parity=serial.PARITY_NONE,
                                      stopbits=serial.STOPBITS_ONE,
                                      bytesize=serial.EIGHTBITS)
        

if __name__ == '__main__':
    SerialCom = SerialCom(57600,'ttyS0')
