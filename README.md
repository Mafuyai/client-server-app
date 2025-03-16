# Simple Client-Server Application

This project demonstrates a basic client-server setup where the server listens for client requests and responds with a message. It's a simulation of a distributed system using Python's socket library.

---

## Features
- A server that listens for incoming connections.
- A client that sends a request to the server.
- The server responds with a predefined message.
- Simple simulation of a distributed system.

---

## Prerequisites
- Python 3.x installed on your system.
- Basic understanding of Python and networking concepts.

---

## Setup Instructions

1. Clone this repository or create the following files in your project directory:
   - `server.py`
   - `client.py`

2. Install dependencies (if needed).

---

### Server Setup
1. Open `server.py` and insert the following code:

    ```python
    import socket

    def start_server():
        host = '127.0.0.1'  # Localhost
        port = 12345         # Port number

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((host, port))
            server_socket.listen(5)
            print(f"Server listening on {host}:{port}")

            while True:
                client_socket, address = server_socket.accept()
                print(f"Connection from {address}")
                message = "Hello from the server!".encode('utf-8')
                client_socket.send(message)
                client_socket.close()

    if __name__ == "__main__":
        start_server()
    ```

2. Run `server.py`:
   ```bash
   python server.py# client-server-app
