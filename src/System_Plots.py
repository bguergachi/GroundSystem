from tkinter import *
import matplotlib                                                               # Control / to comment out/in paragraphs
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
import sys,os, time


# Screen Resolution
height = 422
width = 250

class Plot:
    # Initialize
    def __init__(self, master):
        self.__master = master

        if __name__ == '__main__':
            self.__master.resizable(width=False, height=False)
            self.__master.geometry('{}x{}'.format(height, width))

        # self.__upFrame()
        self.__fullFrame()

    # Full Frame including Buttons
    def __fullFrame(self):

        fullFrame = Frame(self.__master)
        fullFrame.pack(side=BOTTOM)

        self.__avt = Button(fullFrame, text = "Alt - Time", height= 2, width=7, bg='Cyan')
        self.__avt.bind("<Button-1>", self.update("/../DataFiles/altitude"))
        self.__avt.pack(side=LEFT, pady=6, padx=4)

        self.__irvt = Button(fullFrame, text = "Temperature - Time", height= 2, width=7, bg='Cyan')
        self.__irvt.bind("<Button-1>", self.update("/../DataFiles/temperature"))
        self.__irvt.pack(side=LEFT, pady=6, padx=4)

        self.__iacvt = Button(fullFrame, text = "IR Distance - Time", height= 2, width=12, bg='Cyan')
        self.__iacvt.bind("<Button-1>", self.update("/../DataFiles/IRdistance"))
        self.__iacvt.pack(side=LEFT, pady=6, padx=4)

        self.__eacvt = Button(fullFrame, text = "Ex. Accel - Time", height= 2, width=12, bg='Cyan')
        self.__eacvt.bind("<Button-1>", self.update("/../DataFiles/SECOND ACCEL CHANGE THIS"))
        self.__eacvt.pack(side=LEFT, pady=6, padx=4)

        self.__tvt = Button(fullFrame, text = "Temp - Time", height= 2, width=12, bg='Cyan')
        self.__tvt.bind("<Button-1>", self.update("/../DataFiles/altitude"))
        self.__tvt.pack(side=LEFT, pady=6, padx=4)

    # Function to read data from txt file
    def update(self, filepath):

        self.__widget = None

        if self.__widget:
            self.__widget.destroy()

        pullData = open(os.path.dirname(os.path.realpath(__file__))+ filepath,"r").read()

        dataList = pullData.split('\n')
        xList = []
        yList = []
        for eachLine in dataList:
            if len(eachLine) > 1:
                x, y = eachLine.split(',')
                xList.append(int(x))
                yList.append(int(y))

        figure = Figure(figsize=(5, 5), dpi=100)
        a = figure.add_subplot(111)
        figure.subplots_adjust(bottom=0.15)

        a.clear()
        a.plot(xList, yList)

        canvas = FigureCanvasTkAgg(figure, self.__master)
        canvas.draw()
        self.__widget = canvas.get_tk_widget()
        self.__widget.pack()

        ani = animation.FuncAnimation(figure, self.update, interval=250)

if __name__ == '__main__':
    root = Tk()
    root.title("System Plots")
    display = Plot(root)
    root.mainloop()