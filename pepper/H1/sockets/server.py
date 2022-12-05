#!/usr/bin/env python3
# Run the script with Python 3.x
# example:   python.exe server.py
import socket
import sys

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 54321        # Port to listen on (non-privileged ports are > 1023)

print("starting python server with python version:")
print(sys.version)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
