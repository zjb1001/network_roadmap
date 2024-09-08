#!/bin/bash

# This script demonstrates various network configuration commands

# Function to capture and display network changes
capture_changes() {
    echo "Capturing network changes..."
    ip addr show > before.txt
    ip route show >> before.txt
    $1
    ip addr show > after.txt
    ip route show >> after.txt
    echo "Changes made:"
    diff before.txt after.txt
    rm before.txt after.txt
}

# 1. Display initial network interface information
echo "Initial Network Interface Information:"
ip addr show

# 2. Bring an interface down and up (replace eth0 with your interface name)
echo -e "\nBringing eth0 down and up:"
capture_changes "sudo ip link set dev eth0 down && sudo ip link set dev eth0 up"

# 3. Assign a static IP address (replace with appropriate values for your network)
echo -e "\nAssigning static IP:"
capture_changes "sudo ip addr add 192.168.1.100/24 dev eth0"

# 4. Display routing table
echo -e "\nInitial Routing Table:"
ip route show

# 5. Add a default gateway (replace with your gateway IP)
echo -e "\nAdding default gateway:"
capture_changes "sudo ip route add default via 192.168.1.1"

# 6. Monitor network traffic (run for 10 seconds)
echo -e "\nMonitoring network traffic for 10 seconds:"
sudo tcpdump -i eth0 -c 100 -t

# 7. Check system logs for network-related messages
echo -e "\nRecent network-related system logs:"
sudo journalctl --since "1 minute ago" | grep -i "network\|eth0\|ip\|route"

# Note: Some of these commands require root privileges and may disrupt your current network connection
# Use with caution on a live system