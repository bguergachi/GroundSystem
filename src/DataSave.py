import sys,os


class DataSave:
    def __init__(self):
        self.__telemetry = open(os.path.dirname(os.path.realpath(__file__))+"/../DataFiles/telemetry.txt","w")


    def addToTelemetry(self,string):
        self.__telemetry.write(string)


if __name__ == '__main__':
    save = DataSave()
    save.addToTelemetry("Hello world!")