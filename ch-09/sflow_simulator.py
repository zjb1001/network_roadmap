import random
import time
import socket
import struct

def generate_sflow_packet(sampling_rate, sample_pool, drops, frame_length):
    version = 5
    ip_version = 1  # IPv4
    agent_ip = socket.inet_aton("192.168.1.1")
    sub_agent_id = 0
    sequence_number = random.randint(0, 4294967295)
    uptime = int(time.time() * 1000)  # milliseconds
    num_samples = 1

    sample_type = 1  # Flow sample
    sample_length = 88
    source_id = random.randint(0, 4294967295)
    input_interface = random.randint(0, 4294967295)
    output_interface = random.randint(0, 4294967295)
    flow_records = 1

    record_type = 1  # Raw packet header
    flow_data_length = 52
    header_protocol = 1  # Ethernet
    stripped = 0
    header_length = 14 + 20 + 8  # Eth + IP + TCP/UDP headers

    header = struct.pack('!IIIIIII', version, ip_version, struct.unpack('!I', agent_ip)[0], sub_agent_id, sequence_number, uptime, num_samples)
    flow_sample = struct.pack('!IIIIIIIII', sample_type, sample_length, sequence_number, source_id, sampling_rate, sample_pool, drops, input_interface, output_interface)
    flow_record = struct.pack('!IIIIII', record_type, flow_data_length, header_protocol, frame_length, stripped, header_length)

    return header + flow_sample + flow_record + b'\x00' * header_length

def send_sflow_packets(target_ip, target_port, duration, interval, sampling_rate):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    start_time = time.time()
    end_time = start_time + duration
    total_packets = 0
    total_octets = 0

    while time.time() < end_time:
        sample_pool = random.randint(1000, 10000)
        drops = random.randint(0, 10)
        frame_length = random.randint(64, 1518)
        
        total_packets += sample_pool
        total_octets += sample_pool * frame_length
        
        packet = generate_sflow_packet(sampling_rate, sample_pool, drops, frame_length)
        sock.sendto(packet, (target_ip, target_port))
        time.sleep(interval)

    sock.close()
    return total_packets, total_octets

if __name__ == "__main__":
    target_ip = "127.0.0.1"
    target_port = 6343
    duration = 60  # Run for 60 seconds
    interval = 1   # Send an sFlow packet every 1 second
    sampling_rate = 100  # Sample 1 out of every 100 packets

    print(f"Sending sFlow packets to {target_ip}:{target_port} for {duration} seconds")
    total_packets, total_octets = send_sflow_packets(target_ip, target_port, duration, interval, sampling_rate)
    print(f"Sent sFlow data representing {total_packets} packets and {total_octets} bytes")