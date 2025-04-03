# tests/conftest.py
import pytest
from unittest.mock import patch

@pytest.fixture(autouse=True)
def mock_config():
    with patch('configparser.ConfigParser') as mock:
        instance = mock.return_value
        instance.read.return_value = {
            'thresholds': {
                'disk_soft': '61',
                'disk_hard': '80'
            },
            'email': {
                'sender': 'test@test.com',
                'receiver': 'receiver@test.com',
                'password': 'mock'
            }
        }
        yield instance