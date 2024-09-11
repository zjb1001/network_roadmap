#!/bin/bash

# Install necessary packages
sudo apt-get update
sudo apt-get install -y gcc tcpdump netcat-openbsd

# Compile the C program
echo "Compiling simple_socket.c..."
gcc -o simple_socket simple_socket.c

# Start packet capture
echo "Starting packet capture..."
sudo tcpdump -i lo0 port 8080 -w capture.pcap &
TCPDUMP_PID=$!

# Run the server
echo "Running the server..."
./simple_socket &
SERVER_PID=$!

# Wait for the server to start
sleep 2

# Send a test message to the server
echo "Sending test message to server..."
echo "Hello, server!" | nc localhost 8080

# Wait for a moment to capture the response
sleep 2

# Stop the server and packet capture
echo "Stopping server and packet capture..."
kill $SERVER_PID
kill $TCPDUMP_PID

# Analyze the captured packets
echo "Analyzing captured packets..."
tcpdump -r capture.pcap -nn -A

echo "Test completed. Captured packets saved in capture.pcap"