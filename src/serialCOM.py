import serial
import threading
import time, sys
#sys.path.append("..")
import src.DataSave as DataSave, src.LEDfunc as LEDfunc


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
        self.gpsDate = 0

    #Get function to get value of stored data
    def getOnIndex(self,index):
        if index == 0:
            return self.IRdistance
        elif index == 1:
            return self.pressTemp
        elif index == 2:
            return self.pressure
        elif index == 3:
            return self.pressAlt
        elif index == 4:
            return self.tempBattery
        elif index == 5:
            return self.gpsLat
        elif index == 6:
            return self.gpsLong
        elif index == 7:
            return self.gpsTime
        elif index == 8:
            return self.gpsDate
        elif index == 9:
            return self.gpsSpeed
        elif index == 10:
            return self.accelX
        elif index == 11:
            return self.accelY
        elif index == 12:
            return self.accelZ
        elif index == 13:
            return self.accelX1
        elif index == 14:
            return self.accelY1
        elif index == 15:
            return self.accelZ1

    #set function to set value of data
    def setOnIndex(self,index,value):
        if index == 0:
            self.IRdistance = value
        elif index == 1:
            self.pressTemp = value
        elif index == 2:
            self.pressure = value
        elif index == 3:
            self.pressAlt = value
        elif index == 4:
            self.tempBattery = value
        elif index == 5:
            self.gpsLat = value
        elif index == 6:
            self.gpsLong = value
        elif index == 7:
            self.gpsTime = value
        elif index == 8:
            self.gpsDate = value
        elif index == 9:
            self.gpsSpeed = value
        elif index == 10:
            self.accelX = value
        elif index == 11:
            self.accelY = value
        elif index == 12:
            self.accelZ = value
        elif index == 13:
            self.accelX1 = value
        elif index == 14:
            self.accelY1 = value
        elif index == 15:
            self.accelZ1 = value



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
            if data=='\a':
                print("Starting")
                with self.lock:
                    self.dataList.setOnIndex(0, self.__readline(self.dataList.getOnIndex(0)))
            elif data == '\b':
                print("Starting")
                with self.lock:
                    self.dataList.setOnIndex(1, self.__readline(self.dataList.getOnIndex(1)))
            elif data == '\f':
                print("Starting")
                with self.lock:
                    self.dataList.setOnIndex(2, self.__readline(self.dataList.getOnIndex(2)))
            elif data == '\n':
                print("Starting")
                with self.lock:
                    self.dataList.setOnIndex(3, self.__readline(self.dataList.getOnIndex(3)))
            elif data == '\t':
                print("Starting")
                with self.lock:
                    self.dataList.setOnIndex(4, self.__readline(self.dataList.getOnIndex(4)))
            elif data == '\v':
                print("Starting")
                with self.lock:
                    self.dataList.setOnIndex(5, self.__readline(self.dataList.getOnIndex(5)))
            elif data == '\\':
                print("Starting")
                with self.lock:
                    self.dataList.setOnIndex(6, self.__readline(self.dataList.getOnIndex(6)))
            elif data == '^':
                print("Starting")
                with self.lock:
                    self.dataList.setOnIndex(7, self.__readline(self.dataList.getOnIndex(7)))
            elif data == '\'':
                print("Starting")
                with self.lock:
                    self.dataList.setOnIndex(8, self.__readline(self.dataList.getOnIndex(8)))
            elif data == '\"':
                print("Starting")
                with self.lock:
                    self.dataList.setOnIndex(9, self.__readline(self.dataList.getOnIndex(9)))
            elif data == '~':
                print("Starting")
                with self.lock:
                    self.dataList.setOnIndex(10, self.__readline(self.dataList.getOnIndex(10)))
            elif data == '@':
                print("Starting")
                with self.lock:
                    self.dataList.setOnIndex(11, self.__readline(self.dataList.getOnIndex(11)))
            elif data == '#':
                print("Starting")
                with self.lock:
                    self.dataList.setOnIndex(12, self.__readline(self.dataList.getOnIndex(12)))
            elif data == '$':
                print("Starting")
                with self.lock:
                    self.dataList.setOnIndex(13, self.__readline(self.dataList.getOnIndex(13)))
            elif data == 'Y':
                print("Starting")
                with self.lock:
                    self.dataList.setOnIndex(14, self.__readline(self.dataList.getOnIndex(14)))
            elif data == 'Z':
                print("Starting")
                with self.lock:
                    self.dataList.setOnIndex(15, self.__readline(self.dataList.getOnIndex(15)))

            #Save Graph data to files
            self.__fileSaver.addToCSV(dataList)
            self.__fileSaver.addToAltitude(dataList)
            self.__fileSaver.addToPressure(dataList)
            self.__fileSaver.addToDistance(dataList)
            self.__fileSaver.addToTemperature(dataList)
            self.__fileSaver.addToAccelerationEx(dataList)
            self.__fileSaver.addToAccelerationIn(dataList)
            self.__fileSaver.addToBatTemperature(dataList)


    #This function will data char for what ever amount is needed
    def __readline(self, old):
        LEDfunc.greenLED(1)
        rv = ""
        while True:
            try:
                ch = self.__serial.read().decode('utf-8')
            except UnicodeDecodeError:
                print("That wasn't a char")
                continue
            if ch=='\r':
                LEDfunc.greenLED(0)
                print(rv)
                self.lastTimeDataReceived = time.strftime("%I:%M:%S")
                self.lastTimeDataRecivedNumber = time.time()
                try:
                    return float(rv)
                except:
                    return old

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
