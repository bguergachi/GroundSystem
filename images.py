from tkinter import *
import tkinter.font as tkfont
from time import sleep
import os,sys,random
from PIL import ImageTk,Image



# *****************************GUI PORTION************************************
height = 422
width = 250

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
    def getimages(self):
        return rocket

    def showimage(self):
        
        if units == 1:  # radio button value for imperial units is 1
            print("display imperial units")
        else:
            print("display metric units")