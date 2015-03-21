# -*- coding: utf-8 -*-

from __future__ import division
import RPi.GPIO as G
from time import sleep

G.setmode(G.BCM)
G.setwarnings(False)

from shift_register import Sipo_reg


reg = Sipo_reg([2,3,4], 1)
reg.shift_out([0,1,0,1,0,1,0,1,1])
sleep(2)
reg.clear()