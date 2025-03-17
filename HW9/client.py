import socket
import sys 

def send_request(host, port, filename):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((host, port))  # Connect to server
        except ConnectionRefusedError:
            print("Connection refused. Make sure the server is running.")
            sys.exit(1)
        
        s.sendall(filename.encode())  # Send filename to server
        data = s.recv(4096)  # Increased buffer size for larger responses
        print(data.decode())  # Print server response

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python client.py <HOST> <PORT> <FILENAME>")
        sys.exit(1)

    try:
        HOST = sys.argv[1]
        PORT = int(sys.argv[2])
        FILENAME = sys.argv[3]
        send_request(HOST, PORT, FILENAME)  
    except ValueError:
        print("Invalid port number")