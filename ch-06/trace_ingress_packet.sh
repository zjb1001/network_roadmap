#!/bin/bash

# Check if running as root
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

# Function to enable tracing
enable_tracing() {
    echo 1 > /sys/kernel/debug/tracing/events/net/netif_receive_skb/enable
    echo 1 > /sys/kernel/debug/tracing/events/net/net_dev_queue/enable
    echo 1 > /sys/kernel/debug/tracing/events/net/napi_gro_receive_entry/enable
    echo 1 > /sys/kernel/debug/tracing/events/net/netif_rx/enable
    echo 1 > /sys/kernel/debug/tracing/tracing_on
}

# Function to disable tracing
disable_tracing() {
    echo 0 > /sys/kernel/debug/tracing/tracing_on
    echo 0 > /sys/kernel/debug/tracing/events/net/netif_receive_skb/enable
    echo 0 > /sys/kernel/debug/tracing/events/net/net_dev_queue/enable
    echo 0 > /sys/kernel/debug/tracing/events/net/napi_gro_receive_entry/enable
    echo 0 > /sys/kernel/debug/tracing/events/net/netif_rx/enable
}

# Main script
echo "Enabling packet tracing..."
enable_tracing

echo "Generating network traffic (ping to google.com)..."
ping -c 5 google.com > /dev/null

echo "Disabling packet tracing..."
disable_tracing

echo "Trace output:"
cat /sys/kernel/debug/tracing/trace

echo "Trace complete."