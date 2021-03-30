# TODO: Create the UDP Heartbeat client program according the project specifications.
# Note: When submitting this file, replace the 'xx' with your first and last initials
import random
from socket import *
import datetime as dt
import argparse

# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Initializing parser for accepting command line arguements
parser = argparse.ArgumentParser(
description="""UDP Heartbeat Server. Simulates packet loss and supports user defined value for the port number. \
To close the server, press 'Ctrl + C'""",
usage="./Heartbeat.py [--port] N [--packetloss] N [-h/--help]")

# Assign port number to socket
parser.add_argument(
    '--port', default=12000, type=int, metavar='int',
    help='The port where the server should run (integer > 1024 and < 65535) Default: 12000')

# Assign packetloss percentage
parser.add_argument(
    '--packetloss', default=40, type=int, metavar='int',
    help='Percentage of data loss experienced by the server (Simulated) Default: 40%')

try:
    args = parser.parse_args()

except ValueError:
    print ("Usage: ./Heartbeat.py [--port] N [--packetloss] N [-h/--help]")
    exit()

    if args.port < 1024 or args.port > 65535:
        print ('Invalid port number. Value must be within the range 1024-65535')
        exit()

    if args.packetloss < 0 or args.packetloss > 100:
        print ('Invalid value for packet loss percentage. Value must be in between 0 to 100')
        exit()
    # Variable has to be initialized outside so as to be able to use everywhere in the program
    server_start = dt.datetime.now()

    if args.port == 12000:
    # I have taken a default value and it is my headache to make sure it works
        def portassign():
        #A function to make sure the server binds to a free port in case the user hasn't specified one on his own
            flag = True
            while flag:
                try:
                # Bind server to port
                    serverSocket.bind(('', args.port))
                # Record the time at which the server started
                    server_start = dt.datetime.now()
                    print ('Serving on host at port', args.port,'with a packet loss simulation of',args.packetloss,'%')
                    flag = False

                except IOError:
                    print ('Unsuccessful in binding server to port',args.port,'. Trying with another one..')
                    args.port += 1

                except OverflowError:
                    port = 1024

        portassign()


    else:
        try:
            # Bind server to port
            serverSocket.bind(('', args.port))
            # Record the time at which the server started
            server_start = dt.datetime.now()
            print ('Serving on host at port'+ args.port+'with a packet loss simulation of'+args.packetloss+'%')

        except IOError:
            # The user has specified the port number.
            # We should allow him to specify an alternative rather than take matters into our own hands
            print ('Cannot bind server to port'+args.port+'. Try with another one')
            exit()

