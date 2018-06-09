import sys, os
import RPi.GPIO as GPIO


def setupLED():
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(29, GPIO.OUT)
    GPIO.setup(31, GPIO.OUT)
    GPIO.setup(32, GPIO.OUT)
    GPIO.setup(33, GPIO.OUT)
    GPIO.setup(35, GPIO.OUT)
    GPIO.setup(36, GPIO.OUT)


def greenLED(switch):
    GPIO.output(39, switch)


def redLED(switch):
    GPIO.output(31, switch)


def slowRGB1(switch):
    GPIO.output(32, switch)


def slowRGB2(switch):
    GPIO.output(33, switch)


def fastRGB1(switch):
    GPIO.output(35, switch)


def fastRGB2(switch):
    GPIO.output(36, switch)
