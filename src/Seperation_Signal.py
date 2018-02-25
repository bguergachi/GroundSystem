from tkinter import *
import os,sys
from PIL import ImageTk, Image

class Separation_Signal:
    # ***************** Instantiate *****************
    def __init__(self, master):
        self.__master = master
        self.__opened = False
        self.__state = 0
        loadRed = Image.open(os.path.realpath(__file__)+"/../appImages/Redlight.png")
        loadRed.thumbnail(size=(100,100))
        self.__redlight=ImageTk.PhotoImage(loadRed)
        loadGreen = Image.open(os.path.realpath(__file__)+"/../appImages/Green_Light.png")
        loadGreen.thumbnail(size=(100, 100))
        self.__greenlight=ImageTk.PhotoImage(loadGreen)
        if __name__ == '__main__':
            self.window(master)
        self.printShit()

    def window(self, main):
        main.title('Separation Signal')
        height = 250
        width = 422
        self.__master.geometry('{}x{}'.format(width, height))

    def getState(self):
        return self.__state

    def printdseparate(self):
        self.__state = 0

    def printseparate(self):
        self.__state = 1

    def printShit(self):

        if self.__state == 0:
            self.__panel = Label(self.__master, image=self.__redlight)
            self.__panel.image = self.__redlight
            self.__panel.pack()

        elif self.__state == 1:
            self.__panel = Label(self.__master, image=self.__greenlight)
            self.__panel.image = self.__greenlight
            self.__panel.pack()

    def update(self):
        if self.__state == 0:
            self.__panel.config(image=self.__redlight)

        elif self.__state == 1:
            self.__panel.config(image=self.__greenlight)





if __name__ == '__main__':
    root = Tk()
    separation_Signal = Separation_Signal(root)
    root.resizable(height=250, width=422)
    root.mainloop()
