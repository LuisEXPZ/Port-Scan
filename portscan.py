#!/usr/bin/python
import socket
import sys

ip = sys.argv[1]

for porta in range(1,65535):
        meusocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c = meusocket.connect_ex((ip,porta))
        if c == 0:
                print "Porta",porta,"[ABERTA]"
                meusocket.close()

