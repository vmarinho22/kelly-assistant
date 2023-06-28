import pytest
from src.modules.AudioSystem import AudioSystem
from unittest.mock import MagicMock

audio_system = AudioSystem()

class GTTsMock:
    def init(self):
        pass
    
    def save(self, file_name):
        return None

def test_smoke():
    assert isinstance(audio_system, AudioSystem)

def test_create_audio_by_text_method(mocker):
    mock_class = MagicMock(spec=GTTsMock())
    mock_gtts_class = MagicMock(return_value=mock_class)

    mocker.patch('gtts.gTTS', mock_gtts_class)

    assert audio_system.create_audio_by_text('test', 'test') is None

def test_play_audio(mocker):
    mocker.patch('playsound.playsound', MagicMock(return_value=None))

    assert audio_system.play_audio('test') is None

def delete_audio(mocker):
    mocker.patch('os.remove', MagicMock(return_value=None))

    assert audio_system.delete_audio('test') is None