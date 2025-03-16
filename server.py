# server.py
import socket

def start_server(host='127.0.0.1', port=65432):
    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Bind the socket to the address and port
        server_socket.bind((host, port))
        # Listen for incoming connections
        server_socket.listen()
        print(f"Server listening on {host}:{port}...")

        while True:
            # Accept a connection from a client
            client_socket, client_address = server_socket.accept()
            with client_socket:
                print(f"Connected to client at {client_address}")
                # Receive data from the client
                data = client_socket.recv(1024)
                print(f"Received from client: {data.decode('utf-8')}")
                # Send a response back to the client
                response = "Hello from the server!"
                client_socket.sendall(response.encode('utf-8'))
                print(f"Sent response to client: {response}")

if _name_ == "_main_":
    start_server()
