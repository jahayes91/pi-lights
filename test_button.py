# Import required modules
import RPi.GPIO as gpio

# Assign variables
but_count = 0

# Setup pin 17 as an input
gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.IN)

while True:
  input_value = gpio.input(17)

  if input_value == False:
    but_count = but_count + 1

    if but_count > 2:
      but_count = 0
    
    # input_value = True
    while input_value == False:
      input_value = gpio.input(17)

  if but_count == 0:
    print "Program 1"

  if but_count == 1:
    print "Program 2"

  if but_count == 2:
    print "Program 3"
