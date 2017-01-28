from tkinter import *
root = Tk()
root.resizable(width=False, height=False)

def window (main):
    main.title ('Altimeter')
    height=250
    width=422
    root.geometry('{}x{}'.format(width, height))

window(root)

mainFrame = Frame(root)
mainFrame.pack()

buttonFrame = Frame(mainFrame, height=250, width=1140)
buttonFrame.pack(side=LEFT, anchor=W)

metricFrame= Frame(mainFrame, height=250, width=240, bg='cyan')
metricFrame.pack(side=LEFT, anchor=W)

def printaltitude(event):
    print("Shit this works!")

altitude = Button(buttonFrame, text='Altitude', bg='red', fg='white')
altitude.bind("<Button-1>", printaltitude)
altitude.config(font=("times,12"))
altitude.pack(side=BOTTOM, fill=BOTH, anchor=W)

def printtemperature(event):
    print("Shit this works!")

temperature = Button(buttonFrame, text='Temperature', bg='cyan', fg='black')
temperature.bind("<Button-1>", printtemperature)
temperature.config(font=("times,12"))
temperature.pack(side=BOTTOM, fill=BOTH, anchor=W)

def printpressure(event):
    print("Shit this works!")

pressure = Button(buttonFrame, text='Pressure', bg='red', fg='white')
pressure.bind("<Button-1>", printpressure)
pressure.config(font=("times,12"))
pressure.pack(side=BOTTOM, fill=BOTH, anchor=W)

def printairspeed(event):
    print("Shit this works!")

airspeed = Button(buttonFrame, text='Airspeed', bg='cyan', fg='black')
airspeed.bind("<Button-1>", printairspeed)
airspeed.config(font=("times,12"))
airspeed.pack(side=BOTTOM, fill=BOTH, anchor=W)

mainloop()