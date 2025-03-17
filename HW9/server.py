import socket
import sys

def handle_client(conn, addr):
    """Handles client connection and sends the requested file."""
    print(f"Connected by {addr}") 

    while True: 
        data = conn.recv(1024).decode()  # Receive data from client
        if not data:
            break  # Exit if no data received
        
        filename = data.strip()  # Remove trailing spaces/newlines
        response = "Connection Successful!\n---------------HTTP RESPONSE---------------\n"

        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()  # Read file
                response += "HTTP/1.1 200 OK\n" + content
        except FileNotFoundError:
            response += "HTTP/1.1 404 Not Found\n"

        response += "\n---------------END OF HTTP RESPONSE---------------\n"
        conn.sendall(response.encode())  # Send response back to client

    conn.close()  # Close connection

def server(PORT):
    HOST = socket.gethostbyname(socket.gethostname())  # Get local machine IP
    print('Server running on', HOST, 'port', PORT)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()  # Start listening for connections

        while True:
            conn, addr = s.accept()  # Accept client connection
            handle_client(conn, addr)  # Handle client request

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python server.py <PORT>")
        sys.exit(1)

    PORT = int(sys.argv[1])
    server(PORT)