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

# Test Program 1
while True:
  input_value = gpio.input(17)

  if input_value == False:
    but_count = but_count + 1

    if but_count > 1:
      but_count = 0

    while input_value == False:
      input_value = gpio.input(17)

  if but_count == 0:

    for pins in pin_out:
      time.sleep(0.1)
      gpio.output(pins, gpio.HIGH)
 
    time.sleep(0.1)

    for pins in pin_out:
      gpio.output(pins, gpio.LOW)

      if input_value == False:
        break

  if but_count == 1:

    for pins in pin_out:
      gpio.output(pins, gpio.HIGH)

    time.sleep(0.7)

    for pins in pin_out:
      gpio.output(pins, gpio.LOW)

    time.sleep(0.7)
