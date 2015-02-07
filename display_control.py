# -*- coding: utf-8 -*-

#Import library
import RPi.GPIO as G
from time import sleep

#BCM - numbers of GPIOs
G.setmode(G.BCM)

#Actual numbers of diplay pins, [a,b,c,d,e,f,g]
display_pins = [2,3,17,27,22,10,4]

#MUX pins, 11 - first digit, 9 - second digit
mux_pins = [11,9]

#Set dislay pins to output
for display_pin in display_pins:
	G.setup(display_pin, G.OUT)	

G.setup(11, G.OUT)
G.setup(9, G.OUT)		

#Define states of pins
zero = 		[1,1,1,1,1,1,0]
one = 		[0,1,1,0,0,0,0]
two = 		[1,1,0,1,1,0,1]
three = 	[1,1,1,1,0,0,1] 
four = 		[0,1,1,0,0,1,1]
five = 		[1,0,1,1,0,1,1]
six = 		[1,0,1,1,1,1,1]
seven = 	[1,1,1,0,0,0,0]
eight = 	[1,1,1,1,1,1,1]
nine = 		[1,1,1,1,0,1,1]

empty_char =[0,0,0,0,0,0,0]
minus =		[0,0,0,0,0,0,1]

#Match values with numbers
values = {
		"0" : zero,
		"1" : one,
		"2" : two,
		"3" : three,
		"4" : four,
		"5" : five,
		"6" : six,
		"7" : seven,
		"8" : eight,
		"9" : nine,
		"-" : minus,
		" " : empty_char
	}

#main function
def seven_segment(number, empty_char = False, polarity = "anode"):
	
	for pin, level in zip(display_pins, values[number]):
		G.output(pin, not level)
		
	if polarity == "catode":
		for pin, level in zip(display_pins, values[number]):
				G.output(pin, level)

seven_segment("8")
