import sys, os
import RPi.GIPO as GPIO


def setupLED(self):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(19, GPIO.OUT)
    GPIO.setup(21, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(24, GPIO.OUT)
    GPIO.setup(26, GPIO.OUT)


def greenLED(self, switch):
    GPIO.output(19, switch)


def redLED(self, switch):
    GPIO.output(21, switch)


def slowRGB1(self, switch):
    GPIO.output(22, switch)


def slowRGB2(self, switch):
    GPIO.output(23, switch)


def fastRGB1(self, switch):
    GPIO.output(24, switch)


def fastRGB2(self, switch):
    GPIO.output(26, switch)
