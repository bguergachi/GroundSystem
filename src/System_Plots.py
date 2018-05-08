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

        self.__widget = None
        self.__filepath = "/../DataFiles/temperature.csv"
        # self.__upFrame()
        self.__fullFrame()

    # Full Frame including Buttons
    def __fullFrame(self):

        fullFrame = Frame(self.__master)
        fullFrame.pack(side=BOTTOM)

        self.__avt = Button(fullFrame, text = "Alt - Time", bg='darkcyan', fg = 'white', width = 10)
        self.__avt.bind("<Button-1>", lambda ev: self.__setPath("/../DataFiles/altitude.csv"))
        self.__avt.grid(row = 0, column = 1, padx = 3, pady = 1)

        self.__etvt = Button(fullFrame, text = "Ex. Temp - Time", bg='darkcyan', fg = 'white', width = 12)
        self.__etvt.bind("<Button-1>", lambda ev: self.__setPath("/../DataFiles/temperature.csv"))
        self.__etvt.grid(row = 0, column = 2, padx = 3, pady = 1)

        self.__irvt = Button(fullFrame, text = "IR - Time", bg='darkcyan', fg = 'white', width = 10)
        self.__irvt.bind("<Button-1>", lambda ev: self.__setPath("/../DataFiles/IRdistance.csv"))
        self.__irvt.grid(row = 0, column = 3, padx = 3, pady = 1)

        self.__eacvt = Button(fullFrame, text = "Ex. Accel - Time", bg='darkcyan', fg = 'white', width = 15)
        self.__eacvt.bind("<Button-1>", lambda ev: self.__setPath("/../DataFiles/acceleration.csv"))
        self.__eacvt.grid(row = 1, column = 1, padx = 3, pady = 3)

        self.__iavt = Button(fullFrame, text = "In. Accel - Time", bg='darkcyan', fg = 'white', width = 15)
        self.__iavt.bind("<Button-1>", lambda ev: self.__setPath("SECOND MPU"))
        self.__iavt.grid(row = 1, column = 3, padx = 3)

        self.__btvt = Button(fullFrame, text = "Bat. Temp - Time", bg='darkcyan', fg = 'white', width = 15)
        self.__btvt.bind("<Button-1>", lambda ev: self.__setPath("BAT TEMP"))
        self.__btvt.grid(row = 1, column = 2, padx = 3, pady = 3)

    def __setPath(self,filepath):
        self.__filepath = filepath

    # Function to read data from txt file
    def update(self):
        print(self.__filepath)
        pullData = open(os.path.dirname(os.path.realpath(__file__))+ self.__filepath,"r").read()

        dataList = pullData.split('\n')
        xList = []
        yList = []
        for eachLine in dataList:
            if len(eachLine) > 1:
                x, y = eachLine.split(',')
                xList.append(x)
                yList.append(y)

        figure = Figure(figsize=(5, 5), dpi=100)
        a = figure.add_subplot(111)
        figure.subplots_adjust(bottom=0.15)

        a.clear()
        a.plot(xList, yList)

        canvas = FigureCanvasTkAgg(figure, self.__master)
        canvas.draw()
        self.__widget = canvas.get_tk_widget()
        self.__widget.pack()

        #ani = animation.FuncAnimation(figure, self.update, interval=250)

if __name__ == '__main__':
    root = Tk()
    root.title("System Plots")
    display = Plot(root)
    
    root.mainloop()