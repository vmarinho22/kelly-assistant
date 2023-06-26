import pytest
from src.utils.check_connection import online
from unittest.mock import MagicMock, patch

def test_online_case():
    mock_urlopen_method = MagicMock(return_value=True)
    
    with patch('urllib.request.urlopen', mock_urlopen_method):
        assert online() == True
        