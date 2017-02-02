#Created on Sat Jan 28 11:09:59 2017

#@author: Alejandra Zavala

from tkinter import *
global imp, met, portLab, ser1,ser2,ser3

#***************FUNCTIONS************************

def hover_color(widget, color): # function changes color of button when hovering above it
    widget.config(bg =color)

def close_popup(root):
    root.destroy()

def cancel_confirm():
    popup = Tk()
    popup.geometry('200x70')
    popup.title('Confirm Updates')

    update_txt = Label(popup, text="Unsaved setting will be lost. ")
    update_txt.pack()

    update_bttn = Button(popup, text="OK")
    update_bttn.bind("<Button-1>", lambda event: close_popup(popup))
    update_bttn.pack()
    return ()

def update_confirm():
    popup = Tk()
    popup.geometry('200x70')
    popup.title('Confirm Updates')

    update_txt=Label(popup, text="New settings \nhave been saved. ")
    update_txt.pack()

    update_bttn=Button(popup,text= "OK")
    update_bttn.bind("<Button-1>", lambda event: close_popup(popup))
    update_bttn.pack()
    return()

def disable_check(var1,var2):
    B1= var1.get()
    B2= var2.get()
    if ((B1 and B2)==1):
        popup = Tk()
        popup.geometry('200x70')
        popup.title('ERROR!')

        error_txt = Label(popup, text="ERROR:Select only ONE\n option. ")
        error_txt.pack()

        update_bttn = Button(popup, text="OK")
        update_bttn.bind("<Button-1>", lambda event: close_popup(popup))
        update_bttn.pack()
    return()

def avail_ports():
    return()

def select_port():
    return()



# *****************************GUI PORTION************************************
#*****************************************************************************

root = Tk() #root is the "name of the window that will contain the GUI
root.geometry('422x250') # this function defines the size of the window
root.title('Settings Menu') # this function names the overall window
root.configure( background = "snow",)

frame1 = Frame(root, bg="khaki",relief="sunken", width=100, height=220)
frame1.grid(row = 0, column = 0, rowspan = 3, columnspan = 2, sticky = W+E+N+S, padx= 5)

#************** UNITS SLECTION SUBMENU***********************************
units = Label(root, text = "Unit Selection", bg="khaki").grid(row=0,column=0)
imp = IntVar()
met = IntVar()

imperial = Checkbutton(root, text = "imperial",anchor = SW,width = 10,bg ="khaki", variable = imp)
imperial.bind("<Button-1>", lambda event: disable_check(imp,met))
imperial.grid(row = 1, column = 0)

metric = Checkbutton(root,text ="metric",anchor= SW, width = 10, bg ="khaki",variable = met)
metric.bind("<Button-1>", lambda event: disable_check(imp,met))
metric.grid(row=2,column=0)
#****************************************************************************


# *******************AVAILABLE PORTS LIST ******************************
frame2 = Frame(root,bg="lightcyan1",borderwidth=5, relief="sunken", width=300, height=220)
frame2.grid(row = 0, column = 2, rowspan = 7, columnspan = 2, sticky = W+E+N+S)

port_Title = Label(root, text= "Port Selection Menu ", bg ="lightcyan1").grid(row =0, column =2)
avail = Listbox(root)
avail.config(width=30)
avail.insert(1,"GPIO")
avail.insert(2,"USB1")
avail.insert(3,"USB2")
avail.config(width = 25)
avail.grid(row=1,column=2,rowspan =5, columnspan = 1)

#************UPDATE/CANCEL BUTTONS *************************************
Frame2 = Frame(root, bg="navy",relief="sunken", width=420, height=30)
Frame2.grid(row = 7, column = 0, rowspan = 1, columnspan = 3, sticky = W+E+N+S)
Label(root, bg ="navy").grid(row=7, column=0)

update = Button(root, text =" Update Settings ", width = 20, height=1)
update.bind("<Button-1>",lambda event: update_confirm())
update.bind("<B1-Motion>", lambda event:hover_color(update,"green"))
update.grid(row=7, column = 2)

cancel= Button(root, text =" Cancel", width = 10, height=1)
cancel.bind("<Button-1>",lambda event: update_confirm())
cancel.grid(row=7,column= 0)

root.mainloop()