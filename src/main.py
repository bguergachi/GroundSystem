from tkinter import *
import tkinter.font as tkfont
from time import sleep
import os,sys,random, socket
sys.path.append("..")
from PIL import ImageTk,Image
import time
import src.GPSMap as GPSMap , src.Status as Status, src.Settings as Settings
import threading
from queue import Queue

'''

    This class is used to display the main window

'''
# resolution of the screen
height = 480
width = 320
statusBackGround = 'cyan'

#Threading options
threadLock = threading.Lock()
queue = Queue()

#Serial options
baudRate = 9600


class Display:
    # ***************** Instantiate *****************
    def __init__(self, master):
        self.__master = master
        # Set window parameters
        self.__master.resizable(width=False, height=False)
        self.__master.geometry('{}x{}'.format(height, width))
        #To make window borderless
        #master.overrideredirect(True)

        self.__mapShowFlag = 0

        self.__placeMainFrame()

        # Load compass image and render image
        load = Image.open(os.path.dirname(os.path.realpath(__file__))+"/../appImages/rocketry.png")
        load.thumbnail(size=(220, 435))
        render = ImageTk.PhotoImage(load)

        self.__img = Label(self.__mainFrame, image=render, bg='light cyan')
        self.__img.image = render
        self.__img.pack()



        self.__printLabel()
        self.__statusBar()
        self.__SettingsImageButtons()
        self.__startDataThread()

    def __startDataThread(self):
        #for x in range(1):
        #    t = threading.Thread(target = threader)
        #    t.daemon = True
        #    t.start()
        pass


    def __placeMainFrame(self):
        self.__mainFrame = Frame(self.__master, height=220, width=435, bg='light cyan')
        self.__mainFrame.pack_propagate(False)
        self.__mainFrame.place(x=4, y=22)



    # ***************** Print the time label *****************

    def __printLabel(self):
        # Print label of time and time of last received message
        self.__time = Label(self.__master)
        self.__time.config(bd=1, relief=SUNKEN,width = 61)
        self.__time.pack_propagate(False)
        self.__time.pack(side=TOP, anchor=W, pady = 1 ,padx =3)
        self.getTime()





    # ***************** All descriptive status data *****************

    def __statusBar(self):
        # Main frame
        status = Frame(self.__master)
        status.pack(side=BOTTOM, fill="x")

        # Frame with map information
        self.__mapCoordinates = Frame(status, bg=statusBackGround, height=70, width=height / 3 - 4)
        self.__mapCoordinates.pack(side=LEFT, pady=2, padx=2)
        self.__mapCoordinates.pack_propagate(False)
        self.__mapCoordinates.bind("<ButtonPress-1>",self.__changeFrameMap)

        # Frame containing timer information and separation status
        self.__statusStopWatch = Frame(status, bg=statusBackGround, height=70, width=height / 3 - 4)
        self.__statusStopWatch.pack(side=LEFT, pady=2, padx=2)
        self.__statusStopWatch.pack_propagate(False)
        self.__statusStopWatch.bind("<ButtonPress-1>",self.__changeFrameStatus)

        # Frame containing altitude and pressure information
        self.__altitudePressure = Frame(status, bg=statusBackGround, height=70, width=height / 3 - 4)
        self.__altitudePressure.pack(side=LEFT, pady=2, padx=2)
        self.__altitudePressure.pack_propagate(False)
        self.__altitudePressure.bind("<ButtonPress-1>",self.__changeFrameAltimeter)

        #Load compass image and render image
        load = Image.open(os.path.dirname(os.path.realpath(__file__))+"/../appImages/compass.png")
        load.thumbnail(size = (50,50))
        render = ImageTk.PhotoImage(load)

        #Paint compass image in label with parent being frame with map information
        self.__img = Label(self.__mapCoordinates,image = render,bg=statusBackGround)
        self.__img.image = render
        self.__img.pack(side=LEFT,anchor=W,pady=2,padx=8)
        self.__img.bind("<ButtonPress-1>",self.__changeFrameMap)

        #Set text label with coordinates with parent being frame with map information
        self.__latitude_longitude = Label(self.__mapCoordinates, text = self.getLatitude()+",\n"+self.getLongitude(),bg="cyan",fg="black")
        #latitude_longitude.bind("<Button-1>", self.__currentTime = "Hello")
        self.__latitude_longitude.pack(side=LEFT,anchor=W,padx=8)
        self.__latitude_longitude.bind("<ButtonPress-1>",self.__changeFrameMap)

        #Paint stopwatch timer
        self.__stopWatch = Label(self.__statusStopWatch, text = self.getStopWatch(),bg = statusBackGround,fg="black")
        self.__stopWatch.config(font=("times",20))
        self.__stopWatch.pack(side=TOP,anchor=N)
        self.__stopWatch.bind("<ButtonPress-1>",self.__changeFrameStatus)

        #Paint status indication for separation
        self.__statusFlag = Label(self.__statusStopWatch,text="status",bg = statusBackGround,fg = self.getStatusFlag())
        self.__statusFlag.config(font=("times",15))
        self.__statusFlag.pack(side=TOP,anchor=S)
        self.__statusFlag.bind("<ButtonPress-1>",self.__changeFrameStatus)

        #Paint label of altitude or pressure value
        self.__altitude_pressure = Label(self.__altitudePressure, text=self.getAltitudePressureData() + "m", bg = statusBackGround)
        self.__altitude_pressure.config(font=("times,20"))
        self.__altitude_pressure.pack(side = TOP,anchor=N)
        self.__altitude_pressure.bind("<ButtonPress-1>",self.__changeFrameAltimeter)

        #Paint descriptive label of data
        self.__title_of_data = Label(self.__altitudePressure,text=self.getAltitudePressureTitle(),bg = statusBackGround)
        self.__title_of_data.config(font=("times",20))
        self.__title_of_data.pack(side=TOP)
        self.__title_of_data.bind("<ButtonPress-1>",self.__changeFrameAltimeter)


    def __SettingsImageButtons(self):
        #Settings button built as a canvas
        textFont = tkfont.nametofont("TkDefaultFont")
        settingsLabel = "Settings"
        self.__settingsCanvas = Canvas(self.__master, height=(width-78)-8, width=35, borderwidth=2, relief="raised")
        self.__settingsCanvas.create_text((15, (width-78)/2-30), angle="90", anchor="ne", text=settingsLabel, font=textFont)
        self.__settingsCanvas.bind("<ButtonRelease-1>", lambda ev: ev.widget.configure(relief=RAISED))
        self.__settingsCanvas.place(x=height-42,y=2)
        self.__settingsCanvas.bind("<ButtonPress-1>",self.__changeFrameSetting)

        '''
        #Images button built as a canvas
        ImageLabel = "Images"
        Imagecanvas = Canvas(self.__master, height=(width - 78) / 2-4, width=35, borderwidth=2, relief="raised")
        Imagecanvas.create_text((15, (width - 78) / 4-15), angle="90", anchor="ne", text=ImageLabel,
                           font=textFont)
        Imagecanvas.bind("<ButtonPress-1>", lambda ev: ev.widget.configure(relief=SUNKEN))
        Imagecanvas.bind("<ButtonRelease-1>", lambda ev: ev.widget.configure(relief=RAISED))
        Imagecanvas.place(x=height-40,y=(width-78)/2+2)
        '''

    #******************Event handlers*************************

    def __changeFrameMap(self,ev):
        # Switch frame to map
        self.__mainFrame.destroy()
        self.__placeMainFrame()
        self.__runMap = GPSMap.Map(self.__mainFrame, self.__mapShowFlag)
        self.__mapBGRun()
        self.__mapShowFlag = 5

        # Unbind when pushed
        self.__mapCoordinates.unbind("<ButtonPress-1>")
        self.__img.unbind("<ButtonPress-1>")
        self.__latitude_longitude.unbind("<ButtonPress-1>")

        # Bind all other buttons
        self.__statusStopWatch.bind("<ButtonPress-1>", self.__changeFrameStatus)
        self.__stopWatch.bind("<ButtonPress-1>", self.__changeFrameStatus)
        self.__statusFlag.bind("<ButtonPress-1>", self.__changeFrameStatus)
        self.__altitudePressure.bind("<ButtonPress-1>", self.__changeFrameAltimeter)
        self.__altitude_pressure.bind("<ButtonPress-1>", self.__changeFrameAltimeter)
        self.__settingsCanvas.bind("<ButtonPress-1>", self.__changeFrameSetting)


    def __changeFrameStatus(self,ev):
        # Switch frame to map
        self.__mainFrame.destroy()
        self.__placeMainFrame()
        self.__statusFrame = Status.Display(self.__mainFrame)
        # Unbind when pushed
        self.__statusStopWatch.unbind("<ButtonPress-1>")
        self.__stopWatch.unbind("<ButtonPress-1>")
        self.__statusFlag.unbind("<ButtonPress-1>")

        # Bind all other buttons
        self.__mapCoordinates.bind("<ButtonPress-1>",self.__changeFrameMap)
        self.__img.bind("<ButtonPress-1>", self.__changeFrameMap)
        self.__latitude_longitude.bind("<ButtonPress-1>", self.__changeFrameMap)
        self.__altitudePressure.bind("<ButtonPress-1>", self.__changeFrameAltimeter)
        self.__altitude_pressure.bind("<ButtonPress-1>", self.__changeFrameAltimeter)
        self.__settingsCanvas.bind("<ButtonPress-1>", self.__changeFrameSetting)

    def __changeFrameAltimeter(self,ev):
        # Switch frame to map
        self.__mainFrame.destroy()
        self.__placeMainFrame()


        # Unbind when pushed
        self.__altitudePressure.unbind("<ButtonPress-1>")
        self.__altitude_pressure.unbind("<ButtonPress-1>")

        # Bind all other buttons
        self.__mapCoordinates.bind("<ButtonPress-1>", self.__changeFrameMap)
        self.__img.bind("<ButtonPress-1>", self.__changeFrameMap)
        self.__latitude_longitude.bind("<ButtonPress-1>", self.__changeFrameMap)
        self.__statusStopWatch.bind("<ButtonPress-1>", self.__changeFrameStatus)
        self.__stopWatch.bind("<ButtonPress-1>", self.__changeFrameStatus)
        self.__statusFlag.bind("<ButtonPress-1>", self.__changeFrameStatus)
        self.__settingsCanvas.bind("<ButtonPress-1>", self.__changeFrameSetting)

    def __changeFrameSetting(self,ev):
        # Switch frame to map
        self.__mainFrame.destroy()
        self.__placeMainFrame()
        Settings.Display(self.__mainFrame)
        ev.widget.configure(relief=SUNKEN)

        # Unbind when pushed
        self.__settingsCanvas.unbind("<ButtonPress-1>")

        # Bind all other buttons
        self.__mapCoordinates.bind("<ButtonPress-1>", self.__changeFrameMap)
        self.__img.bind("<ButtonPress-1>", self.__changeFrameMap)
        self.__latitude_longitude.bind("<ButtonPress-1>", self.__changeFrameMap)
        self.__statusStopWatch.bind("<ButtonPress-1>", self.__changeFrameStatus)
        self.__stopWatch.bind("<ButtonPress-1>", self.__changeFrameStatus)
        self.__statusFlag.bind("<ButtonPress-1>", self.__changeFrameStatus)
        self.__altitudePressure.bind("<ButtonPress-1>",self.__changeFrameAltimeter)
        self.__altitude_pressure.bind("<ButtonPress-1>",self.__changeFrameAltimeter)

    def __mapBGRun(self):
        self.__runMap.update()
        self.__master.after(700,self.__mapBGRun)


    '''
    def __startSocketGetter(self):
        self.__dataArray = StartSocket.start()
        if(self.__mapShowFlag ==5):

        if(self.__statusFrameSetFlag):

        if
    '''




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



if __name__ == '__main__':
    root = Tk()
    display = Display(root)
    root.mainloop()







