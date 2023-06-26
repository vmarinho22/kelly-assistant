import pytest
from src.modules.Assistant import Assistant
from unittest.mock import MagicMock

assistant = Assistant()

class FrameData:
    def init(self):
        self.frame_data = ""

def test_smoke():
    assert isinstance(assistant, Assistant)

def test_listen_method(mocker):

    mock_frame_data = MagicMock(spec=FrameData())
    mock_frame_data.frame_data = b'frame_data'

    mock_listen_method = MagicMock(return_value=mock_frame_data)
    mock_transpile_audio_method = MagicMock(return_value='texto de retorno')

    mocker.patch('src.modules.SpeechRecognition.listen', mock_listen_method)
    mocker.patch('src.modules.SpeechRecognition.transpile_audio', \
                 mock_transpile_audio_method)
    
    assert assistant.listen('log_message') == 'texto de retorno'

def test_listen_method_with_empty_returned_text(mocker):

    mock_frame_data = MagicMock(spec=FrameData())
    mock_frame_data.frame_data = b''

    mock_listen_method = MagicMock(return_value=mock_frame_data)
    mock_transpile_audio_method = MagicMock(return_value='')

    mocker.patch('src.modules.SpeechRecognition.listen', mock_listen_method)
    mocker.patch('src.modules.SpeechRecognition.transpile_audio', \
                 mock_transpile_audio_method)
    
    assert assistant.listen('log_message') == ''

def test_speak_method_with_no_text(mocker):

    mocker.patch('src.modules.AudioSystem.play_audio', MagicMock())

    assert assistant.speak('init') is None

def test_speak_method_with_custom_text(mocker):

    mock_create_audio_by_text_method = MagicMock(return_value='text')

    mocker.patch('src.modules.AudioSystem.create_audio_by_text', mock_create_audio_by_text_method)
    mocker.patch('src.modules.AudioSystem.play_audio', MagicMock())

    assert assistant.speak('init', 'test') is None

def test_is_called_method():
    assert assistant.is_called('kelly') is True
    assert assistant.is_called('') is False

def test_removeAssistantNameOfCommand():
    assert assistant.removeAssistantNameOfCommand('kelly test') == 'test'
    assert assistant.removeAssistantNameOfCommand('test') == 'test'
    assert assistant.removeAssistantNameOfCommand('kelly') == ''