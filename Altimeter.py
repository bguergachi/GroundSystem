from tkinter import *
import random
import time

class Altimeter_Signal:
    # ***************** Instantiate *****************
    def __init__(self, master):
        self.__master = master
        self.window(self.__master)
        self.__master.resizable(width=False, height=False)

        # MAINFRAME
        # This is the frame where the buttons are located
        self.__mainFrame = Frame(self.__master)
        self.__mainFrame.pack()

        # BUTTONFRAME
        # This is also the frame where the buttons are located
        self.__buttonFrame = Frame(self.__mainFrame, height=250, width=1140)
        self.__buttonFrame.pack(side=LEFT, anchor=W)

        # METRICFRAME
        # This is the frame where the value label is located - See SENSOR LABEL
        self.__metricFrame = Frame(self.__mainFrame, height=250, width=240, bg='cyan')
        self.__metricFrame.pack_propagate(False)
        self.__metricFrame.pack(side=LEFT, anchor=W)

        # VAR1
        # Var1 defines variable to be used for live values - see SENSOR LABEL
        self.__var1 = StringVar(self.__metricFrame)

        # SENSOR LABEL
        # This is the value label which is used to display the live values
        self.__sensor = Label(self.__metricFrame, height=50, width=200, font='size, 25', fg='green',
                              textvariable=self.__var1)
        self.__sensor.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.__sensor.pack()

        # ALTITUDE BUTTON DESCRIPTION
        # This is the configuration for the Altitude Button. It includes the location, size of font, and the print command
        self.__altitude = altitude = Button(self.__buttonFrame, text='Altitude', bg='red', fg='white',
                                            command=self.printaltitude)
        self.__altitude.config(font=("times,12"))
        self.__altitude.pack(side=BOTTOM, fill=BOTH, anchor=W)

        # TEMPERATURE BUTTON DESCRIPTION
        # This is the configuration for the Temperature Button. It includes the location, size of font, and the print command
        self.__temperature = temperature = Button(self.__buttonFrame, text='Temperature', bg='cyan', fg='black',
                                                  command=self.printtemperature)
        self.__temperature.config(font=("times,12"))
        self.__temperature.pack(side=BOTTOM, fill=BOTH, anchor=W)

        # PRESSURE BUTTON DESCRIPTION
        # This is the configuration for the Pressure Button. It includes the location, size of font, and the print command
        self.__pressure = pressure = Button(self.__buttonFrame, text='Pressure', bg='red', fg='white',
                                            command=self.printpressure)
        self.__pressure.config(font=("times,12"))
        self.__pressure.pack(side=BOTTOM, fill=BOTH, anchor=W)

        # AIRSPEED BUTTON DESCRIPTION
        # This is the configuration for the Airspeed Button. It includes the location, size of font, and the print command
        self.__airspeed = airspeed = Button(self.__buttonFrame, text='Airspeed', bg='cyan', fg='black',
                                            command=self.printairspeed)
        self.__airspeed.config(font=("times,12"))
        self.__airspeed.pack(side=BOTTOM, fill=BOTH, anchor=W)

        # ORIGINAL STATE
        # This is the original state used to display the 'Initate' text
        self.__state = -1
        self.update()

    # MAINWINDOW
    # This is the window you see when you run the program
    def window(self, main):
        main.title('Altimeter')
        height = 250
        width = 422
        main.geometry('{}x{}'.format(width, height))

        # ALTITUDE BUTTON - see ALTITUDE BUTTON DESCRIPTION

    def printaltitude(self):
        self.__state = 0

        # TEMPERATURE BUTTON - see TEMPERATURE BUTTON DESCRIPTION

    def printtemperature(self):
        self.__state = 1

        # PRESSURE BUTTON - see PRESSURE BUTTON DESCRIPTION

    def printpressure(self):
        self.__state = 2

        # AIRSPEED BUTTON - see AIRSPEED BUTTON DESCRIPTION

    def printairspeed(self):
        self.__state = 3

    def setSensor(self):
        '''self.__sensor.config('Text =whatever')'''

    # UPDATE FUNCTION
    # This function serves as the primary tool to determine the state in order to let SENSOR LABEL know which information is desired
    def update(self):
        displayText = ''
        if self.__state == -1:
            displayText = 'Initiate'
        elif self.__state == 0:
            displayText = 'Altitude'
        elif self.__state == 1:
            displayText = 'Temperature'
        elif self.__state == 2:
            displayText = 'Pressure'
        elif self.__state == 3:
            displayText = 'Airspeed'

        self.__var1.set(displayText)
        self.__metricFrame.update()

        # MAINLOOP
        # This function has the purpose of refreshing the data to provide a continous live feed
        self.__master.after(200, self.update)


root = Tk()
altimeter_Signal = Altimeter_Signal(root)
root.mainloop()
