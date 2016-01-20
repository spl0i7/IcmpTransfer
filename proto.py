#!/usr/bin/env python
'''
Here we design protocol to be more reliable
'''
from packetgen import PacketGen
import socket
import os
class Proto:
    def __init__(self):
        self.pg=PacketGen()
        self.s=socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_RAW)
    def max_mtu(self,saddr,daddr):
        self.pg.set_saddr(saddr)
        self.pg.set_daddr(daddr)
        ip_header=self.pg.construct_ip_h()
        mtu_size=64
        while mtu_size <= 1500:
            icmp_packet=self.pg.construct_icmp_p("a"*mtu_size)
            packet=ip_header+icmp_packet
            self.s.sendto(packet,(daddr,0))
            mtu_size+=64
        return mtu_size

