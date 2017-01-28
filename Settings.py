#Created on Sat Jan 28 11:09:59 2017

#@author: Alejandra Zavala

from tkinter import *
global imp, met, portLab, ser1,ser2,ser3

#***************FUNCTIONS************************

def hover_color(widget, color, event): # function changes color of button when hovering above it
    widget.config(foreground=color)

def close_popup(root):
    root.destroy()



def cancel_confirm():
    popup = Tk()
    popup.geometry('75*50')
    popup.title('Abandon Settings')

    cancel_txt= Label(popup, text="No unsaved changes will be applied. ")
    cancel_txt.pack()

    cancel_bttn= Button(popup,text= "OK", command = close_popup(popup))
    cancel_bttn.pack()
    return()

def update_confirm():
    popup = Tk()
    popup.geometry('50*50')
    popup.title('Confirm Updates')

    update_txt=Label(popup, text="New settings have been saved. ")
    update_txt.pack()

    update_bttn=Button(popup,text= "OK", command = close_popup(popup))
    update_bttn.pack()

    return()


root = Tk() #root is the "name of the window that will contain the GUI
root.geometry('422x250') # this function defines the size of the window
root.title('Settings Menu') # this function names the overall window
root.configure( background = "snow",)

Frame1 = Frame(root, bg="khaki",relief="sunken", width=100, height=220)
Frame1.grid(row = 0, column = 0, rowspan = 3, columnspan = 2, sticky = W+E+N+S, padx= 5)

#***************************************************************************
Units = Label(root, text = "Unit Selection").grid(row=0,column=0)
imp = IntVar()
imperial = Checkbutton(root, text = "imperial",anchor = SW,width = 10,bg ="khaki", variable = imp,onvalue = 1, offvalue = 0).grid(row = 1, column = 0)

met = IntVar()
metric = Checkbutton(root,text ="metric",anchor= SW, width = 10, bg ="khaki",variable = met,onvalue = 1, offvalue = 0).grid(row=2,column=0)

#****************************************************************************


# ***************************************************************************
Frame2 = Frame(root,bg="lightcyan1",borderwidth=5, relief="sunken", width=300, height=220)
Frame2.grid(row = 0, column = 2, rowspan = 7, columnspan = 2, sticky = W+E+N+S)

Port_Title = Label(root, text= "Port Selection Menu ", bg ="lightcyan1").grid(row =0, column =2)
Avail = Listbox(root)
Avail.config(width=30)
Avail.insert(1,"GPIO")
Avail.insert(2,"USB1")
Avail.insert(3,"USB2")
Avail.config(width = 25)
Avail.grid(row=1,column=2,rowspan =5, columnspan = 1)

#****************************************************************************
Frame2 = Frame(root, bg="navy",relief="sunken", width=420, height=30)
Frame2.grid(row = 7, column = 0, rowspan = 1, columnspan = 3, sticky = W+E+N+S)
Label(root, bg ="navy").grid(row=7, column=0)

update = Button(root, text =" Update Settings ", width = 15, height=1)
update.grid(row=7, column = 2)
update.bind("<Enter>",hover_color(update,"green",'Motion>'))

cancel= Button(root, text =" Cancel", width = 10, height=1)
cancel.grid(row=7,column= 0)

root.mainloop()