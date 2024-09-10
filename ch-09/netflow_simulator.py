import random
import time
import socket
import struct

def generate_netflow_packet(start_time, end_time, packets, octets):
    version = 5
    count = 1
    sys_uptime = int(time.time() * 1000)
    unix_secs = int(time.time())
    unix_nsecs = 0
    flow_sequence = random.randint(0, 65535)
    engine_type = 0
    engine_id = 0

    src_addr = socket.inet_aton(f"192.168.1.{random.randint(1, 254)}")
    dst_addr = socket.inet_aton(f"10.0.0.{random.randint(1, 254)}")
    next_hop = socket.inet_aton("0.0.0.0")
    input_iface = random.randint(0, 65535)
    output_iface = random.randint(0, 65535)
    src_port = random.randint(1024, 65535)
    dst_port = random.randint(1, 1023)
    pad1 = 0
    tcp_flags = random.randint(0, 63)
    prot = random.choice([6, 17])  # TCP or UDP
    tos = 0
    src_as = random.randint(1, 65535)
    dst_as = random.randint(1, 65535)
    src_mask = 24
    dst_mask = 24
    pad2 = 0

    header = struct.pack('!HHIIIIBBH', version, count, sys_uptime, unix_secs, unix_nsecs, flow_sequence, engine_type, engine_id, 0)
    record = struct.pack('!IIIHHIIIIHHBBBBHHBBH', 
        struct.unpack('!I', src_addr)[0], struct.unpack('!I', dst_addr)[0], struct.unpack('!I', next_hop)[0],
        input_iface, output_iface, packets, octets, start_time, end_time, src_port, dst_port,
        pad1, tcp_flags, prot, tos, src_as, dst_as, src_mask, dst_mask, pad2)

    return header + record

def send_netflow_packets(target_ip, target_port, duration, interval):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    start_time = int(time.time())
    end_time = start_time + duration
    total_packets = 0
    total_octets = 0

    while time.time() < end_time:
        packets = random.randint(100, 1000)
        octets = packets * random.randint(64, 1500)
        total_packets += packets
        total_octets += octets
        
        packet = generate_netflow_packet(int(time.time()), int(time.time()) + interval, packets, octets)
        sock.sendto(packet, (target_ip, target_port))
        time.sleep(interval)

    sock.close()
    return total_packets, total_octets

if __name__ == "__main__":
    target_ip = "127.0.0.1"
    target_port = 9995
    duration = 60  # Run for 60 seconds
    interval = 5   # Send a Netflow packet every 5 seconds

    print(f"Sending Netflow packets to {target_ip}:{target_port} for {duration} seconds")
    total_packets, total_octets = send_netflow_packets(target_ip, target_port, duration, interval)
    print(f"Sent Netflow data representing {total_packets} packets and {total_octets} bytes")