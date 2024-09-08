import socket
import struct
import sys
from scapy.all import *

def analyze_ip_packet(packet):
    if IP in packet:
        ip = packet[IP]
        print(f"IP Packet Analysis:")
        print(f"Version: {ip.version}")
        print(f"IHL: {ip.ihl}")
        print(f"ToS: {ip.tos}")
        print(f"Total Length: {ip.len}")
        print(f"Identification: {ip.id}")
        print(f"Flags: {ip.flags}")
        print(f"Fragment Offset: {ip.frag}")
        print(f"TTL: {ip.ttl}")
        print(f"Protocol: {ip.proto}")
        print(f"Header Checksum: {ip.chksum}")
        print(f"Source Address: {ip.src}")
        print(f"Destination Address: {ip.dst}")
    elif IPv6 in packet:
        ipv6 = packet[IPv6]
        print(f"IPv6 Packet Analysis:")
        print(f"Version: {ipv6.version}")
        print(f"Traffic Class: {ipv6.tc}")
        print(f"Flow Label: {ipv6.fl}")
        print(f"Payload Length: {ipv6.plen}")
        print(f"Next Header: {ipv6.nh}")
        print(f"Hop Limit: {ipv6.hlim}")
        print(f"Source Address: {ipv6.src}")
        print(f"Destination Address: {ipv6.dst}")

def main():
    print("Sniffing IP packets. Press Ctrl+C to stop.")
    sniff(filter="ip or ip6", prn=analyze_ip_packet, count=10)
    print("Sniffing complete.")

if __name__ == "__main__":
    main()