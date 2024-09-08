#!/bin/bash

echo "Network Security Test Script"
echo "============================"

# Test iptables
echo "Testing iptables..."
sudo iptables -L
echo ""

# Test nftables
echo "Testing nftables..."
sudo nft list ruleset
echo ""

# Test SELinux
echo "Testing SELinux..."
sestatus
echo ""

# Test OpenVPN
echo "Testing OpenVPN..."
sudo systemctl status openvpn
echo ""

# Test IPsec (strongSwan)
echo "Testing IPsec (strongSwan)..."
sudo ipsec status
echo ""

# Test Snort
echo "Testing Snort..."
sudo systemctl status snort
echo ""

# Test Suricata
echo "Testing Suricata..."
sudo systemctl status suricata
echo ""

echo "Network security test complete."