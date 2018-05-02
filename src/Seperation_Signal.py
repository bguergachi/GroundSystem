from tkinter import *
import os,sys
from PIL import ImageTk, Image

class Separation_Signal:
    # ***************** Instantiate *****************
    def __init__(self, master):
        self.__master = master
        self.__opened = False
        self.__state = 0
        loadRed = Image.open(os.path.dirname(os.path.realpath(__file__))+"/../appImages/Redlight.png")
        loadRed.thumbnail(size=(100,100))
        self.__redlight=ImageTk.PhotoImage(loadRed)
        loadGreen = Image.open(os.path.dirname(os.path.realpath(__file__))+"/../appImages/Green_Light.png")
        loadGreen.thumbnail(size=(100, 100))
        self.__greenlight=ImageTk.PhotoImage(loadGreen)
        if __name__ == '__main__':
            self.window(master)
        self.printShit()







if __name__ == '__main__':
    root = Tk()
    separation_Signal = Separation_Signal(root)
    root.resizable(height=250, width=422)
    root.mainloop()
