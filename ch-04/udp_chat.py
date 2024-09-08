import socket
import threading

def receive_messages(sock):
    while True:
        data, addr = sock.recvfrom(1024)
        print(f"\nReceived message from {addr}: {data.decode()}")

def start_chat(host='127.0.0.1', port=65433):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        print(f"Chat started on {host}:{port}")
        
        # Start a thread to receive messages
        thread = threading.Thread(target=receive_messages, args=(s,))
        thread.daemon = True
        thread.start()
        
        while True:
            message = input("Enter message (or 'quit' to exit): ")
            if message.lower() == 'quit':
                break
            dest_host = input("Enter destination host: ")
            dest_port = int(input("Enter destination port: "))
            s.sendto(message.encode(), (dest_host, dest_port))

if __name__ == "__main__":
    start_chat()