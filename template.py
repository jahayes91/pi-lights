#!/usr/bin/python -tt

import RPi.GPIO as gpio
import time

# Set GPIO mode
gpio.setmode(gpio.BCM)

# Define in pins
pin_in = [17]
for pins in pin_in:
  gpio.setup(pins, gpio.IN)

# Define out pins
pin_out = [14, 15, 18, 23]
for pins in pin_out:
  gpio.setup(pins, gpio.OUT)

for pins in pin_out:
  gpio.output(pins, gpio.LOW)

# Main program
while True: 
