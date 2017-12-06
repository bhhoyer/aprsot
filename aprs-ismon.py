'''
Title: stumon.py
Author: Bryan Hoyer
stumon listens to an aprs-is feed for packets from Bob's Stuart Island Cabin and
sends email if something's wrong
see stuart.py
'''
import aprslib
call = 'k7udr'
call = call.upper()

def callback(packet):
	if packet['from'] == call:
		print packet

AIS = aprslib.IS("K7NHE")
AIS.connect()
# by default `raw` is False, then each line is ran through aprslib.parse() AIS.consumer(callback, raw=True)
AIS.consumer(callback, raw=False)
