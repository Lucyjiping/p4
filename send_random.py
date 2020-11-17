#!/usr/bin/env python
import argparse
import sys
import socket
import random
import struct

from scapy.all import sendp, send, get_if_list, get_if_hwaddr
from scapy.all import Packet
from scapy.all import Ether, IP, UDP, TCP

from time import sleep

def get_if():
    ifs=get_if_list()
    iface=None # "h1-eth0"
    for i in get_if_list():
        if "eth0" in i:
            iface=i
            break;
    if not iface:
        print "Cannot find eth0 interface"
        exit(1)
    return iface

def main():

    if len(sys.argv)<3:
        print 'pass two arguments: <destination> and <packet number> "'
        exit(1)

    addr = socket.gethostbyname(sys.argv[1])
    iface = get_if()

    print "sending on interface %s to %s" % (iface, str(addr))
    pkt_t =  Ether(src=get_if_hwaddr(iface), dst='ff:ff:ff:ff:ff:ff')
    pkt_t = pkt_t /IP(dst=addr) / TCP(dport=1234, sport=random.randint(49152,65535)) 
    pkt_s = pkt_t /"greet"
    pkt_l = pkt_t /"Really big world!"
    pkt_r = pkt_t /"a random packet"
    try:
	for i in range(int(sys.argv[2])):	
		num = random.randint(1,15)
		if num == 2 :
			pkt_s.show2()
			sendp(pkt_s, iface=iface)
		else:
			pkt_r.show2()
			sendp(pkt_r, iface=iface)
		sleep(random.random())
    except KeyboardInterrupt:
        raise


if __name__ == '__main__':
    main()




