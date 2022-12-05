#!/usr/bin/env python27
# Run the script with Python 2.7
# example:   C:\Python27\python.exe client.py

import socket
import sys
from pepper_robots import PepperConfiguration, Robot, PepperNames
from take_picture import pepper_spies

config = PepperConfiguration(PepperNames.Ale)
pepper = Robot(config)

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 54321        # The port used by the server

print("starting python client with python version:")
print(sys.version)

tts = pepper.ALTextToSpeech
tts.setLanguage("English")
tts.setVolume(0.6)
tts.say("Let's play a game of I spy with my little eye")

tts.say("I'l start")
pepper_spies(pepper)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(b'Picture taken')
data = s.recv(1024)

print('Received', repr(data))
