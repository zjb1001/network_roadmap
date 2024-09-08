#!/bin/bash

# This script demonstrates various network configuration commands

# 1. Display network interface information
echo "Network Interface Information:"
ip addr show

# 2. Bring an interface down and up (replace eth0 with your interface name)
echo -e "\nBringing eth0 down and up:"
sudo ip link set dev eth0 down
sudo ip link set dev eth0 up

# 3. Assign a static IP address (replace with appropriate values for your network)
echo -e "\nAssigning static IP:"
sudo ip addr add 192.168.1.100/24 dev eth0

# 4. Display routing table
echo -e "\nRouting Table:"
ip route show

# 5. Add a default gateway (replace with your gateway IP)
echo -e "\nAdding default gateway:"
sudo ip route add default via 192.168.1.1

# Note: Some of these commands require root privileges and may disrupt your current network connection
# Use with caution on a live system