# 1. tcpdump and Wireshark

## Introduction to packet capture and analysis

Packet capture and analysis are essential skills for network administrators and security professionals. These techniques allow you to inspect the actual data flowing through your network, helping you troubleshoot issues, detect security threats, and understand network behavior.

## Using tcpdump for command-line packet capture

tcpdump is a powerful command-line tool for capturing and analyzing network traffic. Here's a basic example of how to use it:

```bash
sudo tcpdump -i eth0 -n
```

This command captures packets on the eth0 interface and displays them in a human-readable format.

Let's create a Python script to demonstrate how to use tcpdump programmatically:

```python
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
    interface = "eth0"  # Change this to your network interface
    captured_data = capture_packets(interface)
    if captured_data:
        print(captured_data)
```

Save this script as `tcpdump_capture.py` and run it with sudo privileges:

```bash
sudo python3 tcpdump_capture.py
```

## Wireshark for GUI-based packet analysis

Wireshark provides a user-friendly graphical interface for packet analysis. While we can't programmatically interact with Wireshark's GUI, we can use its command-line counterpart, tshark, in our scripts.

Here's a Python script that uses tshark to capture packets and save them to a file:

```python
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
    interface = "eth0"  # Change this to your network interface
    output_file = "captured_packets.pcap"
    capture_packets_tshark(interface, output_file)
```

Save this script as `tshark_capture.py` and run it with sudo privileges:

```bash
sudo python3 tshark_capture.py
```

After running this script, you can open the `captured_packets.pcap` file in Wireshark for detailed analysis.

## Practical examples and use cases

1. Monitoring HTTP traffic:
   ```bash
   sudo tcpdump -i eth0 port 80
   ```

2. Capturing packets from a specific IP:
   ```bash
   sudo tcpdump -i eth0 host 192.168.1.100
   ```

3. Analyzing DNS queries:
   ```bash
   sudo tcpdump -i eth0 udp port 53
   ```

These examples demonstrate how tcpdump can be used to focus on specific types of network traffic, which is crucial for troubleshooting and security analysis.

To observe the effects of these commands, run them on a live network interface and observe the output. You'll see detailed information about the packets matching your specified criteria, including source and destination IP addresses, protocols, and payload data.
