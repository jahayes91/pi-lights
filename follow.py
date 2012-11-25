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
  #Check button status
  input_value = gpio.input(pin_in[0])

  if input_value == False:
    for pins in pin_out:
      time.sleep(0.1)
      gpio.output(pins, gpio.HIGH)
      input_value = gpio.input(pin_in[0])

    time.sleep(0.1)

    for pins in pin_out:
      gpio.output(pins, gpio.LOW)

  else:
    for pins in sorted(pin_out, reverse=True):
      time.sleep(0.1)
      gpio.output(pins, gpio.HIGH)
      input_value = gpio.input(pin_in[0])

    time.sleep(0.1)

    for pins in pin_out:
      gpio.output(pins, gpio.LOW)


