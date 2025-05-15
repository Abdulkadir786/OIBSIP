import socket
import threading

# Server Configuration
HOST = '127.0.0.1'  # localhost
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(2)

clients = []

def handle_client(client):
    while True:
        try:
            message = client.recv(1024).decode()
            broadcast(message, client)
        except:
            clients.remove(client)
            client.close()
            break

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            try:
                client.send(message.encode())
            except:
                client.close()
                clients.remove(client)

print("Server started. Waiting for clients to connect...")
while True:
    client_socket, addr = server.accept()
    print(f"Connected by {addr}")
    clients.append(client_socket)
    thread = threading.Thread(target=handle_client, args=(client_socket,))
    thread.start()
