import sys,os, time


class DataSave:
    def __init__(self):
        self.__telemetry = open(os.path.dirname(os.path.realpath(__file__)) + "/../DataFiles/telemetry.csv", "w")
        self.__csv = open(os.path.dirname(os.path.realpath(__file__))+"/../DataFiles/telemetry.csv","w")

    def addToTelemetry(self,string):
        self.__telemetry.write(string)

    def addToCSV(self,dataObj):
        self.__csv.write(time.time())
        for i in range(0,16):
            self.__csv.write(","+dataObj.getOnIndex(i))
        self.__csv.write("\n")


if __name__ == '__main__':
    save = DataSave()
    save.addToTelemetry("Hello world!")