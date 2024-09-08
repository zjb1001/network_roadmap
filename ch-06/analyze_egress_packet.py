import socket
import struct
import sys

def create_raw_socket():
    try:
        s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0003))
    except socket.error as msg:
        print(f'Socket could not be created. Error Code : {msg[0]} Message {msg[1]}')
        sys.exit()
    return s

def analyze_packet(packet):
    # Parse Ethernet header
    eth_length = 14
    eth_header = packet[:eth_length]
    eth = struct.unpack('!6s6sH', eth_header)
    eth_protocol = socket.ntohs(eth[2])
    print(f'Destination MAC: {eth_header[0:6].hex()}')
    print(f'Source MAC: {eth_header[6:12].hex()}')
    print(f'Protocol: {eth_protocol}')

    # Parse IP header
    if eth_protocol == 8:  # IPv4
        ip_header = packet[eth_length:20+eth_length]
        iph = struct.unpack('!BBHHHBBH4s4s', ip_header)
        version_ihl = iph[0]
        ihl = version_ihl & 0xF
        iph_length = ihl * 4
        protocol = iph[6]
        s_addr = socket.inet_ntoa(iph[8])
        d_addr = socket.inet_ntoa(iph[9])
        print(f'IP Version: {version_ihl >> 4}')
        print(f'IP Header Length: {ihl}')
        print(f'Protocol: {protocol}')
        print(f'Source Address: {s_addr}')
        print(f'Destination Address: {d_addr}')

        # Parse TCP/UDP header
        if protocol == 6:  # TCP
            t = iph_length + eth_length
            tcp_header = packet[t:t+20]
            tcph = struct.unpack('!HHLLBBHHH', tcp_header)
            source_port = tcph[0]
            dest_port = tcph[1]
            sequence = tcph[2]
            acknowledgement = tcph[3]
            print(f'TCP Source Port: {source_port}')
            print(f'TCP Destination Port: {dest_port}')
            print(f'Sequence Number: {sequence}')
            print(f'Acknowledgement: {acknowledgement}')
        elif protocol == 17:  # UDP
            u = iph_length + eth_length
            udp_header = packet[u:u+8]
            udph = struct.unpack('!HHHH', udp_header)
            source_port = udph[0]
            dest_port = udph[1]
            print(f'UDP Source Port: {source_port}')
            print(f'UDP Destination Port: {dest_port}')

def main():
    s = create_raw_socket()
    print('Capturing outgoing packets. Press Ctrl+C to stop.')
    try:
        while True:
            packet = s.recvfrom(65565)
            packet = packet[0]
            print('\nOutgoing Packet Detected:')
            analyze_packet(packet)
    except KeyboardInterrupt:
        print('\nPacket capture stopped.')

if __name__ == "__main__":
    main()