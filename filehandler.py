#!/usr/bin/env python
'''
This class is responsible for fragmenting file and sending is over to server
'''
import os
import socket
import time
from packetgen import PacketGen
class FileHandler:
    def __init__(self):
        self.filesize=0
        self.chunksize=0
        self.pointer=0
        self.daddr=""
        self.saddr=""
        self.s=socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_RAW)
        self.pg=PacketGen()
    def send_file(self, file, chunk,saddr,daddr):
        self.filesize = os.path.getsize(file)
        self.chunksize = self.filesize / chunk
        self.pointer = chunk
        self.pg.set_saddr(saddr)
        self.pg.set_daddr(daddr)
        ip_header=self.pg.construct_ip_h()
        fr = open(file, 'rb')
        while True:
            fr.seek(self.pointer - chunk) #changing pointer to read parts of file
            buf = fr.read(chunk)
            if (buf == ''): #we reached eof , get out now.
                break
            icmp_packet=self.pg.construct_icmp_p(buf)
            packet=ip_header+icmp_packet
            self.s.sendto(packet,(daddr,0))
            self.pointer+=chunk
            time.sleep(.0005) #Limiting the time interval to avoid packet loss
        fr.close()


    def filesize(self,file):
        return os.path.getsize(file)
