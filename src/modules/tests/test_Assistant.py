import pytest
from src.modules.Assistant import Assistant
from unittest.mock import MagicMock

class FrameData:
    def init(self):
        self.frame_data = ""

def test_smoke():
    assistant = Assistant()
    assert isinstance(assistant, Assistant)

def test_listen_method(mocker):
    assistant = Assistant()

    mock_frame_data = MagicMock(spec=FrameData())
    mock_frame_data.frame_data = b'frame_data'

    mock_listen_method = MagicMock(return_value=mock_frame_data)
    mock_transpile_audio_method = MagicMock(return_value='texto de retorno')

    mocker.patch('src.modules.SpeechRecognition.listen', mock_listen_method)
    mocker.patch('src.modules.SpeechRecognition.transpile_audio', \
                 mock_transpile_audio_method)
    
    assert assistant.listen('log_message') == 'texto de retorno'