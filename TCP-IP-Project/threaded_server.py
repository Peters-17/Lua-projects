import socket
import threading

SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

def handle_client(client_socket, address):
    print(f"Connection established with {address}")
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            print(f"Received from {address}: {message.decode('utf-8')}")
            client_socket.send("Message received".encode('utf-8'))
        except Exception as e:
            print(f"Error handling client {address}: {e}")
            break
    client_socket.close()
    print(f"Connection closed with {address}")

def server_listen():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((SERVER_IP, SERVER_PORT))
    server.listen()
    print(f"Server listening on {SERVER_IP}:{SERVER_PORT}")

    while True:
        client_socket, address = server.accept()
        client_handler = threading.Thread(
            target=handle_client,
            args=(client_socket, address)
        )
        client_handler.start()

if __name__ == "__main__":
    server_listen()
