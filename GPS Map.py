from tkinter import *
import tkinter.font as tkfont
from time import sleep
import os,sys,random
from PIL import ImageTk,Image

root = Tk()

'''Defines frame dimensions'''

height=250
width=422
root.resizable(width=False, height=False)
root.geometry('{}x{}'.format(width, height))

frame = Frame(root)
frame.pack()

'''Shows Map'''

load = Image.open("Map Image.png")
load.thumbnail(size=(width, height))

map = ImageTk.PhotoImage(load)
label = Label(frame, image=map)
label.pack()

'''Coordinates of map corners
topleft = 32.955651, -106.930123
topright = 32.955651, -106.892924
botleft = 32.937436, -106.930123
botright = 32.937436, -106.892924
'''
'''Sets length and width of map frame in terms of longitude and latitude coordinates'''
longitude_right = 106.892924
longitude_left = 106.930123
longitude_length = longitude_left - longitude_right

latitude_top = 32.955651
latitude_bot = 32.937436
latitude_length = latitude_top - latitude_bot

'''Derives proportionality between longitude/latitude coordinates and x,y direction pixels'''
x_relation = longitude_length/width
y_relation = latitude_length/height



'''Converts latitude/longitude coordinates to x,y parameters'''

#def convert(latitude, longitude)




root.mainloop()


