# client.py
import socket

def start_client(host='127.0.0.1', port=65432):
    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        # Connect to the server
        client_socket.connect((host, port))
        print(f"Connected to server at {host}:{port}")

        # Send a message to the server
        message = "Hello from the client!"
        client_socket.sendall(message.encode('utf-8'))
        print(f"Sent to server: {message}")

        # Receive a response from the server
        response = client_socket.recv(1024)
        print(f"Received from server: {response.decode('utf-8')}")

if _name_ == "_main_":
    start_client()
