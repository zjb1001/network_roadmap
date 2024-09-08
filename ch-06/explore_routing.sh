#!/bin/bash

echo "Current Routing Table:"
ip route show
echo

echo "Policy Routing Tables:"
ip rule show
echo

echo "Detailed Route Information:"
ip route show table all
echo

echo "Route Cache (if available):"
ip route show cache
echo

echo "Routing Statistics:"
ip -s route
echo

echo "Exploring a specific route to 8.8.8.8:"
ip route get 8.8.8.8
echo

echo "Routing exploration complete."