#!/bin/bash

# Check if running as root
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

# Function to create a veth pair
create_veth_pair() {
    echo "Creating veth pair: $1 <-> $2"
    ip link add $1 type veth peer name $2
    ip link set $1 up
    ip link set $2 up
}

# Function to create a Linux bridge
create_bridge() {
    echo "Creating Linux bridge: $1"
    ip link add name $1 type bridge
    ip link set $1 up
}

# Function to add interface to bridge
add_to_bridge() {
    echo "Adding $1 to bridge $2"
    ip link set $1 master $2
}

# Function to create a TUN/TAP device
create_tuntap() {
    echo "Creating TUN/TAP device: $1"
    ip tuntap add dev $1 mode tap
    ip link set $1 up
}

# Main setup
echo "Setting up virtual network..."

# Create a bridge
create_bridge br0

# Create veth pair
create_veth_pair veth0 veth1

# Add one end of veth pair to bridge
add_to_bridge veth0 br0

# Create a TUN/TAP device
create_tuntap tap0

# Add TUN/TAP device to bridge
add_to_bridge tap0 br0

echo "Virtual network setup complete. Network topology:"
echo "veth1 <-> veth0 <-> br0 <-> tap0"

# Display network interfaces
ip link show

echo "Setup complete. You can now use these interfaces for further networking experiments."

echo "For a Python-based implementation of this setup, please refer to virtual_network_simulator.py"