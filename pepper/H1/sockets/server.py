#!/usr/bin/env python3
# Run the script with Python 3.x
# example:   python.exe server.py
import socket
import sys
import os
import sys
import requests

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 54321        # Port to listen on (non-privileged ports are > 1023)

if 'COMPUTER_VISION_SUBSCRIPTION_KEY' in os.environ:
    subscription_key = os.environ['COMPUTER_VISION_SUBSCRIPTION_KEY']
else:
    print("\nSet the COMPUTER_VISION_SUBSCRIPTION_KEY environment variable.\n**Restart your shell or IDE for changes to take effect.**")
    sys.exit()

if 'COMPUTER_VISION_ENDPOINT' in os.environ:
    endpoint = os.environ['COMPUTER_VISION_ENDPOINT']

analyze_url = endpoint + "vision/v3.1/analyze"

image_path = "C:\work\latest.jpg"


print("starting python server with python version:")
print(sys.version)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)

        print('Starting Azure cognitive services image transmission')
        image_data = open(image_path, "rb").read()
        headers = {'Ocp-Apim-Subscription-Key': subscription_key,
                   'Content-Type': 'application/octet-stream'}
        params = {'visualFeatures': 'Categories,Description,Color'}
        response = requests.post(
            analyze_url, headers=headers, params=params, data=image_data)
        response.raise_for_status()

        analysis = response.json()
        data = analysis['description'].get('tags')
        data = str(data)
        data = data.encode()
        while True:
            #data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
