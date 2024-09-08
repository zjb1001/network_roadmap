from scapy.all import *

def analyze_tcp_udp_packet(packet):
    if TCP in packet:
        tcp = packet[TCP]
        print("TCP Packet Analysis:")
        print(f"Source Port: {tcp.sport}")
        print(f"Destination Port: {tcp.dport}")
        print(f"Sequence Number: {tcp.seq}")
        print(f"Acknowledgment Number: {tcp.ack}")
        print(f"Flags: {tcp.flags}")
        print(f"Window Size: {tcp.window}")
        print(f"Checksum: {tcp.chksum}")
    elif UDP in packet:
        udp = packet[UDP]
        print("UDP Packet Analysis:")
        print(f"Source Port: {udp.sport}")
        print(f"Destination Port: {udp.dport}")
        print(f"Length: {udp.len}")
        print(f"Checksum: {udp.chksum}")
    print()

def main():
    print("Sniffing TCP and UDP packets. Press Ctrl+C to stop.")
    sniff(filter="tcp or udp", prn=analyze_tcp_udp_packet, count=10)
    print("Sniffing complete.")

if __name__ == "__main__":
    main()