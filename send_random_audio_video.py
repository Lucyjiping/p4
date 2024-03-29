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
        print 'pass two arguments:  and <packet number> "'
        exit(1)

    addr = socket.gethostbyname("10.0.3.3")
    iface = get_if()

    print "sending on interface %s to %s" % (iface, str(addr))
    pkt_t =  Ether(src=get_if_hwaddr(iface), dst='ff:ff:ff:ff:ff:ff')
    pkt_t = pkt_t /IP(dst=addr) / TCP(dport=1234, sport=random.randint(49152,65535)) 
    pkt_s = pkt_t /"greet"
    pkt_l = pkt_t /"Merry Christmas!!"
    try:
	for i in range(int(sys.argv[1])):	
		pkt_s.show2()
		sendp(pkt_s, iface=iface)
		sleep(random.random())

		pkt_l.show2()
		sendp(pkt_l, iface=iface)
		sleep(random.random())
    except KeyboardInterrupt:
        raise


if __name__ == '__main__':
    main()




