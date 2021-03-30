# TODO: Create the UDP Heartbeat client program according the project specifications.
# Note: When submitting this file, replace the 'xx' with your first and last initials
import sys
from datetime import datetime
import time
from socket import *

# Create the UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Server information
serverName = '127.0.0.1'
serverPort = 45678
serverAddressPort = (serverName, serverPort)

i = 1
while True:
    currentTime = datetime.now().ctime()
    msg = 'heartbeat pulse {}'.format(i)
    print(msg)
    clientSocket.sendto(msg.encode(), serverAddressPort)
    i += 1
    time.sleep(5)

print('Exiting program with status 0.')
sys.exit(0)
