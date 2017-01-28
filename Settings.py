#Created on Sat Jan 28 11:09:59 2017

#@author: Alejandra Zavala


from tkinter import *
global imp, met, portLab, ser1,ser2,ser3



root = Tk() #root is the "name of the window that will contain the GUI
root.geometry('422x250') # this function defines the size of the window
root.title('Settings Menu') # this function names the overall window
root.configure( background = "snow",)

Frame1 = Frame(root, bg="khaki")
Frame1.grid(row = 0, column = 0, rowspan = 3, columnspan = 1, sticky = W+E+N+S)

#***************************************************************************
Units = Label(root, text = "Unit Selection").grid(row=0,column=0)
imp = IntVar()
imperial = Checkbutton(root, text = "imperial",anchor = SW,width = 20,bg ="khaki", variable = imp,onvalue = 1, offvalue = 0).grid(row = 1, column = 0)

met = IntVar()
metric = Checkbutton(root,text ="metric",anchor= SW, width = 20, bg ="khaki",variable = met,onvalue = 1, offvalue = 0).grid(row=2,column=0)

#****************************************************************************


# ***************************************************************************

Avail = Listbox(root)
Avail.insert(1,"GPIO")
Avail.insert(2,"USB1")
Avail.insert(3,"USB2")
Avail.config(width = 25)
Avail.grid(row=1,column=1)

#****************************************************************************
Frame2 = Frame(root, bg="navy")
Frame2.grid(row = 7, column = 0, rowspan = 4, columnspan = 2, sticky = W+E+N+S)
Label(root, bg ="navy").grid(row=7, column=0)

Update = Button(root, text =" update settings", width = 15, height=1).grid(row=8, column = 0)

root.mainloop()