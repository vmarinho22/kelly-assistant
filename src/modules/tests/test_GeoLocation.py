from unittest.mock import MagicMock
import pytest
from src.modules.GeoLocation import GeoLocation

geo = GeoLocation()

class MockRequest:
    def __init__(self):
        self.text = ''

class MockGeoCoder:
    def __init__(self):
        self.latlng = [0, 0]

def test_getIp (mocker):
    mock_class_request = MagicMock(spec=MockRequest())
    mock_class_request.text = '192.168.0.1'

    mocker.patch('requests.get', MagicMock(return_value=mock_class_request))

    assert geo.getIp() == '192.168.0.1'

def test_getGeoPosition(mocker):
    mock_class_request = MagicMock(spec=MockRequest())
    mock_class_request.text = '192.168.0.1'

    mock_class_geocoder = MagicMock(spec=MockGeoCoder())
    mock_class_geocoder.latlng = [0, 0]

    mocker.patch('requests.get', MagicMock(return_value=mock_class_request))
    mocker.patch('geocoder.ip', MagicMock(return_value=mock_class_geocoder))

    assert geo.getGeoPosition() == [0, 0]
