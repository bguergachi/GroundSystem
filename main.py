from tkinter import *

import os

import sys

'''

    This class is used to display the main window

'''


class Display:
    __currentTime = "13:20:42"  # Current time to display

    __lastMesgTime = "13:19:20"  # Time of last message

    def __init__(self, master):
        # Set window parameters

        master.resizable(width=False, height=False)

        master.geometry('{}x{}'.format(480, 320))

        master.overrideredirect(True)

        # Print label of time and time of last recived message

        time = Label(root,
                     text="Time:  " + self.__currentTime + "\t\t\t" + "Time of Last Message:  " + self.__lastMesgTime,
                     bd=1,

                     relief=SUNKEN, width=70)

        time.pack(side=TOP, anchor=W)

        status = Frame(master)

        status.pack(side=BOTTOM, fill="x")

        mapCoordinates = Frame(status, bg="blue", height=70, width=480 / 3 - 4)

        mapCoordinates.pack(side=LEFT, pady=2, padx=2)

        statusStopWatch = Frame(status, bg="blue", height=70, width=480 / 3 - 4)

        statusStopWatch.pack(side=LEFT, pady=2, padx=2)

        altitudePressure = Frame(status, bg="blue", height=70, width=480 / 3 - 4)

        altitudePressure.pack(side=LEFT, pady=2, padx=2)


root = Tk()

display = Display(root)

root.mainloop()
