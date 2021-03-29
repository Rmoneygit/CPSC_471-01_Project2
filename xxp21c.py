# Note: When submitting this file, replace the 'xx' with your first and last initials
import sys
import datetime
import time
from socket import *
from datetime import date

# Variables
packetLoss = 0
maxRTT = 0
minRTT = 1000
sum = 0
iterationCount = 1

# Create the UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)  # Timeout if no response after 1 second

# Server information
serverName = '127.0.0.1'
serverPort = 45678
serverAddressPort = (serverName, serverPort)

while iterationCount <= 10:
    start = time.time()
    clientSocket.sendto(b'message',  (serverAddressPort))
    currentTime = datetime.date.fromtimestamp(time.time())

    try:
        [message, address] = clientSocket.recvfrom(1024)
        RTT = (time.time() - start)
        sum += RTT
        if RTT > maxRTT:
            maxRTT = RTT
        if RTT < minRTT:
            minRTT = RTT
        print('Ping ' + str(iterationCount) + ': host ' + serverName + ' replied: seq ' + str(iterationCount) + ' ' + str(currentTime.ctime()) + ' , RTT = ' + str(RTT) + ' ms')

    except timeout:
        print('Ping ' + str(iterationCount) + ': timed out, message was lost')
        packetLoss += 1

    iterationCount += 1

    if iterationCount > 10:
        clientSocket.close()

if __name__ == '__main__':
    print('Min RTT = ' + str(minRTT) + ' ms')
    print('Max RTT = ' + str(maxRTT) + ' ms')
    avgRTT = sum /( 10 - packetLoss )
    print('Avg RTT = ' + str(avgRTT) + ' ms')
    packetLossRt = packetLoss * 10
    print('Packet lost = ' + str(packetLossRt) + ' %')

sys.exit(0)
