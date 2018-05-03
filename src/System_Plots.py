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

height = 422
width = 250

# f = Figure(figsize=(5,5), dpi=100)
# a = f.add_subplot(111)

class Display:
    def __init__(self, master):
        self.__master = master

        if __name__ == '__main__':
            self.__master.resizable(width=False, height=False)
            self.__master.geometry('{}x{}'.format(height, width))

        self.__upFrame()
        self.__fullFrame()

        self.widget = None

    def __upFrame(self):

        upFrame = Frame(self.__master, height=1)
        upFrame.columnconfigure(0,weight=1)
        upFrame.columnconfigure(1,weight=1)
        upFrame.columnconfigure(2,weight=1)
        upFrame.pack(side=TOP, fill="x")

        curtimedisp = Label(upFrame, text="11:45:14", borderwidth=4, relief="ridge", width= 10, bg='Gold').grid(row=0, column=0, pady=4, padx=4)
        namedisp = Label(upFrame, text="Shivvy", borderwidth=4, relief="ridge", width= 10, bg='Gold').grid(row=0, column=1, pady=4, padx=4)
        eltimedisp = Label(upFrame, text="00:00:14", borderwidth=4, relief="ridge", width= 10, bg='Gold').grid(row=0, column=2, pady=4, padx=4)

    def __fullFrame(self):

        fullFrame = Frame(self.__master)
        fullFrame.pack(side=BOTTOM)

        self.avt = Button(fullFrame, text = "Alt - Time", height= 2, width=12, bg='Cyan')
        self.avt.bind("<Button-1>", self.__graph1)
        self.avt.pack(side=LEFT, pady=6, padx=4)
        self.irvt = Button(fullFrame, text = "IR - Time", height= 2, width=12, bg='Cyan')
        self.irvt.bind("<Button-1>", self.__graph2)
        self.irvt.pack(side=LEFT, pady=6, padx=4)
        self.pvt = Button(fullFrame, text = "Press - Time", height= 2, width=12, bg='Cyan')
        self.pvt.bind("<Button-1>", self.__graph3)
        self.pvt.pack(side=LEFT, pady=6, padx=4)
        self.tvt = Button(fullFrame, text = "Temp - Time", height= 2, width=12, bg='Cyan')
        self.tvt.bind("<Button-1>", self.__graph4)
        self.tvt.pack(side=LEFT, pady=6, padx=4)

    # def animate(self, i, event):
    #
    #     if self.widget:
    #         self.widget.destroy()
    #
    #     pullData = open("sampleData.txt", "r").read()
    #     dataList = pullData.split('\n')
    #     xList = []
    #     yList = []
    #     for eachLine in dataList:
    #         if len(eachLine) > 1:
    #             x, y = eachLine.split(',')
    #             xList.append(int(x))
    #             yList.append(int(y))
    #
    #     a.clear()
    #     a.plot(xList, yList)


    def __graph1(self, event):

        if self.widget:
            self.widget.destroy()

        f = Figure()
        a = f.add_subplot(111)
        f.subplots_adjust(bottom=0.15)
        a.plot([1,2,3],[4,5,4])

        canvas = FigureCanvasTkAgg(f, self.__master)
        canvas.draw()
        self.widget = canvas.get_tk_widget()
        self.widget.pack()

    def __graph2(self, event):

        if self.widget:
            self.widget.destroy()

        f = Figure()
        a = f.add_subplot(111)
        f.subplots_adjust(bottom=0.15)
        a.plot([1,2,3],[2,2.5,2])

        canvas = FigureCanvasTkAgg(f, self.__master)
        canvas.draw()
        self.widget = canvas.get_tk_widget()
        self.widget.pack()

    def __graph3(self, event):

        if self.widget:
            self.widget.destroy()

        f = Figure()
        a = f.add_subplot(111)
        f.subplots_adjust(bottom=0.15)
        a.plot([1,2,3],[1,2,3])

        canvas = FigureCanvasTkAgg(f, self.__master)
        canvas.draw()
        self.widget = canvas.get_tk_widget()
        self.widget.pack()

    def __graph4(self, event):

        if self.widget:
            self.widget.destroy()

        f = Figure()
        a = f.add_subplot(111)
        f.subplots_adjust(bottom=0.15)
        a.plot([1,2,3],[-1,-4,-6])

        canvas = FigureCanvasTkAgg(f, self.__master)
        canvas.draw()
        self.widget = canvas.get_tk_widget()
        self.widget.pack()

if __name__ == '__main__':
    root = Tk()
    root.title("System Plots")
    # self.ani = animation.FuncAnimation(f, self.animate, interval=1000)
    display = Display(root)
    root.mainloop()

    # 1000 ms