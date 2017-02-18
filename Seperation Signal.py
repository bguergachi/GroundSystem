from tkinter import *
from PIL import ImageTk, Image

root = Tk()

def window(main):
    main.title('Separation Signal')
    height = 250
    width = 422
    root.geometry('{}x{}'.format(width, height))

window(root)

def printdseparate():
    global state
    state=0

def printseparate():
    global state
    state = 1

state = 0
opened=False

redlight = ImageTk.PhotoImage(Image.open("C:/Users/shiva/PycharmProjects/GroundSystem/redlight.png"))
greenlight = ImageTk.PhotoImage(Image.open("C:/Users/shiva/PycharmProjects/GroundSystem/greenlight.png"))

def update():


    global root,opened,state,redlight,greenlight

    if state == 0:

        if opened==False:

            print('open image')

            panel = Label(root, image=redlight)
            panel.image = redlight
            panel.pack()

            opened=True

    elif state == 1:

        if opened==False:

            panel = Label(root, image=greenlight)
            panel.image = greenlight
            panel.pack()

            opened=True

    root.update()

def mainloop():

    while True:
        update()

root.resizable(height=250, width=422)
mainloop()