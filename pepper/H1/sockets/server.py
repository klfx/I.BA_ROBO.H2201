#!/usr/bin/env python3
# Run the script with Python 3.x
# example:   python.exe server.py
import socket
import sys
import os
import sys

from ObjectRecognition import ObjectRecognition

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

        print('Creating ObjectRecognition Object')
        or1 = ObjectRecognition()
        data = or1.getTagsEncoded()
        while True:
            if not data:
                break
            conn.sendall(data)
