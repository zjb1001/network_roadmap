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

#### Observing effects:
- Use `ip addr show` before and after making changes to see the differences
- Monitor network traffic with `tcpdump` or `wireshark` to see how changes affect packet flow

### 1.2 ifconfig Command (legacy)

While `ip` is the modern tool, `ifconfig` is still used in many systems.

Example usage:
```bash
ifconfig eth0 192.168.1.100 netmask 255.255.255.0 up
```

#### Observing effects:
- Use `ifconfig` before and after making changes to see the differences
- Check system logs (`/var/log/syslog` or `journalctl`) for any related messages

### 1.3 route Command

Used for viewing and manipulating the IP routing table.

Example:
```bash
route add default gw 192.168.1.1
```

#### Observing effects:
- Use `route -n` before and after making changes to see the differences
- Try `traceroute` to a remote host to see how the routing changes affect the path

## 2. Network Diagnostics

### 2.1 ping

Used to test the reachability of a host on an IP network.

Example:
```bash
ping -c 4 google.com
```

#### Observing effects:
- Look at the round-trip times and packet loss statistics
- Use `ping` with different packet sizes (`-s` option) to test network performance

### 2.2 traceroute

Displays the route and measures transit delays of packets across an IP network.

Example:
```bash
traceroute google.com
```

#### Observing effects:
- Compare results at different times of day to see how network congestion affects routes
- Use `mtr` (My TraceRoute) for a continuous, updated view of the route

### 2.3 netstat

Displays network connections, routing tables, interface statistics, masquerade connections, and multicast memberships.

Example:
```bash
netstat -tuln
```

#### Observing effects:
- Run before and after starting a network service to see new listening ports
- Use `watch netstat -tuln` to see real-time changes in network connections

### 2.4 ss

A more powerful and faster replacement for netstat.

Example:
```bash
ss -tuln
```

#### Observing effects:
- Compare output with netstat to see any differences
- Use `ss -i` to see detailed socket statistics

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

#### Observing effects:
- Restart the DHCP client (`sudo systemctl restart dhcpcd`) and check `ip addr show` for changes
- Monitor DHCP traffic with `tcpdump -i eth0 port 67 or port 68`

### 3.2 DNS Configuration

DNS (Domain Name System) resolves domain names to IP addresses.

Example configuration in `/etc/resolv.conf`:
```
nameserver 8.8.8.8
nameserver 8.8.4.4
```

#### Observing effects:
- Use `dig` or `nslookup` to query domain names and see which DNS server responds
- Monitor DNS traffic with `tcpdump -i eth0 port 53`

## Practical Exercises

1. Network Interface Configuration
2. Routing Table Manipulation
3. Network Diagnostics
4. DHCP and DNS Setup

(See accompanying scripts for hands-on practice)

## Observation Tools and Techniques

1. Packet Capture: Use `tcpdump` or Wireshark to capture and analyze network traffic.
2. System Logs: Check `/var/log/syslog` or use `journalctl` to view system logs related to network changes.
3. Real-time Monitoring: Use tools like `iftop` to monitor bandwidth usage in real-time.
4. Network Statistics: Utilize `netstat`, `ss`, or `ip -s link` for detailed network statistics.
5. Continuous Monitoring: Use `watch` command with network tools for real-time updates.
6. Performance Testing: Use tools like `iperf3` to test network throughput.
7. Visual Traceroute: Use `mtr` for a continuously updated traceroute.
8. Socket Statistics: Employ `ss -i` for detailed socket statistics.
9. DNS Debugging: Use `dig +trace` for step-by-step DNS resolution.
10. Network Graphing: Use tools like `vnstat` to generate long-term network usage graphs.

Remember to always use these tools responsibly and with proper authorization, especially on networks you don't own or manage.