#!/usr/bin/python3

import serial
import argparse

baudrate = 9600

setstate = 0xA0

def relay_write(command, relay, state):
    channel = relay + 1
    check = command + channel + state
    message = [command, channel, state, check]

    ser.write(message)

parser = argparse.ArgumentParser()
parser.add_argument("port", help="The port the relay is connected to")
parser.add_argument("channel", type=int, help="The channel to control")
parser.add_argument("operation", help="Which operation to execute: open or close")
parser.parse_args()

args = parser.parse_args()

# case insensitive
port = args.port.lower()
operation = args.operation.lower()

channel = args.channel

ser = serial.Serial(port, baudrate, timeout=1)

if operation == "open":
    relay_write(setstate, channel, 1)
elif operation == "close":
    relay_write(setstate, channel, 0)
else:
    print("Unknown option: Only open or close are supported")

ser.close()