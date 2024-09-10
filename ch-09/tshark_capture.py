import subprocess
import sys

def capture_packets_tshark(interface, output_file, count=100):
    try:
        command = f"tshark -i {interface} -c {count} -w {output_file}"
        subprocess.run(command, shell=True, check=True)
        print(f"Captured {count} packets and saved to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error running tshark: {e}", file=sys.stderr)

if __name__ == "__main__":
    interface = input("Enter the network interface to capture (e.g., eth0): ")
    count = int(input("Enter the number of packets to capture: "))
    output_file = input("Enter the output file name (e.g., captured_packets.pcap): ")
    capture_packets_tshark(interface, output_file, count)