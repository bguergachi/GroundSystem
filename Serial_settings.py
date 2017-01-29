from Serial import *


def check_ports():
    avail_ports = []
    ser = Serial('/dev/ttyAMA0')
    ser1 = Serial('/dev/ttyUSB0')
    ser2 = Serial('/dev/ttyUSB1')

    if (ser.isOpen() == True): {  # if port is open
        avail_ports.append("GPIO")}

    if (ser.isOpen() == True): {  # if port is open
        avail_ports.append("USB1")}

    if (ser.isOpen() == True): {  # if port is open
        avail_ports.append("USB2")}
    return ()

