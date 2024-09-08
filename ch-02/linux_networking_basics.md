# Linux Networking Basics

This chapter covers the fundamental tools and concepts for networking in Linux systems.

## 1. Network Configuration Tools

### 1.1 ip Command

The `ip` command is a powerful tool for configuring network interfaces, routing tables, and more.

#### Key operations:
- Show interface information: `ip addr show`
- Bring an interface up/down: `ip link set dev eth0 up/down`
- Assign an IP address: `ip addr add 192.168.1.100/24 dev eth0`
- Show routing table: `ip route show`

### 1.2 ifconfig Command (legacy)

While `ip` is the modern tool, `ifconfig` is still used in many systems.

Example usage:
```bash
ifconfig eth0 192.168.1.100 netmask 255.255.255.0 up
```

### 1.3 route Command

Used for viewing and manipulating the IP routing table.

Example:
```bash
route add default gw 192.168.1.1
```

## 2. Network Diagnostics

### 2.1 ping

Used to test the reachability of a host on an IP network.

Example:
```bash
ping -c 4 google.com
```

### 2.2 traceroute

Displays the route and measures transit delays of packets across an IP network.

Example:
```bash
traceroute google.com
```

### 2.3 netstat

Displays network connections, routing tables, interface statistics, masquerade connections, and multicast memberships.

Example:
```bash
netstat -tuln
```

### 2.4 ss

A more powerful and faster replacement for netstat.

Example:
```bash
ss -tuln
```

## 3. Network Services Configuration

### 3.1 DHCP Configuration

DHCP (Dynamic Host Configuration Protocol) is used to automatically assign IP addresses to devices on a network.

Example configuration in `/etc/dhcpcd.conf`:
```
interface eth0
static ip_address=192.168.0.10/24
static routers=192.168.0.1
static domain_name_servers=192.168.0.1 8.8.8.8
```

### 3.2 DNS Configuration

DNS (Domain Name System) resolves domain names to IP addresses.

Example configuration in `/etc/resolv.conf`:
```
nameserver 8.8.8.8
nameserver 8.8.4.4
```

## Practical Exercises

1. Network Interface Configuration
2. Routing Table Manipulation
3. Network Diagnostics
4. DHCP and DNS Setup

(See accompanying scripts for hands-on practice)