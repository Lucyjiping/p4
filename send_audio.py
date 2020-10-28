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

    if len(sys.argv)<2:
        print 'pass one arguments:  <packet number> "'
        exit(1)

    addr = socket.gethostbyname("10.0.2.2")
    iface = get_if()

    print "sending on interface %s to %s" % (iface, str(addr))
    pkt_t =  Ether(src=get_if_hwaddr(iface), dst='ff:ff:ff:ff:ff:ff')
    pkt_t = pkt_t /IP(dst=addr) / TCP(dport=1234, sport=random.randint(49152,65535)) 
    pkt_s = pkt_t /"hello"
    pkt_l = pkt_t /"Really big world!"
    pkt_f = pkt_t /"a"
    pkt_f.show2()
    sendp(pkt_f, iface=iface)
    try:
	for i in range(int(sys.argv[1])):	
		# pkt_l.show2()
		sendp(pkt_s, iface=iface)
		sleep(0.2)
    except KeyboardInterrupt:
        raise


if __name__ == '__main__':
    main()





