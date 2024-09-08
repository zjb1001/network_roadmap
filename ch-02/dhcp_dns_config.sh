#!/bin/bash

# This script demonstrates DHCP and DNS configuration
# Note: This script requires root privileges and will modify system files
# Use with caution on a live system

# 1. Backup current configurations
echo "Backing up current configurations..."
sudo cp /etc/dhcpcd.conf /etc/dhcpcd.conf.bak
sudo cp /etc/resolv.conf /etc/resolv.conf.bak

# 2. Configure DHCP
echo "Configuring DHCP..."
echo "
# Static IP configuration for eth0
interface eth0
static ip_address=192.168.1.100/24
static routers=192.168.1.1
static domain_name_servers=8.8.8.8 8.8.4.4
" | sudo tee -a /etc/dhcpcd.conf

# 3. Configure DNS
echo "Configuring DNS..."
echo "
nameserver 8.8.8.8
nameserver 8.8.4.4
" | sudo tee /etc/resolv.conf

# 4. Restart networking service
echo "Restarting networking service..."
sudo systemctl restart networking

# 5. Display new configurations
echo "New DHCP configuration:"
cat /etc/dhcpcd.conf
echo -e "\nNew DNS configuration:"
cat /etc/resolv.conf

echo -e "\nConfiguration complete. Please reboot or restart networking for changes to take effect."

# Note: This script provides a basic example and may need adjustments based on your specific system and requirements