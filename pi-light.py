import RPi.GPIO as gpio

#Set mode
gpio.setmode(gpio.BCM)

#Set pins IN
gpio.setup(17, gpio.IN)

#Set pins OUT
gpio.setup(14, gpio.OUT)
gpio.setup(15, gpio.OUT)
gpio.setup(18, gpio.OUT)
gpio.setup(23, gpio.OUT)

#Set pins to low
gpio.output(14, gpio.LOW)
gpio.output(15, gpio.LOW)
gpio.output(18, gpio.LOW)
gpio.output(23, gpio.LOW)

#Loop LED's from 14 to 23
while True:
	gpio.output(14, gpio.HIGH)
	gpio.output(15, gpio.HIGH)
	gpio.output(18, gpio.HIGH)
	gpio.output(23, gpio.HIGH)
