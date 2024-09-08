from scapy.all import *

def analyze_icmp_packet(packet):
    if ICMP in packet:
        icmp = packet[ICMP]
        print("ICMP Packet Analysis:")
        print(f"Type: {icmp.type}")
        print(f"Code: {icmp.code}")
        print(f"Checksum: {icmp.chksum}")
        if icmp.type == 8:  # Echo Request
            print("Echo Request (Ping)")
        elif icmp.type == 0:  # Echo Reply
            print("Echo Reply (Ping Response)")
        elif icmp.type == 3:  # Destination Unreachable
            print("Destination Unreachable")
        elif icmp.type == 11:  # Time Exceeded
            print("Time Exceeded (TTL expired)")
    print()

def main():
    print("Sniffing ICMP packets. Press Ctrl+C to stop.")
    sniff(filter="icmp", prn=analyze_icmp_packet, count=10)
    print("Sniffing complete.")

if __name__ == "__main__":
    main()
from scapy.all import *
from scapy.layers import http

def analyze_application_layer_packet(packet):
    if TCP in packet:
        if packet[TCP].dport == 80 or packet[TCP].sport == 80:
            if Raw in packet:
                print("HTTP Packet:")
                print(packet[Raw].load.decode('utf-8', 'ignore'))
        elif packet[TCP].dport == 443 or packet[TCP].sport == 443:
            print("HTTPS Packet (Encrypted)")
        elif packet[TCP].dport == 21 or packet[TCP].sport == 21:
            print("FTP Control Packet:")
            if Raw in packet:
                print(packet[Raw].load.decode('utf-8', 'ignore'))
        elif packet[TCP].dport == 20 or packet[TCP].sport == 20:
            print("FTP Data Packet")
        elif packet[TCP].dport == 22 or packet[TCP].sport == 22:
            print("SSH Packet")
    print()

def main():
    print("Analyzing application layer packets. Press Ctrl+C to stop.")
    sniff(filter="tcp port 80 or tcp port 443 or tcp port 21 or tcp port 20 or tcp port 22", 
          prn=analyze_application_layer_packet, 
          count=20)
    print("Analysis complete.")

if __name__ == "__main__":
    main()