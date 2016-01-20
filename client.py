#!/usr/bin/env python
import os
import sys
from proto import Proto
from filehandler import FileHandler
import time

def display_man():
    print("[+] IcmpFT - ICMP File Transfer")
    print("[+] by spl0i7 https://www.ketansingh.me")
    print("[+] Usage "+sys.argv[0]+" <file> <source ip> <destination ip>")

proto=Proto()
fh=FileHandler()
start_time=time.time()
max_mtu=1436 #our default MTU
if(len(sys.argv) == 4):
    file=sys.argv[1]
    saddr=sys.argv[2]
    daddr=sys.argv[3]
    print("Size : "+str(os.path.getsize(file))+" bytes")
    pointer=max_mtu
    fh.send_file(file, 1436, saddr, daddr)
    time=time.time()-start_time
    print("Time : "+str(time))
    speed=os.path.getsize(file)/float(time)
    print("Speed : "+str(speed/(1024*1024))+" MB/s")
else :
    display_man()


