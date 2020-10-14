#!/usr/bin/python3

import time
import serial
import argparse

relayon = [0xA0, 0x01, 0x01, 0xA2]
relaync = [0xA0, 0x01, 0x00, 0xA1]

parser = argparse.ArgumentParser()
parser.add_argument("port", help="The port the relay is connected to")
parser.add_argument("operation", help="Which operation to execute, NC, NO or status")
parser.parse_args()

args = parser.parse_args()

# case insensitive
port = args.port.lower()
operation = args.operation.lower()

ser = serial.Serial(port, 9600, timeout=1)

if operation == "no":
    ser.write(relayon)
elif operation == "nc":
    ser.write(relaync)
elif operation == "status":
    print("Not implemented")   
else:
    print("Unknown option: Only NC, NO or status are supported")

ser.close()