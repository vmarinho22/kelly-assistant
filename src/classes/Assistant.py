from .AudioSystem import AudioSystem
from .SpeechRecognition import SpeechRecognition


class Assistant:
    
    """
        Dedicated class to centralize assistant methods
    """
    
    speech_recognition = SpeechRecognition()
    audio_system = AudioSystem()
    
    # CONSTANTS
    shutdown_command = 'desligar assistente'
    
    def listen(self, log_message: str) -> str:
        """
            Method to capture audio from microphone and transpile to text
        """
        
        audio_data = self.speech_recognition.listen(log_message)
        audio_transpiled = self.speech_recognition.transpile_audio(audio_data)
        
        return audio_transpiled
    
    def speak(self, fileName: str, text: str = None) -> None:
        if text:
            self.audio_system.create_audio_by_text(fileName, text)
        self.audio_system.play_audio(fileName)    
        
    def is_called(self, text: str) -> bool:
        return 'kelly' in text.lower()