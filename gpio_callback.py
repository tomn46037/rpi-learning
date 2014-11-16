#!/usr/bin/python

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

GPIO.output(17, True);
GPIO.output(22, True);

GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def event(channel):
	print "Button %d called" % channel ;

	if ( channel == 23 ):
		GPIO.output(17, not GPIO.input(17))

	if ( channel == 24 ):
		GPIO.output(22, not GPIO.input(22))

GPIO.add_event_detect(24, GPIO.FALLING)
GPIO.add_event_callback(24, event)

GPIO.add_event_detect(23, GPIO.FALLING)
GPIO.add_event_callback(23, event)

while True:
	c = 1 + 1

GPIO.cleanup()


