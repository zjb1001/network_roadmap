#!/bin/bash

# Basic Networking Commands
echo "Testing basic networking commands..."

# 1. Ping
echo "Pinging google.com:"
ping -c 4 google.com

# 2. Traceroute
echo -e "\nTraceroute to google.com:"
traceroute google.com

# 3. Netstat
echo -e "\nNetstat - Active Internet connections:"
netstat -tuln

# 4. SS (Socket Statistics)
echo -e "\nSS - Socket Statistics:"
ss -tuln

# 5. IP command
echo -e "\nIP Address information:"
ip addr show

# 6. Route
echo -e "\nRouting Table:"
route -n

echo "Basic networking commands test completed."