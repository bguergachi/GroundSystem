from tkinter import *
from DataFiles import *
import matplotlib                                                               # Control / to comment out/in paragraphs
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
import random

# Screen Resolution
height = 422
width = 250

class Display:
    # Initialize
    def __init__(self, master):
        self.__master = master

        if __name__ == '__main__':
            self.__master.resizable(width=False, height=False)
            self.__master.geometry('{}x{}'.format(height, width))

        self.__upFrame()
        self.__fullFrame()

        self.widget = None

    # Top frame for Current and Elapsed Launch Time
    def __upFrame(self):

        upFrame = Frame(self.__master, height=1)
        upFrame.columnconfigure(0,weight=1)
        upFrame.columnconfigure(1,weight=1)
        upFrame.columnconfigure(2,weight=1)
        upFrame.pack(side=TOP, fill="x")

        curtimedisp = Label(upFrame, text="11:45:14", borderwidth=4, relief="ridge", width= 10, bg='Gold').grid(row=0, column=0, pady=4, padx=4)
        namedisp = Label(upFrame, text="Shivvy", borderwidth=4, relief="ridge", width= 10, bg='Gold').grid(row=0, column=1, pady=4, padx=4)
        eltimedisp = Label(upFrame, text="00:00:14", borderwidth=4, relief="ridge", width= 10, bg='Gold').grid(row=0, column=2, pady=4, padx=4)

    # Full Frame including Buttons
    def __fullFrame(self):

        fullFrame = Frame(self.__master)
        fullFrame.pack(side=BOTTOM)

        self.avt = Button(fullFrame, text = "Alt - Time", height= 2, width=12, bg='Cyan')
        self.avt.bind("<Button-1>", self.__animate)
        self.avt.pack(side=LEFT, pady=6, padx=4)

        self.irvt = Button(fullFrame, text = "IR - Time", height= 2, width=12, bg='Cyan')
        self.irvt.bind("<Button-1>", self.__animate)
        self.irvt.pack(side=LEFT, pady=6, padx=4)

        self.pvt = Button(fullFrame, text = "Press - Time", height= 2, width=12, bg='Cyan')
        self.pvt.bind("<Button-1>", self.__animate)
        self.pvt.pack(side=LEFT, pady=6, padx=4)

        self.tvt = Button(fullFrame, text = "Temp - Time", height= 2, width=12, bg='Cyan')
        self.tvt.bind("<Button-1>", self.__animate)
        self.tvt.pack(side=LEFT, pady=6, padx=4)

    # Function to read data from txt file
    def __animate(self, event):

        if self.widget:
            self.widget.destroy()

        pullData = open("sampleData.txt", "r").read()
        dataList = pullData.split('\n')
        xList = []
        yList = []
        for eachLine in dataList:
            if len(eachLine) > 1:
                x, y = eachLine.split(',')
                xList.append(int(x))
                yList.append(int(y))

        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        f.subplots_adjust(bottom=0.15)

        a.clear()
        a.plot(xList, yList)

        canvas = FigureCanvasTkAgg(f, self.__master)
        canvas.draw()
        self.widget = canvas.get_tk_widget()
        self.widget.pack()

        ani = animation.FuncAnimation(f, self.__animate, interval=1000)

        # 1000 ms


# Sample code used in earlier process to test button functionality

    # def __graph1(self, event):
    #
    #     if self.widget:
    #         self.widget.destroy()
    #
    #     f = Figure()
    #     a = f.add_subplot(111)
    #     f.subplots_adjust(bottom=0.15)
    #     a.plot([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],[0,30,90,150,250,400,750,1250,1750,2500,1750,1250,750,400,250,150,90,30,15,10,0])
    #
    #     canvas = FigureCanvasTkAgg(f, self.__master)
    #     canvas.draw()
    #     self.widget = canvas.get_tk_widget()
    #     self.widget.pack()
    #
    # def __graph2(self, event):
    #
    #     if self.widget:
    #         self.widget.destroy()
    #
    #     f = Figure()
    #     a = f.add_subplot(111)
    #     f.subplots_adjust(bottom=0.15)
    #     a.plot([1,2,3],[2,2.5,2])
    #
    #     canvas = FigureCanvasTkAgg(f, self.__master)
    #     canvas.draw()
    #     self.widget = canvas.get_tk_widget()
    #     self.widget.pack()
    #
    # def __graph3(self, event):
    #
    #     if self.widget:
    #         self.widget.destroy()
    #
    #     f = Figure()
    #     a = f.add_subplot(111)
    #     f.subplots_adjust(bottom=0.15)
    #     a.plot([1,2,3],[1,2,3])
    #
    #     canvas = FigureCanvasTkAgg(f, self.__master)
    #     canvas.draw()
    #     self.widget = canvas.get_tk_widget()
    #     self.widget.pack()
    #
    # def __graph4(self, event):
    #
    #     if self.widget:
    #         self.widget.destroy()
    #
    #     f = Figure()
    #     a = f.add_subplot(111)
    #     f.subplots_adjust(bottom=0.15)
    #     a.plot([1,2,3],[-1,-4,-6])
    #
    #     canvas = FigureCanvasTkAgg(f, self.__master)
    #     canvas.draw()
    #     self.widget = canvas.get_tk_widget()
    #     self.widget.pack()

if __name__ == '__main__':
    root = Tk()
    root.title("System Plots")
    display = Display(root)
    root.mainloop()