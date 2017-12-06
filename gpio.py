'''
gpio.py
bhhoyer
'''
import RPi.GPIO as GPIO
import socket
import time
import aprslib
from Beacon import *

def send_is(msg):
	AIS.connect()
#	AIS.sendall('K7UDR>APRS,TCPIP*:'+':EMAIL    :'+email+' '+msg)
	AIS.sendall('K7UDR>APRS,TCPIP*:'+':K7UDR    :'+msg)

#APRS-IS Setup
AIS = aprslib.IS("K7UDR", passwd="16273", port=14580)

#KISS Network Setup
host = socket.gethostbyname('127.0.0.1')
port = 8001

#Source Setup
MYCALL = "k7udr"
email = 'bhhoyer@icloud.com'

#GPIO Setuo
GPIO.setmode(GPIO.BCM)
ACn = 25 #SQL buffered by transistor
GPIO.setup(ACn, GPIO.IN, GPIO.PUD_UP)

#Main

state = GPIO.input(ACn)
print 'Initial State',state
start = time.time()

while True:
	new = GPIO.input(ACn)
	if new != state:
		state = new
		if state == 0:
			start = time.time()
			msg = 'GEN ON'
			send_is(msg)		
		elif state == 1:
			end = time.time()
			msg = 'GEN OFF'
			send_is(msg)			
			print 'Generator ran for:',int(end-start)
		else:
			print 'Assert ERROR'
	time.sleep(1)
