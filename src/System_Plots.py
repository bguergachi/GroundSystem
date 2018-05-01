from tkinter import *
from DataFiles import *

# resolution of the screen
height = 422
width = 250
BackGround = 'red'

class Display:
    # ***************** Instantiate *****************
    def __init__(self, master):
        self.__master = master
        self.__sysPlot = 0

        # Set window parameters
        if __name__ == '__main__':
            self.__master.resizable(width=False, height=False)
            self.__master.geometry('{}x{}'.format(height, width))

    def __sBar(self):
    # Main frame
        sval = Frame(self.__master)
        sval.pack(side=TOP, anchor=N)

    def __plotBar(self):
        # Main frame
        status = Frame(self.__master)
        status.pack(side=BOTTOM, fill="x")

if __name__ == '__main__':
    root = Tk()
    root.mainloop()