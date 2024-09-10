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