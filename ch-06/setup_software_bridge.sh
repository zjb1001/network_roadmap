#!/bin/bash

# Check if running as root
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

# Create a bridge
echo "Creating bridge br0..."
ip link add name br0 type bridge

# Add interfaces to the bridge (replace eth0 and eth1 with your actual interface names)
echo "Adding interfaces to the bridge..."
ip link set dev eth0 master br0
ip link set dev eth1 master br0

# Bring up the bridge and interfaces
echo "Bringing up the bridge and interfaces..."
ip link set dev br0 up
ip link set dev eth0 up
ip link set dev eth1 up

# Configure IP address for the bridge (adjust as needed)
echo "Configuring IP address for the bridge..."
ip addr add 192.168.1.1/24 dev br0

# Enable STP
echo "Enabling Spanning Tree Protocol..."
ip link set dev br0 type bridge stp_state 1

# Show bridge information
echo "Bridge information:"
bridge link show
bridge vlan show

echo "Software bridge setup complete."