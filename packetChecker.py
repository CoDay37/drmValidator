import os
import pcap as p
import dpkt, pcap
from scapy.all import *

sniffer = pcap.pcap(name=None, promisc=True, immediate=True)
for timestamp, raw_buf in sniffer:
    output = {}


    print("YOLO = XD")
    var= 11
    var +=1

    #unpacking ethernet frame
    eth = dpkt.ethernet.Ethernet(raw_buf)
    output['eth'] = {'src': eth.src, 'dst': eth.dst,'type': eth.type}
    #Is this an ip packet?
    if not isinstance(eth.data, dpkt.ip.IP):
        print ('Non IP packet type not supported %s\n' % eth.data.__class__.__name__)
        continue
    #Grab ip packet
    packet = eth.data

    #pull out information
    df = bool(packet.off & dpkt.ip.IP_DF)
    mf = bool(packet.off & dpkt.ip.IP_MF)
    offset = packet.off & dpkt.ip.IP_OFFMASK

    #pulling out src, dst, length, fragment info, TTL, checksum and protocol
    output['ip'] = {'src':packet.src, 'dst':packet.dst, 'p': packet.p, 'len':packet.len, 'ttl':packet.ttl, 'df':df, 'mf':mf, 'offset': offset, 'checksum':packet.sum}






#pip install pypcap