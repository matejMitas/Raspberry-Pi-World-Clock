# -*- coding: utf-8 -*-

from __future__ import division
import RPi.GPIO as G
from time import sleep

G.setmode(G.BCM)
G.setwarnings(False)

from shift_register import Sipo_reg

reg = Sipo_reg([2,3,4], 2)

#Match values with numbers
values = {
		"0" : [1,1,1,1,1,1,0],
		"1" : [0,0,0,0,1,1,0],
		"2" : [1,1,0,1,1,0,1],
		"3" : [1,1,1,1,0,0,1],
		"4" : [0,1,1,0,0,1,1],
		"5" : [1,0,1,1,0,1,1],
		"6" : [1,0,1,1,1,1,1],
		"7" : [1,1,1,0,0,0,0],
		"8" : [1,1,1,1,1,1,1],
		"9" : [1,1,1,1,0,1,1],
		"-" : [0,0,0,0,0,0,1],
		" " : [0,0,0,0,0,0,0]
}


def show(number, pins):
    num = values[number]
    number = []
    dot = [0]

    for digit in num:
        number.append(not digit)

    reg.shift_out(number + dot + pins)
    sleep(0.5)


try:
    while True:
        show("1", [1,0,0,0])
        show("2", [0,1,0,0])
        show("3", [0,0,1,0])
        show("4", [0,0,0,1])
except KeyboardInterrupt:
    print("Konec")

reg.clear()
