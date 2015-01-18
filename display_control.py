# -*- coding: utf-8 -*-

#Import library
import RPi.GPIO as G
from time import sleep

#BCM - numbers of GPIOs
G.setmode(G.BCM)

#Actual numbers of pins, alphabetical order
pins = [7,8,11,10,22,25,9]

#Set pins to output
for pin in pins:
	G.setup(pin, G.OUT)	

#Define states of pins
zero = 	[1,1,1,1,1,1,0]
one = 		[0,1,1,0,0,0,0]
two = 		[1,1,0,1,1,0,1]
three = 	[1,1,1,1,0,0,1] 
four = 	[0,1,1,0,0,1,1]
five = 	[1,0,1,1,0,1,1]
six = 		[1,0,1,1,1,1,1]
seven = 	[1,1,1,0,0,0,0]
eight = 	[1,1,1,1,1,1,1]
nine = 	[1,1,1,1,0,1,1]

#main function
def seven_segment(number, polarity = "anode"):
	
	values = {
		0 : zero,
		1 : one,
		2 : two,
		3 : three,
		4 : four,
		5 : five,
		6 : six,
		7 : seven,
		8 : eight,
		9 : nine
	}
	
	for pin, level in zip(pins, values[number]):
		G.output(pin, not level)
		
	if polarity == "catode":
		for pin, level in zip(pins, values[number]):
				G.output(pin, level)

#usage - seven_segment(your_number)
	
G.cleanup()
