#!/usr/bin/python3

import time
import serial
import argparse

relayopen = [0xA0, 0x01, 0x01, 0xA2]
relayclose = [0xA0, 0x01, 0x00, 0xA1]

baudrate = 9600

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
    ser.write(relayopen)
elif operation == "close":
    ser.write(relayclose)
elif operation == "status":
    print("Not implemented")   
else:
    print("Unknown option: Only NC, NO or status are supported")

ser.close()