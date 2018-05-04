import sys,os, time


class DataSave:
    def __init__(self):
        self.__telemetry = open(os.path.dirname(os.path.realpath(__file__)) + "/../DataFiles/telemetry.txt", "w")
        self.__csv = open(os.path.dirname(os.path.realpath(__file__))+"/../DataFiles/telemetry.csv","w")
        self.__altitude = open(os.path.dirname(os.path.realpath(__file__))+"/../DataFiles/altitude","w")
        self.__pressure = open(os.path.dirname(os.path.realpath(__file__)) + "/../DataFiles/pressure","w")
        self.__distance = open(os.path.dirname(os.path.realpath(__file__)) + "/../DataFiles/IRdistance","w")
        self.__battery = open(os.path.dirname(os.path.realpath(__file__)) + "/../DataFiles/battery","w")

    def addToTelemetry(self,string):
        self.__telemetry.write(string)

    def addToCSV(self,dataObj):
        self.__csv.write(time.time())
        for i in range(0,15):
            self.__csv.write(","+dataObj.getOnIndex(i))
        self.__csv.write("\n")

    def addToAltitude(self,dataObj):
        self.__altitude.write(time.time())
        self.__altitude.write(","+dataObj.getOnIndex(4))
        self.__altitude.write("\n")

    def addToPressure(self,dataObj):
        self.__pressure.write(time.time())
        self.__pressure.write(","+dataObj.getOnIndex(12))
        self.__pressure.write("\n")

    def addToDistance(self,dataObj):
        self.__distance.write(time.time())
        self.__distance.write(","+dataObj.getOnIndex(15))
        self.__distance.write("\n")

    def addToBattery(self,dataObj):
        self.__battery.write(time.time())
        self.__battery.write(","+dataObj.getOnIndex(13))
        self.__battery.write("\n")


if __name__ == '__main__':
    save = DataSave()
    save.addToTelemetry("Hello world!")
