import socket
import time

def generate_traffic(target_ip, target_port, num_packets):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for i in range(num_packets):
        message = f"Packet {i+1}".encode()
        sock.sendto(message, (target_ip, target_port))
        time.sleep(0.1)  # Send a packet every 0.1 seconds
    sock.close()

if __name__ == "__main__":
    target_ip = "127.0.0.1"
    target_port = 12345
    num_packets = 100

    print(f"Generating {num_packets} packets of traffic...")
    generate_traffic(target_ip, target_port, num_packets)
    print("Traffic generation complete.")
import random
import time
import socket

def generate_traffic(duration, packets_per_second):
    start_time = time.time()
    total_packets = 0
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while time.time() - start_time < duration:
        for _ in range(packets_per_second):
            src_ip = f"192.168.1.{random.randint(1, 254)}"
            dst_ip = f"10.0.0.{random.randint(1, 254)}"
            src_port = random.randint(1024, 65535)
            dst_port = random.randint(1, 1023)
            payload = b"X" * random.randint(64, 1500)
            
            sock.sendto(payload, (dst_ip, dst_port))
            total_packets += 1
        
        time.sleep(1)
    
    sock.close()
    return total_packets

if __name__ == "__main__":
    duration = 60  # Run for 60 seconds
    packets_per_second = 100
    total_packets = generate_traffic(duration, packets_per_second)
    print(f"Generated {total_packets} packets over {duration} seconds")