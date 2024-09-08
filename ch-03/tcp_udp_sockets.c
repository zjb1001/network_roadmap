#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>

#define TCP_PORT 8080
#define UDP_PORT 8081
#define BUFFER_SIZE 1024

void handle_tcp_client(int client_socket) {
    char buffer[BUFFER_SIZE] = {0};
    recv(client_socket, buffer, BUFFER_SIZE, 0);
    printf("Received TCP message: %s\n", buffer);
    send(client_socket, buffer, strlen(buffer), 0);
    close(client_socket);
}

void start_tcp_server() {
    int server_fd, client_socket;
    struct sockaddr_in address;
    int addrlen = sizeof(address);

    server_fd = socket(AF_INET, SOCK_STREAM, 0);
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(TCP_PORT);

    bind(server_fd, (struct sockaddr *)&address, sizeof(address));
    listen(server_fd, 3);

    printf("TCP Server listening on port %d\n", TCP_PORT);

    while(1) {
        client_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t*)&addrlen);
        handle_tcp_client(client_socket);
    }
}

void start_udp_server() {
    int server_fd;
    char buffer[BUFFER_SIZE] = {0};
    struct sockaddr_in address, client_addr;
    int addrlen = sizeof(address);

    server_fd = socket(AF_INET, SOCK_DGRAM, 0);
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(UDP_PORT);

    bind(server_fd, (struct sockaddr *)&address, sizeof(address));

    printf("UDP Server listening on port %d\n", UDP_PORT);

    while(1) {
        int len = recvfrom(server_fd, buffer, BUFFER_SIZE, 0, (struct sockaddr *)&client_addr, &addrlen);
        buffer[len] = '\0';
        printf("Received UDP message: %s\n", buffer);
        sendto(server_fd, buffer, strlen(buffer), 0, (struct sockaddr *)&client_addr, addrlen);
    }
}

int main() {
    if (fork() == 0) {
        start_tcp_server();
    } else {
        start_udp_server();
    }
    return 0;
}