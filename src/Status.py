from tkinter import *

from GroundSystem.src import Seperation_Signal

# resolution of the screen
height = 422
width = 250
statusBackGround = 'cyan'
BackGround = 'red'

class Display:
    # ***************** Instantiate *****************
    def __init__(self, master):
        self.__master = master

        self.__status = 0

        # Set window parameters
        if __name__ == '__main__':
            self.__master.resizable(width=False, height=False)
            self.__master.geometry('{}x{}'.format(height, width))

        self.__sBar()
        self.__valueBar()
        self.__sepsig()
        self.__runSigImage()



#Left Main Frame

    def __sBar(self):
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
        accdisplay = Label(accframe, text="Speed", bg=statusBackGround)
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

    def __valueBar(self):
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
        altitudedisplayr = Label(altitudeframer, text=self.setAltitude(self), bg='Cyan')
        altitudedisplayr.config(font=("times,12"))
        altitudedisplayr.pack(side=TOP)

    # Paint label of airspeed
        airspeeddisplayr = Label(airspeedframer, text=self.setAirspeed(self), bg='Cyan')
        airspeeddisplayr.config(font=("times,12"))
        airspeeddisplayr.pack(side=TOP)

    # Paint label of acceleration
        accelerationdisplayr = Label(accelerationframer, text=self.setAcceleration(self), bg='Cyan')
        accelerationdisplayr.config(font=("times,12"))
        accelerationdisplayr.pack(side=TOP)

    # Paint label of pressure
        pressuredisplayr = Label(pressureframer, text=self.setPressure(self), bg='Cyan')
        pressuredisplayr.config(font=("times,12"))
        pressuredisplayr.pack(side=TOP)

    # Paint label of temperature
        temperaturedisplayr = Label(temperatureframer, text=self.setTemperature(self), bg='Cyan')
        temperaturedisplayr.config(font=("times,12"))
        temperaturedisplayr.pack(side=TOP)

#Far Right SepSig Frame

    def __sepsig(self):
    # Main frame
        sep = Frame(self.__master)
        sep.pack(side=LEFT, anchor=S)

    #Frame with title
        septitleframe = Frame(sep, height=28, width=height / 2, bg='Cyan')
        septitleframe.pack(side=TOP, pady=2, padx=2)
        septitleframe.pack_propagate(False)

        sepsigname = Label(septitleframe, text=" Sep Signal", bg='Cyan')
        sepsigname.config(font=("times,3"))
        sepsigname.pack(side=TOP)

    # Frame and display of sepsig
        self.__imageFrame = Frame(sep, height=160, width=height / 2)
        self.__imageFrame.pack(side=TOP, pady=2, padx=2)
        self.__imageFrame.pack_propagate(False)


    #Paint signal image in label with parent being frame with map information
        self.__statusImage = Seperation_Signal.Separation_Signal(self.__imageFrame)







    def __runSigImage(self):
    #Check if seperation sig is true or false
        if self.__status:
            self.__statusImage.printdseparate()
        else:
            self.__statusImage.printseparate()

        self.__statusImage.update()
        self.__master.after(700,self.__runSigImage)








#****************************************Setters******************************************
    def setStatus(self, status):
        self.__status = status


    def setAltitude(self, altitude):
        self.__altitude = altitude

    def setAirspeed(self, airspeed):
        self.__airspeed = airspeed

    def setAcceleration(self, acceleration):
        self.__acceleration = acceleration

    def setPressure(self, pressure):
        self.__pressure = pressure

    def setTemperature(self, temperature):
        self.__temperature = temperature

if __name__ == '__main__':
    root = Tk()
    root.wm_title("Status/Signal")
    display = Display(root)
    root.mainloop()
