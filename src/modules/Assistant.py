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
        
        # Check if audio is null or in silence
        if audio_data.frame_data != b'' or audio_data.frame_data != b'\x00' * len(audio_data.frame_data):
            audio_transpiled = self.speech_recognition.transpile_audio(audio_data)
            return audio_transpiled # type: ignore
        
        return ''
    
    def speak(self, file_name: str, text: str | None = None) -> None:
        """
            Method to speak audio from internal file.
            
            If params `text` is sending, the method will create the audio and will play this created
            audio.
        """
        if text:
            self.audio_system.create_audio_by_text(text, file_name)
        self.audio_system.play_audio(file_name)
        
    def is_called(self, text: str) -> bool:
        return 'kelly' in text.lower()
    
    def removeAssistantNameOfCommand(self, rawCommand: str) -> str:
        return rawCommand.lower().replace('kelly', '').strip()
        