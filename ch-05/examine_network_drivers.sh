#!/bin/bash

echo "Network Device Driver Information:"
echo "=================================="

# List all network interfaces
interfaces=$(ls /sys/class/net/)

for interface in $interfaces
do
    echo "Interface: $interface"
    
    # Get driver information
    driver=$(readlink /sys/class/net/$interface/device/driver/module)
    driver=${driver##*/}
    echo "Driver: $driver"
    
    # Get driver version
    if [ -f "/sys/class/net/$interface/device/driver/module/version" ]; then
        version=$(cat /sys/class/net/$interface/device/driver/module/version)
        echo "Driver Version: $version"
    fi
    
    # Get device information
    if [ -f "/sys/class/net/$interface/device/uevent" ]; then
        dev_info=$(cat /sys/class/net/$interface/device/uevent)
        echo "Device Info: $dev_info"
    fi
    
    echo "-----------------------------------"
done

echo "Done."