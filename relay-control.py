#!/usr/bin/python

from RPi import GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

bl = [5,6]
fl = [12,13]
fr = [16,19]
br = [20,21]

forward = [5,12,21,19]
backwards = [6,13,20,16]
left = [6,13,21,19]
right = [5,12,20,16]

GPIO.setup(bl,GPIO.OUT,initial=0)
GPIO.setup(fl,GPIO.OUT,initial=0)
GPIO.setup(br,GPIO.OUT,initial=0)
GPIO.setup(fr,GPIO.OUT,initial=0)

def stop():
        GPIO.output(bl,0)
        GPIO.output(br,0)
        GPIO.output(fl,0)
        GPIO.output(fr,0)

def move(direction):
        stop()
        GPIO.output(direction,1)

try:
        while True:
                command = raw_input('move me (f,b,l,r,s): ')
                if command == 'f':
                        move(forward)
                elif command == 'b':
                        move(backwards)
                elif command == 'l':
                        move(left)
                elif command == 'r':
                        move(right)
                elif command == 's':
                        stop()
                else:
                        stop()
finally:
        GPIO.cleanup()
