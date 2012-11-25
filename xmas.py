#import required modules
import RPi.GPIO as gpio
import time

# Define GPIO pins IN and OUT
pin_in = [17]
pin_out = [14, 15, 18, 23]


# Set mode
gpio.setmode(gpio.BCM)

# Initilise pins IN
for pins in pin_in:
  print gpio.setup(pins, gpio.IN)

#Initilise pins OUT

for pins in pin_out:
  print gpio.setup(pins, gpio.OUT)
