class SpeechRecognition(object):

    def __init__(self, robot, vocabulary, selecteditem, callback):

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


    def unsubscribe(self):
        self.__speech_recognition.unsubscribe("SpeechDetection")
        print('Speech recognition engine stopped')


