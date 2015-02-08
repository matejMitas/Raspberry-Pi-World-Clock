# -*- coding: utf-8 -*-

from __future__ import division

#Import library
import RPi.GPIO as G
from time import sleep, time

#BCM - numbers of Gs
G.setmode(G.BCM)

G.setwarnings(False)

#set refresh rate	
refresh_rate = 400 # in Hz

#Actual numbers of diplay pins, [a,b,c,d,e,f,g]
display_pins = [2,3,17,27,22,10,4]

#MUX pins, 9 - first digit, 11 - second digit
mux_pins = [11,9,23,24]

#Set dislay pins to output
for display_pin in display_pins:
	G.setup(display_pin, G.OUT)	

for mux_pin in mux_pins:
	G.setup(mux_pin, G.OUT)		

#Define states of pins
# zero = 		[1,1,1,1,1,1,0]
# one = 		[0,1,1,0,0,0,0]
# two = 		[1,1,0,1,1,0,1]
# three = 	[1,1,1,1,0,0,1] 
# four = 		[0,1,1,0,0,1,1]
# five = 		[1,0,1,1,0,1,1]
# six = 		[1,0,1,1,1,1,1]
# seven = 	[1,1,1,0,0,0,0]
# eight = 	[1,1,1,1,1,1,1]
# nine = 		[1,1,1,1,0,1,1]

zero = 		[1,1,1,1,1,1,0]
one = 		[0,0,0,0,1,1,0]
two = 		[1,1,0,1,1,0,1]
three = 	[1,0,0,1,1,1,1] 
four = 		[0,0,1,0,1,1,1]
five = 		[1,0,1,1,0,1,1]
six = 		[1,1,1,1,0,1,1]
seven = 	[0,0,0,1,1,1,0]
eight = 	[1,1,1,1,1,1,1]
nine = 		[1,0,1,1,1,1,1]

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

	  

# def my_callback(channel): 
# 	print "mínus jeden rok"
# 	hack = 2015 + 1
# 	show_four_chars(hack)

# def my_callback3(channel):  
# 	print "standart"
# 	hack = 2015
# 	show_four_chars(hack)

# def my_callback2(channel):  
# 	print "plus jeden rok" 
# 	hack = 2015 - 1
# 	show_four_chars(hack)

# G.setup(25, G.IN, pull_up_down=G.PUD_DOWN)
# G.setup(7, G.IN, pull_up_down=G.PUD_DOWN)   
# G.setup(8, G.IN, pull_up_down=G.PUD_DOWN)          
	 
# G.add_event_detect(25, G.RISING, callback=my_callback, bouncetime=200)
# G.add_event_detect(7, G.RISING, callback=my_callback2, bouncetime=200)  
# G.add_event_detect(8, G.RISING, callback=my_callback3, bouncetime=200) 		

#main function
def show_four_chars(inp, polarity = "anode"):

	#parse input
	chars = list(str(inp))
	
	if len(chars) < 4:	
		diff = 4 - len(chars)
		chars[:0] = " " * diff

	#show char	
	def show_digit(digit):

		for pin, level in zip(display_pins, values[digit]):
			G.output(pin, not level)
				
		if polarity == "catode":
			for pin, level in zip(display_pins, values[digit]):
					G.output(pin, level)			

	#multiplexing part
	try:

		current_time_of_the_time_when_the_loop_was_created = int(time() * 1000)

		while True:
		
			if (current_time_of_the_time_when_the_loop_was_created + 1) < int(time() * 1000):
				break
			else:
				print current_time_of_the_time_when_the_loop_was_created	

			G11 = [True, False, False, False]
			G9  = [False, True, False, False]
			G23 = [False, False, False, True]
			G24 = [False, False, True, False]
			
			for i in range(4):
				G.output(11, G11[i])
				G.output(23,  G23[i])
				G.output(9, G9[i])
				G.output(24, G24[i])
	
				show_digit(chars[i])
				sleep(1/refresh_rate)

	except KeyboardInterrupt:
		print("Konec!")
		G.cleanup()		


for i in range(1000):
	show_four_chars(i)
