from tkinter import *
import tkinter.font as tkfont
from time import sleep
import os,sys,random
from PIL import ImageTk,Image
import time


'''

    This class is used to display the main window

'''
# resolution of the screen
height = 480
width = 320
statusBackGround = 'cyan'





class Display:
    # ***************** Instantiate *****************
    def __init__(self, master):
        self.__master = master
        # Set window parameters
        self.__master.resizable(width=False, height=False)
        self.__master.geometry('{}x{}'.format(height, width))
        #To make window borderless
        #master.overrideredirect(True)

        #Variables for time values
        #self.__currentTime = StringVar()
        #self.__lastMesgTime = StringVar()

        self.__time = Label(self.__master)

        self.printLabel()
        self.getTime()
        self.statusBar()
        self.SettingsImageButtons()
        self.scrollButtons()







    # ***************** Print the time label *****************

    def printLabel(self):
        # Print label of time and time of last received message
        self.__time.config(bd=1, relief=SUNKEN,width = 60)
        self.__time.pack_propagate(False)
        self.__time.pack(side=TOP, anchor=W)

        #testFrame = Frame(self.__master, height=250, width=422,bg="white")
        #testFrame.place(x=2,y=25)





    # ***************** All descriptive status data *****************

    def statusBar(self):
        # Main frame
        status = Frame(self.__master)
        status.pack(side=BOTTOM, fill="x")

        # Frame with map information
        mapCoordinates = Frame(status, bg=statusBackGround, height=70, width=height / 3 - 4)
        mapCoordinates.pack(side=LEFT, pady=2, padx=2)
        mapCoordinates.pack_propagate(False)

        # Frame containing timer information and separation status
        statusStopWatch = Frame(status, bg=statusBackGround, height=70, width=height / 3 - 4)
        statusStopWatch.pack(side=LEFT, pady=2, padx=2)
        statusStopWatch.pack_propagate(False)

        # Frame containing altitude and pressure information
        altitudePressure = Frame(status, bg=statusBackGround, height=70, width=height / 3 - 4)
        altitudePressure.pack(side=LEFT, pady=2, padx=2)
        altitudePressure.pack_propagate(False)

        #Load compass image and render image
        load = Image.open("compass.png")
        load.thumbnail(size = (50,50))
        render = ImageTk.PhotoImage(load)

        #Paint compass image in label with parent being frame with map information
        img = Label(mapCoordinates,image = render,bg=statusBackGround)
        img.image = render
        img.pack(side=LEFT,anchor=W,pady=2,padx=8)

        #Set text label with coordinates with parent being frame with map information
        latitude_longitude = Label(mapCoordinates, text = self.getLatitude()+",\n"+self.getLongitude(),bg="cyan",fg="black")
        #latitude_longitude.bind("<Button-1>", self.__currentTime = "Hello")
        latitude_longitude.pack(side=LEFT,anchor=W,padx=8)

        #Paint stopwatch timer
        stopWatch = Label(statusStopWatch, text = self.getStopWatch(),bg = statusBackGround,fg="black")
        stopWatch.config(font=("times",20))
        stopWatch.pack(side=TOP,anchor=N)

        #Paint status indication for separation
        statusFlag = Label(statusStopWatch,text="status",bg = statusBackGround,fg = self.getStatusFlag())
        statusFlag.config(font=("times",15))
        statusFlag.pack(side=TOP,anchor=S)

        #Paint label of altitude or pressure value
        altitude_pressure = Label(altitudePressure, text=self.getAltitudePressureData() + "m", bg = statusBackGround)
        altitude_pressure.config(font=("times,20"))
        altitude_pressure.pack(side = TOP,anchor=N)

        #Paint descriptive label of data
        title_of_data = Label(altitudePressure,text=self.getAltitudePressureTitle(),bg = statusBackGround)
        title_of_data.config(font=("times",20))
        title_of_data.pack(side=TOP)


    def SettingsImageButtons(self):
        #Settings button built as a canvas
        textFont = tkfont.nametofont("TkDefaultFont")
        settingsLabel = "Settings"
        settingsCanvas = Canvas(self.__master, height=(width-78)/2-4, width=35, background="SystemButtonFace", borderwidth=2,
                           relief="raised")
        settingsCanvas.create_text((15, (width-78)/4-15), angle="90", anchor="ne", text=settingsLabel, fill="SystemButtonText", font=textFont)
        settingsCanvas.bind("<ButtonPress-1>", lambda ev: ev.widget.configure(relief=SUNKEN))
        settingsCanvas.bind("<ButtonRelease-1>", lambda ev: ev.widget.configure(relief=RAISED))
        settingsCanvas.place(x=height-40,y=0)

        #Images button built as a canvas
        ImageLabel = "Images"
        Imagecanvas = Canvas(self.__master, height=(width - 78) / 2-4, width=35, background="SystemButtonFace", borderwidth=2,
                        relief="raised")
        Imagecanvas.create_text((15, (width - 78) / 4-15), angle="90", anchor="ne", text=ImageLabel, fill="SystemButtonText",
                           font=textFont)
        Imagecanvas.bind("<ButtonPress-1>", lambda ev: ev.widget.configure(relief=SUNKEN))
        Imagecanvas.bind("<ButtonRelease-1>", lambda ev: ev.widget.configure(relief=RAISED))
        Imagecanvas.place(x=height-40,y=(width-78)/2+2)


    def scrollButtons(self):
        pass



    #****************** Methods used to get data **************

    def getLatitude(self):
        return "43.380379"

    def getLongitude(self):
        return "-79.732410"

    def getTime(self):

        ## 12 hour format ##
        currentTime = time.strftime("%I:%M:%S")# Current time to display
        lastMesgTime =str(random.randint(0, 24)) + ":" + str(random.randint(0, 60)) + ":" + str(
            random.randint(0, 60))  # Time of last message
        self.__time.config(text="Time:  " + currentTime + "\t\t\t" + "Time of Last Message:  " + lastMesgTime)
        self.__master.after(1000,self.getTime)

    def getStopWatch(self):
        return "01:23.1"

    def getStatusFlag(self):
        return "red"

    def getAltitudePressureData(self):
        return "473.1"

    def getAltitudePressureTitle(self):
        return "Altitude"




root = Tk()
display = Display(root)
root.mainloop()







