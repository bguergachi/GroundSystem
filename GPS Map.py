from tkinter import *
import tkinter.font as tkfont
import tkinter.messagebox
from time import sleep
import os,sys,random
from PIL import ImageTk,Image

root = Tk()

#Defines frame dimensions
height=250
width=422

root.resizable(width=False, height=False)
root.geometry('{}x{}'.format(width, height))

frame = Frame(root)
frame.pack()

#Loads Map
load_map = Image.open("Map Image.png")
load_map.thumbnail(size=(width, height))

#Loads Crosshair
load_crosshair = Image.open("Crosshair.png")
crosshair_size = (20, 20)
load_crosshair.thumbnail(size=(crosshair_size[0], crosshair_size[1]))

'''Coordinates of Map corners
topleft = 32.955651, -106.930123
topright = 32.955651, -106.892924
botleft = 32.937436, -106.930123
botright = 32.937436, -106.892924
'''

#Sets length and width of map frame in terms of latitude and longitude coordinates
latitude_top = 32.955651
latitude_bot = 32.937436
latitude_length = latitude_top - latitude_bot

longitude_right = 106.892924
longitude_left = 106.930123
longitude_length = longitude_left - longitude_right

#Derives proportionality between latitude/longitude coordinates and x,y direction pixels
y_relation = height/latitude_length
x_relation = width/longitude_length

#Converts latitude/longitude coordinates to x,y parameters
def convert_pixel(latitude, longitude):
    y = (latitude_top-latitude)*y_relation
    x = (longitude_left-(longitude*(-1)))*x_relation
    return y, x

#Random test coordinates
def getRandomNumber():
    rand_lat = round(random.uniform(latitude_bot, latitude_top), 6)
    rand_long = round(random.uniform(longitude_right, longitude_left), 6)*(-1)
    return rand_lat, rand_long

random_coordinate = getRandomNumber()
print(random_coordinate)

pixel_values = convert_pixel(random_coordinate[0], random_coordinate[1])
print(pixel_values)

#Seperates integer and decimals
pixel_integer = [int(pixel_values[0]), int(pixel_values[1])]
pixel_decimals = (pixel_values[0] % 1, pixel_values[1] % 1)
print(pixel_integer)
print(pixel_decimals)

#Displays Map and Crosshair
load_map.paste(load_crosshair,(pixel_integer[1]-int(crosshair_size[0]/2), pixel_integer[0]-int(crosshair_size[1]/2)), load_crosshair) #Positions and blends Crosshair with map
map = ImageTk.PhotoImage(load_map)
crosshair = ImageTk.PhotoImage(load_crosshair)
label_map = Label(frame, image=map)
label_map.pack()

#Notifies user if crosshair leaves map
if random_coordinate[0] > latitude_top or random_coordinate[0] < latitude_bot:
    tkinter.messagebox.showwarning('Warning', 'Rocket has left the competition area!!!')
    print("Rocket has left competition area!!!")
elif random_coordinate[1]*(-1) > longitude_left or random_coordinate[1]*(-1) < longitude_right:
    tkinter.messagebox.showwarning('Warning', 'Rocket has left the competition area!!!')
    print("Rocket has left competition area!!!")


root.mainloop()


