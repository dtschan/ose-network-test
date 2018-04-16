#!/usr/bin/env python

import socket
import sys
import time
import threading

def ping():
    server_address = ('ose-network-test', 10000)

    seq = 0
    while True:
        sock.sendto("%r %r" % (seq, time.time()), server_address)
        seq += 1
        time.sleep(1)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#sock.settimeout(10)

try:
    ping_thread = threading.Thread(target=ping)
    ping_thread.setDaemon(True)
    ping_thread.start()

    last_seq = -1
    last_hour = -1
    lost_pkgs = 0
    while True:
        data, server = sock.recvfrom(4096)
        server_seq, start_time, server_time = data.split(' ')
        stop_time = time.time()
        seq = int(server_seq)
        start_time = float(start_time)
        server_time = float(server_time)

        hour = time.localtime(start_time).tm_hour
        if last_hour != -1 and hour != last_hour:
            print '%s Lost %d packages in the last hour' % (time.ctime(stop_time), lost_pkgs)
            lost_pks = 0
        last_hour = hour

        if seq > last_seq + 1:
          print '%s lost %d packages or packages out of order' % (time.ctime(stop_time), seq - last_seq - 1)
          lost_pkgs += seq - last_seq - 1
        print '%s %d %.2f %.2f' % (time.ctime(stop_time), seq, (server_time - start_time) * 1000.0, (stop_time - start_time) * 1000.0)
        last_seq = seq

finally:
    sock.close()
