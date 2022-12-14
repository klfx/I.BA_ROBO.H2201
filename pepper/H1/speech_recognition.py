import re
import time
from pepper_robots import PepperConfiguration, PepperNames, Robot


class SpeechRecognition(object):

    def __init__(self, robot, vocabulary, callback):

        memory = robot.session.service("ALMemory")
        self.subscriber = memory.subscriber("WordRecognized")
        self.subscriber.signal.connect(callback)
        self.__speech_recognition = robot.session.service("ALSpeechRecognition")
        self.__speech_recognition.pause(True)  # need to pause speech recognition to set parameters
        self.__speech_recognition.setLanguage("English")
        self.__speech_recognition.setVocabulary(vocabulary, False)
        self.__speech_recognition.pause(False)
        self.__speech_recognition.subscribe("SpeechDetection")
        print('Speech recognition engine started')

    def subscribe(self):
        self.__speech_recognition.subscribe("SpeechDetection")
        print('Speech recognition engine started')

    def unsubscribe(self):
        self.__speech_recognition.unsubscribe("SpeechDetection")
        print('Speech recognition engine stopped')

    def pause(self):
        self.__speech_recognition.pause(True)

    def unpause(self):
        self.__speech_recognition.pause(False)

    def getMemory(self):
        return self.memory


if __name__ == "__main__":

    running = True
    vocab = ['pineapple','banana','stawberry','peach','grape']
    target = 'pineapple'
    threshold = 0.35
    print("Start SpeechRecognition Demo")

    config = PepperConfiguration(PepperNames.Amber)
    pepper = Robot(config)

    def regex(val):
        words_pattern = '([a-zA-Z]+)'
        reg_word = re.findall(words_pattern, val, flags=re.IGNORECASE)
        return reg_word

    def speech_callback(value):
        global running
        print("recognized the following word:" + value[0] + " with accuracy: " + str(value[1]))

        if value[0] == target:
            if value[1] > threshold:
                print("Good guess!")
                running = False

        else:
            print("Wrong guess. Try again")

    while running:
        print(running)
        sr = SpeechRecognition(pepper,vocab,speech_callback)
        time.sleep(5)
        #print('SpeechRegonition Memory: ', sr.getMemory())
        sr.unsubscribe()
