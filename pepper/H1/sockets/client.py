#!/usr/bin/env python27
# Run the script with Python 2.7
# example:   C:\Python27\python.exe client.py

import socket
import sys
import time
import random
from speech_recognition import SpeechRecognition

from pepper_robots import PepperConfiguration, Robot, PepperNames
from naoqi_python_wrapper.ALAutonomousLife import ALAutonomousLife
from take_picture import pepper_spies

config = PepperConfiguration(PepperNames.Ale)
pepper = Robot(config)

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 54321        # The port used by the server

print("starting python client with python version:")
print(sys.version)

tts = pepper.ALTextToSpeech
pepper.ALAutonomousLife.setState("solitary")
pepper.ALRobotPosture.goToPosture("StandZero", 1.0)
tts.setLanguage("English")
tts.setVolume(0.6)
#tts.say("Let's play a game of I spy with my little eye")

#tts.say("I'l start")
#pepper.ALMotion.moveTo(-0.5, 0, 0)
pepper_spies(pepper)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.sendall(b'Picture taken')
data = s.recv(1024)
print('original data:'+data)
#data = data.decode('utf-8')

data = data.strip('][').split(', ')

itemlist = []
for i in data:
    i = i.replace("'", "")
    #pepper.ALTextToSpeech.say(i)
    itemlist.append(i)

selecteditem = random.choice(itemlist)

#overwrite with mock data
itemlist = ['person', 'indoor', 'laptop', 'computer']
selecteditem = 'computer'

def speech_callback(value):
    #tts.say(selecteditem)
    print("recognized the following word:" + value[0] + " with accuracy: " + str(value[1]))
    if value[0] == "person":
        if value[1] > 0.35:
            print "received person"
    if value[0] == "indoor":
        if value[1] > 0.35:
            print "received indoor"

tts.say("Try to guess what i have spotted in the room")
print('calling SpeechRecognition with itemlist:'+str(itemlist))
sr = SpeechRecognition(pepper, itemlist, speech_callback)
time.sleep(100)
sr.unsubscribe()

