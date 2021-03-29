# Note: When submitting this file, replace the 'xx' with your first and last initials
import sys
from datetime import datetime
import time
from socket import *

# Variables
packetLoss = 0
maxRTT = 0
minRTT = 1000
summedRTT = 0
iterationCount = 1

# Create the UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)  # Timeout if no response after 1 second

# Server information
serverName = '127.0.0.1'
serverPort = 45678
serverAddressPort = (serverName, serverPort)

# Send 10 packets to the server.
for i in range(1, 11):
    start = time.time()  # When message was sent to the server.
    currentTime = datetime.now().ctime()
    msg = 'seq {} {}'.format(i, currentTime)
    clientSocket.sendto(msg.encode(), serverAddressPort)

    try:
        response, address = clientSocket.recvfrom(1024)
        RTT = (time.time() - start) * 1000  # Round-Trip Time in milliseconds

        # Determine RTT statistics
        summedRTT += RTT
        if RTT > maxRTT:
            maxRTT = RTT
        if RTT < minRTT:
            minRTT = RTT

        print('Ping {}: {} replied: {}, RTT = {} ms'.format(i, serverName, response.decode(), RTT))

    except timeout:
        print('Ping {}: timed out, message was lost.'.format(i))
        packetLoss += 1

# Display RTT statistics.
print('Min RTT = {} ms'.format(minRTT))
print('Max RTT = {} ms'.format(maxRTT))
avgRTT = summedRTT / (10 - packetLoss)
print('Avg RTT = {} ms'.format(avgRTT))
packetLossRt = packetLoss * 10
print('Packets lost = {}%'.format(packetLossRt))
print('Exiting program with status 0.')
sys.exit(0)
