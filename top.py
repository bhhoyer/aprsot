#top.py

import socket
import time
from Beacon import *

# Mainline of the program:

#server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Fill in the name and port number of the server with the KISS TNC.
host = socket.gethostbyname('127.0.0.1')
port = 8001
MYCALL = "k7udr"
email = 'bhhoyer@icloud.com'
msg = '{GEN:ON}'


APRS = ':EMAIL    :'+email+' '+msg


#server.connect((host,port))

frame = buildUIFrame("Python",MYCALL,APRS)
frame = KissWrap(frame)
print "the kiss frame is:",len(frame)
#dumpstring(frame)

#and send it
#server.send(frame)
#server.close()

for i in range (1,4):
	print APRS+' seq',i
	time.sleep(3)
