import socket
import struct
import sys

def analyze_ip_packet(packet):
    # Analyze IPv4 header
    ip_header = struct.unpack('!BBHHHBBH4s4s', packet[:20])
    version_ihl = ip_header[0]
    version = version_ihl >> 4
    ihl = version_ihl & 0xF
    tos = ip_header[1]
    total_length = ip_header[2]
    identification = ip_header[3]
    flags_fragment_offset = ip_header[4]
    ttl = ip_header[5]
    protocol = ip_header[6]
    header_checksum = ip_header[7]
    source_address = socket.inet_ntoa(ip_header[8])
    destination_address = socket.inet_ntoa(ip_header[9])

    print(f"IPv{version} Packet Analysis:")
    print(f"Version: {version}")
    print(f"IHL: {ihl}")
    print(f"ToS: {tos}")
    print(f"Total Length: {total_length}")
    print(f"Identification: {identification}")
    print(f"Flags & Fragment Offset: {flags_fragment_offset}")
    print(f"TTL: {ttl}")
    print(f"Protocol: {protocol}")
    print(f"Header Checksum: {header_checksum}")
    print(f"Source Address: {source_address}")
    print(f"Destination Address: {destination_address}")

def create_raw_socket(protocol):
    if sys.platform.startswith('win'):
        socket_protocol = socket.IPPROTO_IP
    else:
        socket_protocol = socket.IPPROTO_ICMP
    
    sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
    sniffer.bind(('0.0.0.0', 0))
    sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    
    if sys.platform.startswith('win'):
        sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    
    return sniffer

def main():
    sniffer = create_raw_socket(socket.IPPROTO_ICMP)
    
    try:
        print("Sniffing IP packets. Press Ctrl+C to stop.")
        while True:
            packet = sniffer.recvfrom(65565)[0]
            analyze_ip_packet(packet)
            print("\n")
    except KeyboardInterrupt:
        print("Sniffing stopped.")
    finally:
        if sys.platform.startswith('win'):
            sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

if __name__ == "__main__":
    main()