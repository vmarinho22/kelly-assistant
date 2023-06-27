from unittest import mock
from unittest.mock import MagicMock
import pytest
from src.modules.Command import Command

command = Command()

def test_smoke():
    assert isinstance(command, Command)


def test_find_command():
    assert command.find_command(['horas']) == 'hora'
    assert command.find_command(['dia']) == 'data'
    assert command.find_command(['clima']) == 'temperatura'
    assert command.find_command(['test']) == ''

def test_try_find_command_by_synonyms(mocker):
    mocker.patch('src.modules.NaturalLanguageProcessing.get_synonyms', MagicMock(return_value=['hora']))

    assert command.try_find_command_by_synonyms(['horas']) == 'hora'
