import speech_recognition as sr
from src.clear import *

class SpeechRecognition:
    device_index=15
    microphone = sr.Recognizer()

    def deviceChannelIndex(self, value):
        self.device_index = value

    def listenMicrophone(self):
        with sr.Microphone(device_index=self.device_index) as source:
            self.microphone.adjust_for_ambient_noise(source)
            print("Ouvindo...")
            audio = self.microphone.listen(source)
            return audio

    def recognizeSpeech(self, audio):
        try:
            text = self.microphone.recognize_google(audio, language='pt-BR')
            return text;
        except sr.UnknownValueError:
            return ''