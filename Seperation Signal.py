from tkinter import *

root = Tk()
root.title("Separation Signal")

def window(main):
    main.title('Altimeter')
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

mainFrame = Frame(root)
mainFrame.pack()

var1 = StringVar(mainFrame)

sensor = Label(mainFrame, height=50, width=200, font='size, 25', fg='green', textvariable=var1)
sensor.place(relx=0.5, rely=0.5, anchor=CENTER)
sensor.pack()

state = 0

def update():
    displayText = ''

    global state
    if state == 0:
        displayText = 'Didnt'

    elif state == 1:
        displayText = 'Separated'

    var1.set(displayText)
    print(var1)
    mainFrame.update()

def mainloop():
    while True:
        update()

root.resizable(height=250, width=422)
mainloop()