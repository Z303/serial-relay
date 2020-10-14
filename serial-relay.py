#!/usr/bin/python3

import time
import serial

port = 'COM3'
ser = serial.Serial(port, 9600, timeout=1)

turnon = [0xA0, 0x01, 0x01, 0xA2]
turnoff = [0xA0, 0x01, 0x00, 0xA1]

ser.write(turnon)
print('ON')
time.sleep(1)
ser.write(turnoff)
print('OFF')
ser.close()