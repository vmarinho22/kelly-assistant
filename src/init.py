
from src.classes.SpeechRecognition import SpeechRecognition

# Ubuntu Marinho = 12 14 *15*

def init():
    speechRecognition = SpeechRecognition()
    audio = speechRecognition.listenMicrophone()
    print('Audio gravado')
    audioInText = speechRecognition.recognizeSpeech(audio);

    if(audioInText != ""):
        print("Você falou: " + audioInText)
    else:
        print("----Não entendi----")