#Created on Sat Jan 28 11:09:59 2017

#@author: Alejandra Zavala

from tkinter import *
global units, ports
#***************FUNCTIONS************************

def hover_color(widget, color): # function changes color of button when hovering above it
    widget.config(bg =color) #backgrounf color widget configuration

def close_popup(root): # closes popup window , used in cancel_confirm function
    root.destroy() # ___.destroy() closes the window

def update_confirm(mssg): #pop-up message window to confirm action
    popup = Tk()
    popup.geometry('200x70')
    popup.title('Confirm Updates')

    update_txt=Label(popup, text= mssg)
    update_txt.pack()

    update_bttn=Button(popup,text= "OK")
    update_bttn.bind("<Button-1>", lambda event: close_popup(popup))
    update_bttn.pack()
    return()

def send_settings(): # function that tells status menu which units to display
    if units==1: # radio button value for imperial units is 1
        print("display imperial units")
    else:
        print("display metric units")

# need to update once we figure out the uart stuff
def get_availPorts(): #function outputs list of ports avilable
    ports = ["port1", "port2", "port3", "port4", "port5", "port6"]
    return(ports)

# need to update once we figure out the uart stuff
def select_port(listb): # sends port selection to pywire
    list_num = listb.curselection() # outputs the index of the selected port from the listbox
    return(list_num)

# *****************************GUI PORTION************************************
#*****************************************************************************

root = Tk() #root is the "name of the window that will contain the GUI
root.geometry('422x250') # this function defines the size of the window
root.title('Settings Menu') # this function names the overall window
root.configure( background = "snow")
#logo=PhotoImage(file=C:\Users\Alejandra Zavala\Desktop\rocketry.gif)

frame1 = Frame(root, bg="khaki",relief="sunken", width=100, height=220)#everything after root is juts formattign settings
frame1.grid(row = 0, column = 0, rowspan = 3, columnspan = 2, sticky = W+E+N+S, padx= 5) # formatting locations and span of widget

#************** UNITS SLECTION SUBMENU***********************************
unit_label = Label(root, text = "Unit Selection", bg="goldenrod3",font="Verdana 9 bold").grid(row=0,column=0)#title of subsection
units= IntVar()# variable will hold variable value assigned to each radiobutton

#used radiobutton because they only admit one selection (either metric or imperial)
imperial = Radiobutton(root, text = "Imperial",font="Verdana 9 bold",anchor = SW,width = 10,bg ="khaki", variable = units,value =1)
imperial.grid(row = 1, column = 0)

metric = Radiobutton(root,text ="Metric",font="Verdana 9 bold",anchor= SW, width = 10, bg ="khaki",variable = units,value=2)
metric.grid(row=2,column=0)

# *******************AVAILABLE PORTS LIST ******************************
frame2 = Frame(root,bg="lightcyan1",borderwidth=5, relief="sunken", width=300, height=220)
frame2.grid(row = 0, column = 2, rowspan = 7, columnspan = 2, sticky = W+E+N+S)

port_Title = Label(root, text= "Port Selection Menu ", bg ="blue4",fg= 'white',font="Verdana 10 bold").grid(row =0, column =2)
avail = Listbox(root,height=7)

ports = get_availPorts() # function outputs a list with available ports

for port in ports: # for all items in the ports list
    avail.insert(END,port) #insert the item in the listbox

avail.config(width = 25)#formatting
avail.bind('<<ListboxSelect>>',lambda event:select_port(avail)) # lamda function gets invoked after <<Event>>
avail.grid(row=1,column=2,rowspan =5, columnspan = 1)



#************UPDATE/CANCEL BUTTONS *************************************
Frame2 = Frame(root, bg="slate gray",relief="sunken", width=420, height=30)
Frame2.grid(row = 7, column = 0, rowspan = 1, columnspan = 3, sticky = W+E+N+S)
Label(root, bg ="navy").grid(row=7, column=0)

update = Button(root, text =" Update Settings ", width = 20, height=1,relief = RAISED)
update.bind("<Button-1>",lambda event: update_confirm("New settings \nhave been saved. "))
update.grid(row=7, column = 2)

cancel= Button(root, text =" Cancel", width = 10, height=1,relief=GROOVE)
cancel.bind("<Button-1>",lambda event: update_confirm("Unsaved setting will be lost. "))
cancel.grid(row=7,column= 0)

root.mainloop()