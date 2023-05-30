import socket
import os

IP = '172.16.173.106'
#P = socket.gethostbyname(socket.gethostname())
PORT = 8000
ADDR = (IP, PORT)
#FORMAT = "utf-8"
SIZE = 1024
 
def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    path=input("Enter the path to be sent: ")
    file = open(path, "r")
    data = file.read()
    
    filename = os.path.basename(path)
    client.send(filename.encode())
    msg = client.recv(SIZE).decode()
    print(f"[SERVER]: {msg}")

    client.send(data.encode())
    msg = client.recv(SIZE).decode()
    print(f"[SERVER]: {msg}")
 
    file.close()
 
    client.close()
 
 
if __name__ == "__main__":
    main()
