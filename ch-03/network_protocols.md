# Chapter 3: Network Protocols

This chapter covers fundamental network protocols essential for understanding the Linux network stack. We'll explore each protocol with practical examples and packet capture analysis.

## 1. Ethernet and ARP (Address Resolution Protocol)

### 1.1 Ethernet
Ethernet is the most widely used LAN (Local Area Network) technology. It operates at the Data Link Layer of the OSI model.

Key concepts:
- MAC (Media Access Control) addresses
- Frame structure
- CSMA/CD (Carrier Sense Multiple Access with Collision Detection)

### 1.2 ARP (Address Resolution Protocol)
ARP is used to map IP addresses to MAC addresses in a local network.

Key concepts:
- ARP cache
- ARP request and reply messages

Practical Example: See `ethernet_arp_analysis.sh` for Ethernet and ARP packet capture and analysis.

## 2. IPv4 and IPv6

### 2.1 IPv4 (Internet Protocol version 4)
IPv4 is the fourth version of the Internet Protocol and the most widely used protocol for data communication on the Internet.

Key concepts:
- IP addressing and subnetting
- IP header structure
- Fragmentation and reassembly

### 2.2 IPv6 (Internet Protocol version 6)
IPv6 is the most recent version of the Internet Protocol, designed to eventually replace IPv4.

Key concepts:
- 128-bit addressing
- Simplified header structure
- Built-in security features

Practical Example: See `ip_packet_analyzer.py` for IPv4 and IPv6 packet capture and analysis.

## 3. TCP (Transmission Control Protocol) and UDP (User Datagram Protocol)

### 3.1 TCP
TCP is a connection-oriented protocol that provides reliable, ordered, and error-checked delivery of data.

Key concepts:
- Three-way handshake
- Flow control and congestion control
- Sequence and acknowledgment numbers

### 3.2 UDP
UDP is a connectionless protocol that provides a simple, unreliable datagram service.

Key concepts:
- Lightweight header
- No guarantee of delivery, ordering, or duplicate protection
- Suitable for real-time applications

Practical Example: See `tcp_udp_analyzer.py` for TCP and UDP packet capture and analysis.

## 4. ICMP (Internet Control Message Protocol)

ICMP is used by network devices to send error messages and operational information.

Key concepts:
- ICMP message types (e.g., Echo Request/Reply, Destination Unreachable)
- Ping and Traceroute utilities

Practical Example: See `icmp_analyzer.py` for ICMP packet capture and analysis.

## 5. Common Application Layer Protocols

### 5.1 HTTP/HTTPS (Hypertext Transfer Protocol / Secure)
Used for transmitting hypermedia documents on the World Wide Web.

### 5.2 FTP (File Transfer Protocol)
Used for transferring files between clients and servers on a network.

### 5.3 SSH (Secure Shell)
A cryptographic network protocol for secure data communication, remote command-line login, remote command execution, and other secure network services.

Practical Example: See `application_layer_analyzer.py` for HTTP, FTP, and SSH packet capture and analysis.

## Practical Exercises

1. Run `ethernet_arp_analysis.sh` to capture and analyze Ethernet and ARP packets.
2. Use `ip_packet_analyzer.py` to examine IPv4 and IPv6 packets.
3. Analyze TCP and UDP traffic using `tcp_udp_analyzer.py`.
4. Capture and examine ICMP packets with `icmp_analyzer.py`.
5. Study application layer protocols using `application_layer_analyzer.py`.

These exercises will provide hands-on experience with network protocols and deepen your understanding of their purposes and behaviors.