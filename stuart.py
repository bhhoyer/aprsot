
'''
Title: stuart.py
Built for Bob Brunkow's Stusrt Island Cabin using a UDRC-II and external 2m radio.
A generator on a timer runs for 2 hours twice a week to charge batteries and pump water.
A 5V wall wart plugs into an AC outlet to determine if the generator is on.
The output connects to the SQL input on the HD-15.
APRS Messages are sent on 144.39 and picked up by Igates.
A seperate pi at Bob's and connected APRS-IS monitors the reports and emails alarms
see stumon.py
'''
import RPi.GPIO as GPIO
import subprocess


GPIO.setmode(GPIO.BCM)
#Wall Wart drives HDR16-4 with Pullup removed thru Q1 IO25 is low true
GPIO.setup(25, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def genon(channel):
	print “Generator is ON”


def genoff(channel):
	print “Generator is OFF”

GPIO.add_event_detect(25, GPIO.RISING, callback=genoff, bouncetime=300)
GPIO.add_event_detect(25, GPIO.FALLING, callback=genon, bouncetime=300)
