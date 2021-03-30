# TODO: Create the UDP Heartbeat server program according the project specifications.
# Note: When submitting this file, replace the 'xx' with your first and last initials
# TODO: Create the UDP Heartbeat server program according the project specifications.
# Note: When submitting this file, replace the 'xx' with your first and last initials
import random
from socket import *
import datetime as dt
import argparse

# Multiple clients may access the server
# So maintain a dictionary (table) with IP address of the client as key
# and a list with fields as
# 1: the number of packets received as value
# 2: The lost packet count
# 3: Timestamp of last received heartbeat
iptable = dict()
# This is another dictionary that holds the number of packets lost between two successive replies
# for a particular address
packets_lost = dict()
while True:

    try:
# If no client pings the server for a whole minute, we have to assume that all clients are closed
        serverSocket.settimeout(60)
# Generate random number in the range of 0 to 100
        rand = random.randint(0, 100)

# Receive the client packet along with the address it is coming from
        message, address = serverSocket.recvfrom(1024)
# The client is sending us a message with sequence number and a timestamp separated by a whitespace tab character
# We need to split it by the whitespace tab character to extract the timestamp
        message_list = message.split('\t')
        message = dt.datetime.strptime(message_list[1],"%Y-%m-%d %H:%M:%S.%f")
  
    try:
  
# If the client is pinging the server for the first time, create a key for its address
        if not address in iptable:
            iptable[address] = [0,0,0]
# iptable[address][0] --> No of packets received
# iptable[address][1] --> Lost packet count
# iptable[address][2] --> Timestamp of last heartbeat
    packets_lost[address] = 0

# A new packet has been received, so the value has to be incremented
    iptable[address][0] += 1

# Human readable console response
    print 'Received packet no',iptable[address][0],'from',address,'.',
    print 'The sequence number sent with the packet was',message_list[0]
now = dt.datetime.now()
  
# Delay between the time at which the client sent the packet and the time server received it
response = now - message

# Timestamp of most recent ping from the client
iptable[address][2] = now

# If rand is less is than the arguement packetloss, we consider the packet lost and do not respond
if rand < args.packetloss:
print 'Simulating packet loss for',address[0], ':', address[1]
# Increment the value of total packets lost for the address
iptable[address][1]+=1
# Increment the value of packets lost in between two successful replies
# Needed to report to the client
packets_lost[address] += 1
continue

  
# Otherwise, the server responds by replying with the time difference and a report of lost packets
reply = "Packet delivery delay = "+str(response)+", Number of packets lost in between = "+ packets_lost[address]
# Reset packets_lost's value. We are restarting the counter for that address
packets_lost[address] = 0

serverSocket.sendto(reply, address)
print 'Sent response to',address,'with a delay of',response.total_seconds()

# The client may send a packet with invalid data either mistakenly or with a mischievious attempt at breaking the server.
# This except block replies with a response and makes sure that server doesn't break down
except TypeError:
print 'Client at',address,'sent an unrecognized packet. Replying with an appropriate response'
response = 'The datatype supported by this server is string. Given data is'+str(type(message))
serverSocket.sendto(response,address)

# The server can be closed with a keyboard interrupt. But before exiting, the socket must be safely closed for security reasons
# Optional feature addition is to print a report of all the clients who pinged and some additional information
except KeyboardInterrupt:
print '\nSafely closing down the server...'
# It should exit with a status summary of no of packets received from each client in a tabular format
def decor():
"""Decoration for Status Summary"""
for i in range(0,70):
print '-',
print

decor()
print "Summary"
decor()
server_end = dt.datetime.now()
print "Server started serving on port",args.port,"on",server_start,"and is exiting on",server_end
print "Server ran for a duration of",( server_end - server_start )
print "NOTE: The packetloss percentage is only for studying the simulation.",
print "Real life UDP server wouldn't know and wouldn't care about packetloss"
decor()
print "Client\t\t\tNumber of Packets Received\tPacket loss percentage\tLast Heartbeat received at"
decor()

for key in iptable:
percentage = ((int(iptable[key][1])) / (int(iptable[key][0]) * 1.0) * 100)
print key,"\t",iptable[key][0],"\t\t\t\t",("%.2f" %percentage) ,"%\t\t\t", iptable[key][2]

print ''
decor()
break;

except Exception as e:
  
if type(e) == timeout:
print "NOTE: It's been a whole minute since the last client pinged the server.",
print "If there are no more clients to test the server with, you can close the server with Ctrl+C key stroke"

else:
print e

# Safely close the socket
serverSocket.close()
