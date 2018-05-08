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

        self.__avt = Button(fullFrame, text = "h - t", bg='darkcyan', fg = 'white', width = 7)
        self.__avt.bind("<Button-1>", lambda ev: self.__setPath("/../DataFiles/altitude.csv"))
        self.__avt.grid(row = 0, column = 1, padx = 5)

        self.__etvt = Button(fullFrame, text = "T - t", bg='darkcyan', fg = 'white', width = 7)
        self.__etvt.bind("<Button-1>", lambda ev: self.__setPath("/../DataFiles/temperature.csv"))
        self.__etvt.grid(row = 0, column = 2, padx = 5)

        self.__irvt = Button(fullFrame, text = "IR - t", bg='darkcyan', fg = 'white', width = 7)
        self.__irvt.bind("<Button-1>", lambda ev: self.__setPath("/../DataFiles/IRdistance.csv"))
        self.__irvt.grid(row = 0, column = 3, padx = 5)

        self.__eacvt = Button(fullFrame, text = "Ex. a - t", bg='darkcyan', fg = 'white', width = 7)
        self.__eacvt.bind("<Button-1>", lambda ev: self.__setPath("/../DataFiles/accelerationEx.csv"))
        self.__eacvt.grid(row = 0, column = 4, padx = 5)

        self.__iavt = Button(fullFrame, text = "In. a - t", bg='darkcyan', fg = 'white', width = 7)
        self.__iavt.bind("<Button-1>", lambda ev: self.__setPath("/../DataFiles/accelerationIn.csv"))
        self.__iavt.grid(row = 0, column = 5, padx = 5)

        self.__btvt = Button(fullFrame, text = "B.T - t", bg='darkcyan', fg = 'white', width = 7)
        self.__btvt.bind("<Button-1>", lambda ev: self.__setPath("/../DataFiles/batTemperature.csv"))
        self.__btvt.grid(row = 0, column = 6, padx = 5)

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