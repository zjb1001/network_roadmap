import subprocess
import sys

def capture_packets(interface, count=10):
    try:
        command = f"sudo tcpdump -i {interface} -c {count} -n"
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running tcpdump: {e}", file=sys.stderr)
        return None

if __name__ == "__main__":
    interface = input("Enter the network interface to capture (e.g., eth0): ")
    count = int(input("Enter the number of packets to capture: "))
    captured_data = capture_packets(interface, count)
    if captured_data:
        print(captured_data)
        
        # Save captured data to a file
        with open("captured_packets.txt", "w") as f:
            f.write(captured_data)
        print(f"Captured data saved to captured_packets.txt")