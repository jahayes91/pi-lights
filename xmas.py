#!/usr/bin/python -tt

# import required modules
import RPi.GPIO as gpio
import time

# Assign variables
but_count = 0

# Define GPIO pins IN and OUT
pin_in = [17]
pin_out = [14, 15, 18, 23]


# Set mode
gpio.setmode(gpio.BCM)

# Initilise pins IN
for pins in pin_in:
  gpio.setup(pins, gpio.IN)

# Initilise pins OUT
for pins in pin_out:
 gpio.setup(pins, gpio.OUT)

for pins in pin_out:
  gpio.output(pins, gpio.LOW)

# Keep Program looping
while True:

  # Check button status
  input_value = gpio.input(17)
  
  # Increment Button Count
  if input_value == False:
    but_count = but_count + 1

    # Loop button count
    if but_count > 1:
      but_count = 0

    
    while input_value == False:
      input_value = gpio.input(17)

  # If button count if 0 then run first light program
  if but_count == 0:

    # Loop through pins and switch each one on
    for pins in pin_out:
      time.sleep(0.1)
      gpio.output(pins, gpio.HIGH)
      input_value == gpio.input(pin_in[0])
    time.sleep(0.1)
    
    # Switch off all pins to begin another iteration
    for pins in pin_out:
      gpio.output(pins, gpio.LOW)
      input_value == gpio.input(pin_in[0])

  # If count = 1 run second light program
  if but_count == 1:

    # Turn all pins on
    for pins in pin_out:
      gpio.output(pins, gpio.HIGH)
      input_value == gpio.input(pin_in[0])
    
    # Wait .7 of a second
    time.sleep(0.4)

    # Turn all pins off
    for pins in pin_out:
      gpio.output(pins, gpio.LOW)
      input_value == gpio.input(pin_in[0])
    
    # Wait .7 of a second
    time.sleep(0.4)
