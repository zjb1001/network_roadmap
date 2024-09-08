#!/bin/bash

# This script demonstrates various network diagnostic commands

# 1. Ping test
echo "Ping test to google.com:"
ping -c 4 google.com

# 2. Traceroute
echo -e "\nTraceroute to google.com:"
traceroute google.com

# 3. Network connections and listening ports
echo -e "\nNetwork connections and listening ports (netstat):"
netstat -tuln

echo -e "\nNetwork connections and listening ports (ss):"
ss -tuln

# 4. DNS lookup
echo -e "\nDNS lookup for google.com:"
nslookup google.com

# 5. Check network interface statistics
echo -e "\nNetwork interface statistics:"
ifconfig

# 6. Display the local IP address
echo -e "\nLocal IP address:"
hostname -I

# 7. Show ARP cache
echo -e "\nARP cache:"
arp -e

# These commands don't require root privileges and are safe to run on most systems