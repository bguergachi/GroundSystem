from tkinter import *
import random

def window (main):
    main.title ('Altimeter')
    height=250
    width=422
    root.geometry('{}x{}'.format(width, height))

def printaltitude(e):
    sensor.config(text='blue')

def printtemperature(e):
    sensor.config(text='red')

def printpressure(e):
    sensor.config(text='orange')

def printairspeed(e):
    sensor.config(text='green')

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

sensor = Label(metricFrame, height=50,width=200, font='size, 20', text='shiaf')
sensor.place(relx=0.5, rely=0.5, anchor=CENTER)
sensor.pack()

# This is the configuration for the Altitude Button. It includes the location, size of font, and the print command
altitude = Button(buttonFrame, text='Altitude', bg='red', fg='white')
altitude.bind("<Button-1>", printaltitude)
altitude.config(font=("times,12"))
altitude.pack(side=BOTTOM, fill=BOTH, anchor=W)

# This is the configuration for the Temperature Button. It includes the location, size of font, and the print command
temperature = Button(buttonFrame, text='Temperature', bg='cyan', fg='black')
temperature.bind("<Button-1>", printtemperature)
temperature.config(font=("times,12"))
temperature.pack(side=BOTTOM, fill=BOTH, anchor=W)

# This is the configuration for the Pressure Button. It includes the location, size of font, and the print command
pressure = Button(buttonFrame, text='Pressure', bg='red', fg='white')
pressure.bind("<Button-1>", printpressure)
pressure.config(font=("times,12"))
pressure.pack(side=BOTTOM, fill=BOTH, anchor=W)

# This is the configuration for the Airspeed Button. It includes the location, size of font, and the print command
airspeed = Button(buttonFrame, text='Airspeed', bg='cyan', fg='black')
airspeed.bind("<Button-1>", printairspeed)
airspeed.config(font=("times,12"))
airspeed.pack(side=BOTTOM, fill=BOTH, anchor=W)

mainloop()