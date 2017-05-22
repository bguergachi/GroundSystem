from tkinter import *
import tkinter.font as tkfont
from PIL import ImageTk,Image

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


# Left Main Frame

    def sBar(self):
    # Main frame
        sval = Frame(self.__master)
        sval.pack(side=LEFT)

    # Altitude Frame
        alframe = Frame(sval, bg=statusBackGround, height=35, width=height / 3)
        alframe.pack(side=TOP)
        alframe.pack_propagate(False)

    # Airspeed Frame
        airframe = Frame(sval, bg=statusBackGround, height=35, width=height / 3)
        airframe.pack(side=TOP)
        airframe.pack_propagate(False)

    # Acceleration Frame
        accframe = Frame(sval, bg=statusBackGround, height=35, width=height / 3)
        accframe.pack(side=TOP)
        accframe.pack_propagate(False)

    # Pressure Frame
        presframe = Frame(sval, bg=statusBackGround, height=35, width=height / 3)
        presframe.pack(side=TOP)
        presframe.pack_propagate(False)

    # Temperature Frame
        tempframe = Frame(sval, bg=statusBackGround, height=35, width=height / 3)
        tempframe.pack(side=TOP)
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
        values.pack(side=RIGHT)

    # Altitude Frame
        altitudeframer = Frame(values, bg=BackGround, height=35, width=height / 3)
        altitudeframer.pack(side=TOP)
        altitudeframer.pack_propagate(False)

    # Airspeed Frame
        airspeedframer = Frame(values, bg=BackGround, height=35, width=height / 3)
        airspeedframer.pack(side=TOP)
        airspeedframer.pack_propagate(False)

    # Acceleration Frame
        accelerationframer = Frame(values, bg=BackGround, height=35, width=height / 3)
        accelerationframer.pack(side=TOP)
        accelerationframer.pack_propagate(False)

    # Pressure Frame
        pressureframer = Frame(values, bg=BackGround, height=35, width=height / 3)
        pressureframer.pack(side=TOP)
        pressureframer.pack_propagate(False)

    # Temperature Frame
        temperatureframer = Frame(values, bg=BackGround, height=35, width=height / 3)
        temperatureframer.pack(side=TOP)
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


root = Tk()
root.wm_title("Status/Signal")
display = Display(root)
root.mainloop()