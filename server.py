#!/usr/bin/env python

import socket
def icmpListen():
        s=socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_ICMP)
        s.setsockopt(socket.SOL_IP,socket.IP_HDRINCL,1)
        file =open("file.bin",'ab')
        while True:
                addr=s.recvfrom(1500)
                print ("Sender "+str(addr[1][0]))
                print ("DATA : "+str(addr[0][28:])) #strip off headers
                print ("Data Length:"+str(len(str(addr[0][28:]))))
                print (len(str(addr[0])))
                file.write(addr[0][28:])
icmpListen()
