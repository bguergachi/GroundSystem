from tkinter import *
from time import sleep
import os,sys,random
from PIL import ImageTk,Image

'''

    This class is used to display the main window

'''
# resolution of the screen
height = 480
width = 320





class Display:
    # *****************Instantiate*****************
    def __init__(self, master):
        self.__master = master
        # Set window parameters
        self.__master.resizable(width=False, height=False)
        self.__master.geometry('{}x{}'.format(height, width))
        # master.overrideredirect(True)

        self.printLabel()
        self.statusBar()
        self.__master.after(200,lambda: self)




    # *****************Print the time label*****************
    def printLabel(self):
        # Print label of time and time of last received message
        time = Label(self.__master,
                     text="Time:  " + self.getTime()[0] + "\t\t\t" + "Time of Last Message:  " + self.getTime()[1],
                     bd=1, relief=SUNKEN)
        time.pack(side=TOP, anchor=W)





    # *****************All descriptive status data *****************
    def statusBar(self):
        # Main frame
        status = Frame(self.__master)
        status.pack(side=BOTTOM, fill="x")

        # Frame with map information
        mapCoordinates = Frame(status, bg="cyan", height=70, width=480 / 3 - 4)
        mapCoordinates.pack(side=LEFT, pady=2, padx=2)
        mapCoordinates.pack_propagate(False)

        # Frame containing timer information and separation status
        statusStopWatch = Frame(status, bg="cyan", height=70, width=480 / 3 - 4)
        statusStopWatch.pack(side=LEFT, pady=2, padx=2)
        statusStopWatch.pack_propagate(False)

        # Frame containing altitude and pressure information
        altitudePressure = Frame(status, bg="cyan", height=70, width=480 / 3 - 4)
        altitudePressure.pack(side=LEFT, pady=2, padx=2)
        altitudePressure.pack_propagate(False)

        load = Image.open("compass.png")

        load.thumbnail(size = (50,50))
        render = ImageTk.PhotoImage(load)

        img = Label(mapCoordinates,image = render,bg="cyan")
        img.image = render
        img.pack(side=LEFT,anchor=W,pady=2,padx=8)



        latitude_longitude = Label(mapCoordinates, text = self.getLatitude()+",\n"+self.getLongitude(),bg="cyan",fg="black")
        latitude_longitude.pack(side=LEFT,anchor=W,padx=8)


    def getLatitude(self):
        return "43.380379"

    def getLongitude(self):
        return "-79.732410"


    def getTime(self):
        currentTime = str(random.randint(0, 24)) + ":" + str(random.randint(0, 60)) + ":" + str(
            random.randint(0, 60))  # Current time to display
        lastMesgTime = str(random.randint(0, 24)) + ":" + str(random.randint(0, 60)) + ":" + str(
            random.randint(0, 60))  # Time of last message
        return [currentTime, lastMesgTime]


root = Tk()
display = Display(root)
root.mainloop()



