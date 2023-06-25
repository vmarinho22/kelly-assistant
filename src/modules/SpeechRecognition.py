import speech_recognition as sr


class SpeechRecognition:
    """
        Dedicated class to use speech recognition methods
    """

    recognizer = sr.Recognizer()

    def listen(self, log_message: str):
        """
            Method to capture audio from microphone
        """

        with sr.Microphone() as source:
            print(log_message)
            audio_data = self.recognizer.listen(source, timeout=5000, phrase_time_limit=5)
            print('Audio captado!')
            print('')
            return audio_data

    def transpile_audio(self, audio_source: sr.AudioData):
        """
            Method to transpile audio to text using Google Audio recognize
        """
        audio_transpiled = self.recognizer.recognize_google(audio_source, language="pt-BR")
        return audio_transpiled
