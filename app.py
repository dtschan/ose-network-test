#!/usr/bin/env python

import socket
import sys
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('0.0.0.0', 10000)
sock.bind(server_address)

while True:
    data, address = sock.recvfrom(4096)
    sock.sendto('%s %r' % (data, time.time()), address)
