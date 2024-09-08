#!/bin/bash

# Check if running as root
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

# Function to display current network settings
show_current_settings() {
    echo "Current Network Settings:"
    echo "------------------------"
    echo "TCP Window Scaling: $(sysctl net.ipv4.tcp_window_scaling)"
    echo "TCP Timestamps: $(sysctl net.ipv4.tcp_timestamps)"
    echo "TCP SACK: $(sysctl net.ipv4.tcp_sack)"
    echo "TCP Congestion Control: $(sysctl net.ipv4.tcp_congestion_control)"
    echo "Network Interface Queue Length: $(sysctl net.core.netdev_max_backlog)"
    echo "------------------------"
}

# Function to optimize TCP settings
optimize_tcp() {
    echo "Optimizing TCP settings..."
    sysctl -w net.ipv4.tcp_window_scaling=1
    sysctl -w net.ipv4.tcp_timestamps=1
    sysctl -w net.ipv4.tcp_sack=1
    sysctl -w net.ipv4.tcp_congestion_control=cubic
    sysctl -w net.core.netdev_max_backlog=5000
    echo "TCP settings optimized."
}

# Function to run a network benchmark
run_benchmark() {
    echo "Running network benchmark..."
    if ! command -v iperf3 &> /dev/null
    then
        echo "iperf3 could not be found. Please install it to run benchmarks."
        return
    fi
    iperf3 -c iperf.he.net -t 10
}

# Main menu
while true; do
    echo "
    Network Performance Tuner
    1. Show current settings
    2. Optimize TCP settings
    3. Run network benchmark
    4. Exit
    "
    read -p "Enter your choice: " choice

    case $choice in
        1)
            show_current_settings
            ;;
        2)
            optimize_tcp
            ;;
        3)
            run_benchmark
            ;;
        4)
            echo "Exiting..."
            exit 0
            ;;
        *)
            echo "Invalid option"
            ;;
    esac
done