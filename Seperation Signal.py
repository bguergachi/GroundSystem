from tkinter import *
from PIL import ImageTk, Image

class Separation_Signal:
    # ***************** Instantiate *****************
    def __init__(self, master):
        self.__opened = False
        self.__state = 0
        self.__redlight=ImageTk.PhotoImage(Image.open("./Image/redlight.png"))
        self.__greenlight=ImageTk.PhotoImage(Image.open("./Image/greenlight.png"))
        self.window(master)
        self.update()

    def window(self, main):
        main.title('Separation Signal')
        height = 250
        width = 422
        root.geometry('{}x{}'.format(width, height))

    def getState(self):
        return self.__state

    def printdseparate(self):
        state = 0

    def printseparate(self):
        state = 1

    def update(self):

        if self.__state == 0:

            if self.__opened == False:

                panel = Label(root, image=self.__redlight)
                panel.image = self.__redlight
                panel.pack()
                self.__opened=True

        elif self.__state == 1:

            if self.__opened == False:

                panel = Label(root, image=self.__greenlight)
                panel.image = self.__greenlight
                panel.pack()
                self.__opened=True

        root.update()
        root.after(500,self.update)

root = Tk()

separation_Signal = Separation_Signal(root)
root.resizable(height=250, width=422)
root.mainloop()