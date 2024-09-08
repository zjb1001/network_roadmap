#!/bin/bash

# Check if running as root
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

# Function to start tracing
start_trace() {
    echo "Starting packet flow trace..."
    # Use ftrace to trace network-related functions
    echo 1 > /sys/kernel/debug/tracing/events/net/net_dev_queue/enable
    echo 1 > /sys/kernel/debug/tracing/events/net/net_dev_xmit/enable
    echo 1 > /sys/kernel/debug/tracing/events/net/netif_receive_skb/enable
    echo 1 > /sys/kernel/debug/tracing/tracing_on
}

# Function to stop tracing
stop_trace() {
    echo "Stopping packet flow trace..."
    echo 0 > /sys/kernel/debug/tracing/tracing_on
    echo 0 > /sys/kernel/debug/tracing/events/net/net_dev_queue/enable
    echo 0 > /sys/kernel/debug/tracing/events/net/net_dev_xmit/enable
    echo 0 > /sys/kernel/debug/tracing/events/net/netif_receive_skb/enable
}

# Function to display trace
show_trace() {
    echo "Displaying packet flow trace:"
    cat /sys/kernel/debug/tracing/trace
}

# Main script
start_trace

echo "Generating network traffic... (ping google.com)"
ping -c 5 google.com > /dev/null

stop_trace
show_trace

echo "Trace complete."