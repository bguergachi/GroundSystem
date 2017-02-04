from tkinter import *
import random

def window (main):
    main.title ('Altimeter')
    height=250
    width=422
    root.geometry('{}x{}'.format(width, height))

def printaltitude(event):
    print("shit this works")

def printtemperature():
    sensor.config(text='shazzy')

def printpressure(event):
    print("Shit this works!")

def printairspeed(event):
    print("Shit his works!")

root = Tk()
root.resizable(width=False, height=False)

window(root)

#This is the frame where the buttons are located
mainFrame = Frame(root)
mainFrame.pack()

#This is the frame where the buttons are located
buttonFrame = Frame(mainFrame, height=250, width=1140)
buttonFrame.pack(side=LEFT, anchor=W)

#This is the frame where the values are located
metricFrame= Frame(mainFrame, height=250, width=240, bg='cyan')
metricFrame.pack_propagate(False)
metricFrame.pack(side=LEFT, anchor=W)

sensor = Label(metricFrame).pack()

# This is the configuration for the Altitude Button. It includes the location, size of font, and the print command
altitude = Button(buttonFrame, text='Altitude', command = printaltitude, bg='red', fg='white')
altitude.bind("<Button-1>", printaltitude)
altitude.config(font=("times,12"))
altitude.pack(side=BOTTOM, fill=BOTH, anchor=W)

# This is the configuration for the Temperature Button. It includes the location, size of font, and the print command
temperature = Button(buttonFrame, text='Temperature', command = printtemperature, bg='cyan', fg='black')
temperature.config(font=("times,12"))
temperature.pack(side=BOTTOM, fill=BOTH, anchor=W)

# This is the configuration for the Pressure Button. It includes the location, size of font, and the print command
pressure = Button(buttonFrame, text='Pressure', command = printpressure, bg='red', fg='white')
pressure.bind("<Button-1>", printpressure)
pressure.config(font=("times,12"))
pressure.pack(side=BOTTOM, fill=BOTH, anchor=W)

# This is the configuration for the Airspeed Button. It includes the location, size of font, and the print command
airspeed = Button(buttonFrame, text='Airspeed', command = printairspeed, bg='cyan', fg='black')
airspeed.bind("<Button-1>", printairspeed)
airspeed.config(font=("times,12"))
airspeed.pack(side=BOTTOM, fill=BOTH, anchor=W)

mainloop()