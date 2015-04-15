from __future__ import division
import RPi.GPIO as G
from time import sleep

G.setmode(G.BCM)

parallel_load = 11
clock = 9
serial_out = 10