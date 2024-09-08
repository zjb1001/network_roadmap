#!/bin/bash

# This script demonstrates various network diagnostic commands

# Function to run a command and measure its execution time
run_timed_command() {
    echo "Running: $1"
    start_time=$(date +%s.%N)
    eval $1
    end_time=$(date +%s.%N)
    execution_time=$(echo "$end_time - $start_time" | bc)
    echo "Execution time: $execution_time seconds"
    echo
}

# 1. Ping test
echo "Ping test to google.com:"
run_timed_command "ping -c 4 google.com"

# 2. Traceroute
echo -e "Traceroute to google.com:"
run_timed_command "traceroute google.com"

# 3. Network connections and listening ports
echo -e "Network connections and listening ports (netstat):"
run_timed_command "netstat -tuln"

echo -e "Network connections and listening ports (ss):"
run_timed_command "ss -tuln"

# 4. DNS lookup
echo -e "DNS lookup for google.com:"
run_timed_command "nslookup google.com"

# 5. Check network interface statistics
echo -e "Network interface statistics:"
run_timed_command "ifconfig"

# 6. Display the local IP address
echo -e "Local IP address:"
run_timed_command "hostname -I"

# 7. Show ARP cache
echo -e "ARP cache:"
run_timed_command "arp -e"

# 8. Continuous network monitoring (run for 30 seconds)
echo -e "Continuous network monitoring (30 seconds):"
run_timed_command "timeout 30s iftop -t -s 5 || true"

# 9. Check open ports
echo -e "Open ports:"
run_timed_command "sudo lsof -i -P -n | grep LISTEN"

# 10. Display routing table
echo -e "Routing table:"
run_timed_command "route -n"

# These commands don't require root privileges and are safe to run on most systems
# except for the iftop and lsof commands which may require sudo