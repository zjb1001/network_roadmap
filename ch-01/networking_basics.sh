#!/bin/bash

# Basic Networking Commands
echo "Testing basic networking commands..."

# 1. Ping
echo "Pinging google.com:"
ping -c 4 google.com

# 2. Traceroute
echo
echo "Traceroute to google.com:"
traceroute google.com

# 3. Netstat
echo
echo "Netstat - Active Internet connections:"
netstat -tuln

# 4. SS (Socket Statistics)
echo
echo "SS - Socket Statistics:"
ss -tuln

# 5. IP command
echo
echo "IP Address information:"
ip addr show

# 6. Route
echo
echo "Routing Table:"
route -n

echo "Basic networking commands test completed."