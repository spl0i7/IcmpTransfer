#!/usr/bin/env python
'''
This class is responsible for packet generation using raw sockets
'''
import socket
import struct
class PacketGen:
    def __init__(self):
        #IP Header Initialization
        self.ip_ihl=5
        self.ip_ver=4
        self.ip_tos=0
        self.ip_id=1337
        self.ip_frag_off=0
        self.ip_tot_len=0
        self.ip_ttl=255
        self.ip_proto=1
        self.ip_csum=0
        self.ip_ihl_ver=(self.ip_ver<<4)+self.ip_ihl
        self.ip_saddr=0
        self.ip_daddr=0
        #ICMP Header Initialization
        self.icmp_type=8
        self.icmp_code=0
        self.icmp_identifier=1337
        self.icmp_sequence=0
        self.icmp_csum=0
        self.imcp_data=None
    def set_saddr(self, saddr):
        self.ip_saddr=socket.inet_aton(saddr)
    def set_daddr(self, daddr):
        self.ip_daddr=socket.inet_aton(daddr)
    def ip_checksum(self,csum):
        self.ip_csum=csum
    def icmp_csum(self,icmp_csum):
        self.icmp_csum=icmp_csum
    def construct_ip_h(self):
        ip_header=struct.pack('!BBHHHBBH4s4s', self.ip_ihl_ver, self.ip_tos, self.ip_tot_len, self.ip_id, self.ip_frag_off, self.ip_ttl, self.ip_proto, self.ip_csum, self.ip_saddr, self.ip_daddr)
        return ip_header
    def construct_icmp_p(self,data):
        self.icmp_data=data
        icmp_data_length=len(data)
        icmp_packet=struct.pack('!BBHHH'+str(icmp_data_length)+'s',self.icmp_type,self.icmp_code,self.icmp_csum,self.icmp_identifier,self.icmp_sequence,self.icmp_data)
        icmp_packet=struct.pack('!BBHHH'+str(icmp_data_length)+'s',self.icmp_type,self.icmp_code,self.checksum(icmp_packet),self.icmp_identifier,self.icmp_sequence,self.icmp_data)
        return icmp_packet
    #I don't understand how checksum works
    def checksum(self,packet):
        sum=0
        count=0
        countTo=(len(packet)/2)*2
        while count<countTo:
                tmp=ord(packet[count+1])*256 + ord(packet[count])
                sum+=tmp
                count+=2
        if countTo<len(packet):
                sum+=ord(packet[len(packet) -1])
        sum = (sum >> 16)  +  (sum & 0xffff)
        sum = sum + (sum >> 16)
        answer = ~sum
        answer = answer & 0xffff
        answer = answer >> 8 | (answer << 8 & 0xff00)
        return answer
