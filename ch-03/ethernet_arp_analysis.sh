#!/bin/bash

# This script demonstrates Ethernet and ARP analysis

# Function to run a command and display its output
run_command() {
    echo "Running: $1"
    eval $1
    echo
}

# 1. Display Ethernet interfaces
run_command "ip link show"

# 2. Show MAC address of a specific interface (replace eth0 with your interface name)
run_command "ip link show eth0 | grep ether"

# 3. Display ARP cache
run_command "arp -e"

# 4. Capture ARP traffic
echo "Capturing ARP traffic for 30 seconds..."
run_command "sudo tcpdump -i eth0 arp -v -c 10"

# 5. Manually add an ARP entry (replace with appropriate IP and MAC)
run_command "sudo arp -s 192.168.1.100 00:11:22:33:44:55"

# 6. Remove the manually added ARP entry
run_command "sudo arp -d 192.168.1.100"

# 7. Clear the entire ARP cache
run_command "sudo ip -s -s neigh flush all"

echo "Ethernet and ARP analysis completed."
#!/bin/bash

# Ethernet and ARP Analysis Script

# Capture Ethernet frames
echo "Capturing Ethernet frames..."
sudo tcpdump -i eth0 -nn -c 10 -e

# Capture ARP packets
echo "Capturing ARP packets..."
sudo tcpdump -i eth0 -nn arp -c 5

# Display ARP cache
echo "Current ARP cache:"
arp -e

# Flush ARP cache and observe ARP requests
echo "Flushing ARP cache and observing new ARP requests..."
sudo ip -s -s neigh flush all
sudo tcpdump -i eth0 -nn arp -c 5

echo "Ethernet and ARP analysis complete."