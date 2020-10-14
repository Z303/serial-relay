#!/usr/bin/python3

import time
import serial
import argparse

baudrate = 9600

def relay_write(channel, state):
    command = 0xA0
    check = command + channel + state
    message = [command, channel, state, check]

    ser.write(message)

parser = argparse.ArgumentParser()
parser.add_argument("port", help="The port the relay is connected to")
parser.add_argument("operation", help="Which operation to execute: open, close or status")
parser.parse_args()

args = parser.parse_args()

# case insensitive
port = args.port.lower()
operation = args.operation.lower()

ser = serial.Serial(port, baudrate, timeout=1)

if operation == "open":
    relay_write(1, 1)
elif operation == "close":
    relay_write(1, 0)
elif operation == "status":
    print("Not implemented")   
else:
    print("Unknown option: Only NC, NO or status are supported")

ser.close()