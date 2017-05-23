from tkinter import *
from PIL import ImageTk,Image
import os

# resolution of the screen
height = 422
width = 250
statusBackGround = 'cyan'
BackGround = 'red'

class Display:
    # ***************** Instantiate *****************
    def __init__(self, master):
        self.__master = master

        # Set window parameters
        self.__master.resizable(width=False, height=False)
        self.__master.geometry('{}x{}'.format(height, width))

        self.sBar()
        self.valueBar()
        self.sepsig()



#Left Main Frame

    def sBar(self):
    # Main frame
        sval = Frame(self.__master)
        sval.pack(side=LEFT, anchor=S)

    # Altitude Frame
        alframe = Frame(sval, bg=statusBackGround, height=35, width=height / 3)
        alframe.pack(side=TOP, pady=2, padx=2)
        alframe.pack_propagate(False)

    # Airspeed Frame
        airframe = Frame(sval, bg=statusBackGround, height=35, width=height / 3)
        airframe.pack(side=TOP, pady=2, padx=2)
        airframe.pack_propagate(False)

    # Acceleration Frame
        accframe = Frame(sval, bg=statusBackGround, height=35, width=height / 3)
        accframe.pack(side=TOP, pady=2, padx=2)
        accframe.pack_propagate(False)

    # Pressure Frame
        presframe = Frame(sval, bg=statusBackGround, height=35, width=height / 3)
        presframe.pack(side=TOP, pady=2, padx=2)
        presframe.pack_propagate(False)

    # Temperature Frame
        tempframe = Frame(sval, bg=statusBackGround, height=35, width=height / 3)
        tempframe.pack(side=TOP, pady=2, padx=2)
        tempframe.pack_propagate(False)

    # Paint label of altitude
        altdisplay = Label(alframe, text="Altitude", bg=statusBackGround)
        altdisplay.config(font=("times,12"))
        altdisplay.pack(side=TOP)

    # Paint label of airspeed
        airdisplay = Label(airframe, text="Airspeed", bg=statusBackGround)
        airdisplay.config(font=("times,12"))
        airdisplay.pack(side=TOP)

    # Paint label of acceleration
        accdisplay = Label(accframe, text="Acceleration", bg=statusBackGround)
        accdisplay.config(font=("times,12"))
        accdisplay.pack(side=TOP)

    # Paint label of pressure
        presdisplay = Label(presframe, text="Pressure", bg=statusBackGround)
        presdisplay.config(font=("times,12"))
        presdisplay.pack(side=TOP)

    # Paint label of temperature
        tempdisplay = Label(tempframe, text="Temperature", bg=statusBackGround)
        tempdisplay.config(font=("times,12"))
        tempdisplay.pack(side=TOP)

#Right Main Frame

    def valueBar(self):
        # Main frame
        values = Frame(self.__master)
        values.pack(side=LEFT, anchor=S)

    # Altitude Frame
        altitudeframer = Frame(values, bg=BackGround, height=35, width=height / 3)
        altitudeframer.pack(side=TOP, pady=2, padx=2)
        altitudeframer.pack_propagate(False)

    # Airspeed Frame
        airspeedframer = Frame(values, bg=BackGround, height=35, width=height / 3)
        airspeedframer.pack(side=TOP, pady=2, padx=2)
        airspeedframer.pack_propagate(False)

    # Acceleration Frame
        accelerationframer = Frame(values, bg=BackGround, height=35, width=height / 3)
        accelerationframer.pack(side=TOP, pady=2, padx=2)
        accelerationframer.pack_propagate(False)

    # Pressure Frame
        pressureframer = Frame(values, bg=BackGround, height=35, width=height / 3)
        pressureframer.pack(side=TOP, pady=2, padx=2)
        pressureframer.pack_propagate(False)

    # Temperature Frame
        temperatureframer = Frame(values, bg=BackGround, height=35, width=height / 3)
        temperatureframer.pack(side=TOP, pady=2, padx=2)
        temperatureframer.pack_propagate(False)

    # Paint label of altitude
        altitudedisplayr = Label(altitudeframer, text="Altitude", bg='Cyan')
        altitudedisplayr.config(font=("times,12"))
        altitudedisplayr.pack(side=TOP)

    # Paint label of airspeed
        airspeeddisplayr = Label(airspeedframer, text="Airspeed", bg='Cyan')
        airspeeddisplayr.config(font=("times,12"))
        airspeeddisplayr.pack(side=TOP)

    # Paint label of acceleration
        accelerationdisplayr = Label(accelerationframer, text="Acceleration", bg='Cyan')
        accelerationdisplayr.config(font=("times,12"))
        accelerationdisplayr.pack(side=TOP)

    # Paint label of pressure
        pressuredisplayr = Label(pressureframer, text="Pressure", bg='Cyan')
        pressuredisplayr.config(font=("times,12"))
        pressuredisplayr.pack(side=TOP)

    # Paint label of temperature
        temperaturedisplayr = Label(temperatureframer, text="Temperature", bg='Cyan')
        temperaturedisplayr.config(font=("times,12"))
        temperaturedisplayr.pack(side=TOP)

#Far Right SepSig Frame

    def sepsig(self):
    # Main frame
        sep = Frame(self.__master)
        sep.pack(side=RIGHT, anchor=S)

    #Frame with title
        septitleframe = Frame(sep, height=28, width=height / 2)
        septitleframe.pack(side=TOP, pady=2, padx=2)
        septitleframe.pack_propagate(False)

        sepsigname = Label(septitleframe, text="Seperation Signal", bg='Cyan')
        sepsigname.config(font=("times,12"))
        sepsigname.pack(side=TOP)

    # Frame and display of sepsig
        sepsignal = Frame(sep, height=160, width=height / 2)
        sepsignal.pack(side=TOP, pady=2, padx=2)
        sepsignal.pack_propagate(False)

    #Load light image and render image
        load = ImageTk.PhotoImage(Image.open("Redlight.png"))

    #Label into which Image is inserted
        img = Label(sepsignal,image = load, bg='gold')
        img.pack()

#Setters

    def set_altitude(self, altitude):
        self.__altitude = altitude

    def set_airspeed(self, airspeed):
        self.__airspeed = airspeed

    def set_acceleration(self, acceleration):
        self.__acceleration = acceleration

    def set_pressure(self, pressure):
        self.__pressure = pressure

    def set_temperature(self, temperature):
        self.__temperature = temperature

root = Tk()
root.wm_title("Status/Signal")
display = Display(root)
root.mainloop()