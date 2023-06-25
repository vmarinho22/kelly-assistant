import os

from gtts import gTTS
from playsound import playsound


class AudioSystem:
    """
        Dedicated class to use audio methods
    """
    
    def create_audio_by_text(self, text: str, file_name: str):
        """
            Method to transform text into audio
        """
        audio = gTTS(text=text, lang="pt-BR", slow=False)
        audio.save(f"sounds/{file_name}.mp3")
        
    def play_audio(self, file_name: str, blocked: bool = True):
        """
            Method to play sound by file name
        """
        playsound(f'sounds/{file_name}.mp3', blocked)
        
    def delete_audio(self, file_name: str) -> None:
        os.remove(f'sounds/{file_name}.mp3')