# Chapter 4: Socket Programming

This chapter covers the fundamentals of socket programming, which is essential for understanding how network applications communicate at a low level.

## 1. Berkeley Sockets API

The Berkeley Sockets API is a standard interface for network programming. It provides a set of functions that allow applications to create network connections and exchange data.

Key concepts:
- Socket creation and configuration
- Binding sockets to addresses and ports
- Establishing connections (for TCP)
- Sending and receiving data
- Closing connections

## 2. Creating TCP and UDP Servers and Clients

We'll explore how to create both TCP (connection-oriented) and UDP (connectionless) servers and clients.

### 2.1 TCP Server and Client
- Server: socket creation, binding, listening, accepting connections, data exchange
- Client: socket creation, connecting to server, data exchange

### 2.2 UDP Server and Client
- Server: socket creation, binding, receiving datagrams
- Client: socket creation, sending datagrams

## 3. Non-blocking I/O and select/poll/epoll

These mechanisms allow for efficient handling of multiple connections without using multiple threads or processes.

- Non-blocking I/O: Setting sockets to non-blocking mode
- select(): Monitoring multiple file descriptors
- poll(): A more efficient alternative to select()
- epoll(): A scalable I/O event notification mechanism (Linux-specific)

## Practical Exercises

1. Implement a simple TCP echo server and client
2. Create a UDP-based chat application
3. Build a multi-client TCP server using select()
4. Develop a high-performance server using epoll()

These exercises will provide hands-on experience with socket programming concepts and techniques.