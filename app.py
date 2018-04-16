#!/usr/bin/env python

import socket
import sys
import time

server_address = ('0.0.0.0', 10000)
#sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(server_address)
sock.listen(1)

while True:
    try:
        conn, addr = sock.accept()
        while True:
            data, address = conn.recvfrom(4096)
            conn.send('%s %r' % (data, time.time()))
    except Exception as e:
        print '%s %s' % (time.ctime(), e)

