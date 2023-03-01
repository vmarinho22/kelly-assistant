from gtts import gTTS
from playsound import playsound


class AudioSystem:
    """
        Dedicated class to use audio methods
    """
    
    def create_audio_by_text(self, text: str, fileName: str):
        """
            Method to transform text into audio
        """
        audio = gTTS(text=text, lang="pt-BR", slow=False)
        audio.save(f"sounds/{fileName}.mp3")
        
    def play_audio(self, fileName: str, blocked: bool = True):
        """
            Method to play sound by file name
        """
        playsound(f'sounds/{fileName}.mp3', blocked)