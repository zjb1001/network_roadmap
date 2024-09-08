# Chapter 3: Network Protocols

This chapter covers fundamental network protocols essential for understanding the Linux network stack.

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

## 4. ICMP (Internet Control Message Protocol)

ICMP is used by network devices to send error messages and operational information.

Key concepts:
- ICMP message types (e.g., Echo Request/Reply, Destination Unreachable)
- Ping and Traceroute utilities

## 5. Common Application Layer Protocols

### 5.1 HTTP/HTTPS (Hypertext Transfer Protocol / Secure)
Used for transmitting hypermedia documents on the World Wide Web.

### 5.2 FTP (File Transfer Protocol)
Used for transferring files between clients and servers on a network.

### 5.3 SSH (Secure Shell)
A cryptographic network protocol for secure data communication, remote command-line login, remote command execution, and other secure network services.

## Practical Exercises

1. Ethernet and ARP analysis
2. IPv4 and IPv6 packet examination
3. TCP and UDP socket programming
4. ICMP ping and traceroute implementation
5. Simple HTTP server and client

(See accompanying scripts and programs for hands-on practice)