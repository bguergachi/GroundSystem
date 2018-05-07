import sys,os,time,math


class DataSave:
    def __init__(self):
        self.__telemetry = open(os.path.dirname(os.path.realpath(__file__)) + "/../DataFiles/telemetry.txt", "w")
        self.__csv = open(os.path.dirname(os.path.realpath(__file__))+"/../DataFiles/telemetry.csv","w")
        self.__altitude = open(os.path.dirname(os.path.realpath(__file__))+"/../DataFiles/altitude.csv","w")
        self.__pressure = open(os.path.dirname(os.path.realpath(__file__)) + "/../DataFiles/pressure.csv","w")
        self.__distance = open(os.path.dirname(os.path.realpath(__file__)) + "/../DataFiles/IRdistance.csv","w")
        self.__temperature = open(os.path.dirname(os.path.realpath(__file__)) + "/../DataFiles/temperature.csv", "w")
        self.__acceleration = open(os.path.dirname(os.path.realpath(__file__)) + "/../DataFiles/acceleration.csv", "w")

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

    def addToTemperature(self, dataObj):
        self.__temperature.write(time.time())
        self.__temperature.write("," + dataObj.getOnIndex(12))
        self.__temperature.write("\n")

    def addToAcceleration(self, dataObj):
        self.__acceleration.write(time.time())
        self.__acceleration.write("," + str(math.sqrt(dataObj.getOnIndex(5)**2 + dataObj.getOnIndex(6)**2 + dataObj.getOnIndex(7)**2)))
        self.__acceleration.write("\n")


if __name__ == '__main__':
    save = DataSave()
    save.addToTelemetry("Hello world!")
