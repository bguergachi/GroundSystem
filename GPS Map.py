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

'''Sets length and width of map frame in terms of latitude and longitude coordinates'''
latitude_top = 32.955651
latitude_bot = 32.937436
latitude_length = latitude_top - latitude_bot

longitude_right = 106.892924
longitude_left = 106.930123
longitude_length = longitude_left - longitude_right

'''Derives proportionality between latitude/longitude coordinates and x,y direction pixels'''
y_relation = height/latitude_length
x_relation = width/longitude_length

'''Converts latitude/longitude coordinates to x,y parameters'''

def convert(latitude, longitude):
    y = (latitude-latitude_bot)*y_relation
    x = (longitude_left-(longitude*(-1)))*x_relation
    return x, y

'''Gets the latitude and longitude coordinates'''
getLatitude()
getLongitude()
'''Eg. latitude = 32.949512, longitude = -106.911585'''

root.mainloop()


