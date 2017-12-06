'''
Title: stumon.py
Author: Bryan Hoyer
stumon listens to an aprs-is feed for packets from Bob's Stuart Island Cabin and
sends email if something's wrong
see stuart.py
'''
import aprslib

# a valid passcode for the callsign is required in order to send
AIS = aprslib.IS("K7UDR", passwd="16273", port=14580)
AIS.connect()
# send a single status message
AIS.sendall("KE7TLE>APRS,TCPIP*::EMAIL    :bhhoyer@icloud.com From APRSLIB to you via Python")
#AIS.sendall("K7NHE>APRS,TCPIP*:=4840.5N/12310.16WyTesting")
