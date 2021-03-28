# Note: When submitting this file, replace the 'xx' with your first and last initials
import sys
import time
from socket import *
from datetime import date

# Create the UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1.0)  # Timeout if no response after 1 second

# Server information
serverName = '127.0.0.1'
serverPort = 45678
serverAddressPort = (serverName, serverPort)

# Send 10 ping messages to the server
for i in range(1, 10):
    try:
        msg = 'seq {} {}'.format(str(i), date.today().ctime())
        tic = time.time()  # Time when message was sent
        clientSocket.sendto(msg.encode(), serverAddressPort)

        response = clientSocket.recv(1024)
        toc = time.time()  # Time when response was received
        RTT = str(toc - tic)  # Round-trip time
        print('Ping {} : host {} replied: {}, RTT = {} ms'.format(str(i), serverName, response.decode(), RTT))

    except socket.timeout:
        print('Ping' + str(i) + ': timed out, message was lost.')

print('Closing socket.')
clientSocket.close()
print('Exiting program.')
sys.exit(0)
