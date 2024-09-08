# Chapter 6: Packet Flow in Linux

This chapter explores the journey of network packets through the Linux kernel, focusing on the key stages of packet processing.

## 1. Ingress Packet Processing

When a packet arrives at a network interface:
- Hardware generates an interrupt
- Device driver handles the interrupt and retrieves the packet
- Packet is placed in a ring buffer
- Soft IRQ is raised to process the packet
- Packet traverses the network stack (e.g., IP, TCP/UDP layers)

## 2. Egress Packet Processing

When an application sends data:
- Data is passed through the socket interface
- TCP/IP stack processes the data (segmentation, adding headers)
- Packet is queued for transmission
- QoS and traffic control may be applied
- Device driver sends the packet to the network interface

## 3. Routing Subsystem

The routing subsystem determines where packets should be sent:
- Routing table lookup
- Longest prefix match algorithm
- Policy-based routing
- Netfilter hooks for custom routing logic

## 4. Bridging Subsystem

Bridging allows connecting multiple network segments at the data link layer:
- Bridge device creation and management
- MAC address learning
- STP (Spanning Tree Protocol) implementation
- VLAN support

## Practical Exercises

1. Trace ingress packet flow
2. Analyze egress packet processing
3. Explore Linux routing tables and policies
4. Set up a software bridge

These exercises will provide hands-on experience with packet flow in the Linux kernel.