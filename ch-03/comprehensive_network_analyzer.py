from scapy.all import *
from scapy.layers import http

def analyze_packet(packet):
    print("\n" + "=" * 50)
    
    # Ethernet
    if Ether in packet:
        ether = packet[Ether]
        print(f"Ethernet Frame:")
        print(f"Source MAC: {ether.src}")
        print(f"Destination MAC: {ether.dst}")
        print(f"Type: {ether.type}")
    
    # ARP
    if ARP in packet:
        arp = packet[ARP]
        print(f"ARP Packet:")
        print(f"Operation: {'Request' if arp.op == 1 else 'Reply'}")
        print(f"Sender MAC: {arp.hwsrc}")
        print(f"Sender IP: {arp.psrc}")
        print(f"Target MAC: {arp.hwdst}")
        print(f"Target IP: {arp.pdst}")
    
    # IP
    if IP in packet:
        ip = packet[IP]
        print(f"IP Packet:")
        print(f"Version: {ip.version}")
        print(f"Source IP: {ip.src}")
        print(f"Destination IP: {ip.dst}")
        print(f"Protocol: {ip.proto}")
    
    # IPv6
    if IPv6 in packet:
        ipv6 = packet[IPv6]
        print(f"IPv6 Packet:")
        print(f"Version: {ipv6.version}")
        print(f"Source IP: {ipv6.src}")
        print(f"Destination IP: {ipv6.dst}")
        print(f"Next Header: {ipv6.nh}")
    
    # TCP
    if TCP in packet:
        tcp = packet[TCP]
        print(f"TCP Segment:")
        print(f"Source Port: {tcp.sport}")
        print(f"Destination Port: {tcp.dport}")
        print(f"Flags: {tcp.flags}")
    
    # UDP
    if UDP in packet:
        udp = packet[UDP]
        print(f"UDP Datagram:")
        print(f"Source Port: {udp.sport}")
        print(f"Destination Port: {udp.dport}")
    
    # ICMP
    if ICMP in packet:
        icmp = packet[ICMP]
        print(f"ICMP Packet:")
        print(f"Type: {icmp.type}")
        print(f"Code: {icmp.code}")
    
    # Application Layer
    if TCP in packet:
        if packet[TCP].dport == 80 or packet[TCP].sport == 80:
            print("HTTP Packet")
        elif packet[TCP].dport == 443 or packet[TCP].sport == 443:
            print("HTTPS Packet")
        elif packet[TCP].dport == 21 or packet[TCP].sport == 21:
            print("FTP Control Packet")
        elif packet[TCP].dport == 20 or packet[TCP].sport == 20:
            print("FTP Data Packet")
        elif packet[TCP].dport == 22 or packet[TCP].sport == 22:
            print("SSH Packet")

def main():
    print("Starting comprehensive network analysis. Press Ctrl+C to stop.")
    sniff(prn=analyze_packet, store=0)

if __name__ == "__main__":
    main()