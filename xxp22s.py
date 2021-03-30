# TODO: Create the UDP Heartbeat server program according the project specifications.
# Note: When submitting this file, replace the 'xx' with your first and last initials
from socket import *
import datetime as dt
import time

# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('127.0.0.1', 45678))
serverSocket.settimeout(10)
# Record the time at which the server started
server_start = dt.datetime.now()

print('UDP Ping-Server is listening.')
while True:
    try:
        start_time = time.time()
        # Receive the client packet along with the address it is coming from
        message, address = serverSocket.recvfrom(1024)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print('Server received {}. Pulse interval was {}'.format(message.decode(), elapsed_time))
    except timeout:
        print('No pulse after 10 seconds. Server quits.')
        break
