from tkinter import *
import random
import time

#MAINWINDOW
#This is the window you see when you run the program
def window(main):
    main.title('Altimeter')
    height = 250
    width = 422
    root.geometry('{}x{}'.format(width, height))

#ALTITUDE BUTTON - see ALTITUDE BUTTON DESCRIPTION
def printaltitude():
    global state
    state=0

#TEMPERATURE BUTTON - see TEMPERATURE BUTTON DESCRIPTION
def printtemperature():
    global state
    state = 1

#PRESSURE BUTTON - see PRESSURE BUTTON DESCRIPTION
def printpressure():
    global state
    state = 2

#AIRSPEED BUTTON - see AIRSPEED BUTTON DESCRIPTION
def printairspeed():
    global state
    state = 3
    '''sensor.config(text='green')'''

root = Tk()
root.resizable(width=False, height=False)

window(root)

#MAINFRAME
# This is the frame where the buttons are located
mainFrame = Frame(root)
mainFrame.pack()

#BUTTONFRAME
# This is also the frame where the buttons are located
buttonFrame = Frame(mainFrame, height=250, width=1140)
buttonFrame.pack(side=LEFT, anchor=W)

#METRICFRAME
# This is the frame where the value label is located - See SENSOR LABEL
metricFrame = Frame(mainFrame, height=250, width=240, bg='cyan')
metricFrame.pack_propagate(False)
metricFrame.pack(side=LEFT, anchor=W)

#VAR1
#Var1 defines variable to be used for live values - see SENSOR LABEL
var1 = StringVar(metricFrame)

#SENSOR LABEL
# This is the value label which is used to display the live values
sensor = Label(metricFrame, height=50, width=200, font='size, 25', fg='green', textvariable=var1)
sensor.place(relx=0.5, rely=0.5, anchor=CENTER)
sensor.pack()

#ALTITUDE BUTTON DESCRIPTION
# This is the configuration for the Altitude Button. It includes the location, size of font, and the print command
altitude = Button(buttonFrame, text='Altitude', bg='red', fg='white', command=printaltitude)
altitude.config(font=("times,12"))
altitude.pack(side=BOTTOM, fill=BOTH, anchor=W)

#TEMPERATURE BUTTON DESCRIPTION
# This is the configuration for the Temperature Button. It includes the location, size of font, and the print command
temperature = Button(buttonFrame, text='Temperature', bg='cyan', fg='black', command=printtemperature)
temperature.config(font=("times,12"))
temperature.pack(side=BOTTOM, fill=BOTH, anchor=W)

#PRESSURE BUTTON DESCRIPTION
# This is the configuration for the Pressure Button. It includes the location, size of font, and the print command
pressure = Button(buttonFrame, text='Pressure', bg='red', fg='white', command=printpressure)
pressure.config(font=("times,12"))
pressure.pack(side=BOTTOM, fill=BOTH, anchor=W)

#AIRSPEED BUTTON DESCRIPTION
# This is the configuration for the Airspeed Button. It includes the location, size of font, and the print command
airspeed = Button(buttonFrame, text='Airspeed', bg='cyan', fg='black', command=printairspeed)
airspeed.config(font=("times,12"))
airspeed.pack(side=BOTTOM, fill=BOTH, anchor=W)

#ORIGINAL STATE
#This is the original state used to display the 'Initate' text
state = -1

#UPDATE FUNCTION
#This function serves as the primary tool to determine the state in order to let SENSOR LABEL know which information is desired
def update():
    displayText = ''
    if state == -1:
        displayText = 'Initiate'
    elif state == 0:
        displayText = 'Altitude'
    elif state == 1:
        displayText = 'Temperature'
    elif state == 2:
        displayText = 'Pressure'
    elif state == 3:
        displayText = 'Airspeed'

    var1.set(displayText)
    metricFrame.update()

#MAINLOOP
#This function has the purpose of refreshing the data to provide a continous live feed
def mainloop():
    while True:
        update()

mainloop()