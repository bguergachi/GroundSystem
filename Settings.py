#Created on Sat Jan 28 11:09:59 2017

#@author: Alejandra Zavala

from tkinter import *
import tkinter.font as tkfont
from time import sleep
import os,sys,random
from PIL import ImageTk,Image


# *****************************GUI PORTION************************************
height = 422
width = 250
units = 0
ports = 0

class Display:
    def __init__(self, root):
        self.__root = root
        # Set window parameters
        self.__root.resizable(width=False, height=False)
        self.__root.geometry('{}x{}'.format(height, width))
        self.__root.title('Settings Menu') # this function names the overall window
        self.__root.configure(background="snow")
        self.send_settings()
        self.get_availPorts()
        self.formx()


    # ***************FUNCTIONS************************
    # units are no longer in use
        # "def send_settings(self):
        #global units, ports# function that tells status menu which units to display
        #if units == 1:  # radio button value for imperial units is 1
            #print("display imperial units")
        #else:
            #print("display metric units")"

    # need to update once we figure out the uart stuff
    def get_availPorts(self):  # function outputs list of ports avilable
        ports = ["port1", "port2", "port3", "port4", "port5", "port6"]
        return (ports)
    def send_settings(selfself):
        return ()

    def hover_color(self, widget, color):  # function changes color of button when hovering above it
        widget.config(bg=color)  # backgrounf color widget configuration

    def close_popup(self,root):  # closes popup window , used in cancel_confirm function
        root.destroy()  # ___.destroy() closes the window

    def update_confirm(self,mssg):  # pop-up message window to confirm action
        popup = Tk()
        popup.geometry('200x70')
        popup.title('Confirm Updates')

        update_txt = Label(popup, text=mssg)
        update_txt.pack()

        update_bttn = Button(popup, text="OK")
        update_bttn.bind("<Button-1>", lambda event: self.close_popup(popup))
        update_bttn.pack()
        return ()

    # need to update once we figure out the uart stuff
    def select_port(self,listb):  # sends port selection to pywire
        list_num = listb.curselection()  # outputs the index of the selected port from the listbox
        return (list_num)

    def formx(self):
        frame1 = Frame(self.__root, bg="khaki",relief="sunken", width=100, height=220)#everything after root is juts formattign settings
        frame1.grid(row = 0, column = 0, rowspan = 3, columnspan = 2, sticky = W+E+N+S, padx= 5) # formatting locations and span of widget

        #************** UNITS SLECTION SUBMENU**********************************
        #unit_label = Label(self.__root, text = "Unit Selection", bg="goldenrod3",font="Verdana 9 bold",height=2).grid(row=0,column=0)#title of subsection
        #units= IntVar()# variable will hold variable value assigned to each radiobutton

        #used radiobutton because they only admit one selection (either metric or imperial)
        #imperial = Radiobutton(self.__root, text = "Imperial",font="Verdana 9 bold",anchor = SW,width = 10,bg ="khaki", variable = units,value =1)
        #imperial.grid(row = 1, column = 0)

        #metric = Radiobutton(self.__root,text ="Metric",font="Verdana 9 bold",anchor= SW, width = 10, bg ="khaki",variable = units,value=2)
        #metric.grid(row=2,column=0)

        # *******************AVAILABLE PORTS LIST ******************************
        frame2 = Frame(self.__root,bg="lightcyan1",borderwidth=5, relief="sunken", width=300, height=220)
        frame2.grid(row = 0, column = 2, rowspan = 7, columnspan = 3, sticky = W+E+N+S)

        #port_img = Label(root,image=logo,justify=LEFT).grid(row=0,column=3)
        logo=PhotoImage(file='rocketry-smaller.gif')
        port_Title = Label(self.__root, compound=RIGHT,text= "Port Selection Menu ",image=logo, bg ="blue4",width=275,fg= 'white',font="Verdana 10 bold").grid(row =0, column =2)
        avail = Listbox(self.__root,height=7)

        ports = self.get_availPorts() # function outputs a list with available ports

        for port in ports: # for all items in the ports list
            avail.insert(END,port) #insert the item in the listbox

        avail.config(width = 20)#formatting
        avail.bind('<<ListboxSelect>>', lambda event: self.select_port(avail)) # lamda function gets invoked after <<Event>>
        avail.grid(row=1,column=2,rowspan =5, columnspan = 1)

        #************UPDATE/CANCEL BUTTONS *************************************
        Frame2 = Frame(self.__root, bg="slate gray",relief="sunken", width=420, height=30)
        Frame2.grid(row = 7, column = 0, rowspan = 1, columnspan = 3, sticky = W+E+N+S)
        Label(self.__root, bg ="navy").grid(row=7, column=0)

        update = Button(self.__root, text =" Update Settings ", width = 20, height=1,relief = RAISED)
        update.bind("<Button-1>",lambda event: self.update_confirm("New settings \nhave been saved. "))
        update.grid(row=7, column = 2)

        cancel= Button(self.__root, text =" Cancel", width = 10, height=1,relief=GROOVE)
        cancel.bind("<Button-1>",lambda event: self.update_confirm("Unsaved setting will be lost. "))
        cancel.grid(row=7,column= 0)

    #def getunits(self):#fucntion that returns unit option
        #return units

    def getports(selfself):#function that returns port option
        return ports
if __name__ == '__main__':
    root2= Tk()
    display=Display(root2)
    root2.mainloop()