import select
import socket

def start_server(host='127.0.0.1', port=65432):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(5)
    
    inputs = [server_socket]
    
    print(f"Server listening on {host}:{port}")
    
    while True:
        readable, _, _ = select.select(inputs, [], [])
        for sock in readable:
            if sock == server_socket:
                client_socket, client_address = server_socket.accept()
                print(f"New connection from {client_address}")
                inputs.append(client_socket)
            else:
                data = sock.recv(1024)
                if data:
                    print(f"Received data from {sock.getpeername()}: {data.decode()}")
                    sock.send(data)  # Echo back the received data
                else:
                    print(f"Closing connection from {sock.getpeername()}")
                    inputs.remove(sock)
                    sock.close()

if __name__ == "__main__":
    start_server()