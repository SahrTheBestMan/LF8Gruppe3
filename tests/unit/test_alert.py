# tests/unit/test_alert.py

import monitoring.alert as alert
import logging
from unittest.mock import patch

def test_send_alert():
    with patch("monitoring.alert.smtplib.SMTP_SSL") as mock_smtp:
        alert.send_alert("Test Subject", "Test Message")
        instance = mock_smtp.return_value.__enter__.return_value
        instance.login.assert_called_once()
        instance.send_message.assert_called_once()

def test_check_threshold_warnung():
    with patch("monitoring.alert.send_alert") as mock_alert:
        alert.check_threshold(76, "RAM")  # Soft Limit überschritten
        mock_alert.assert_called_once()
        args = mock_alert.call_args[0]
        assert "Warnung" in args[0]

def test_check_threshold_kritisch():
    with patch("monitoring.alert.send_alert") as mock_alert:
        alert.check_threshold(91, "RAM")  # Hard Limit überschritten
        mock_alert.assert_called_once()
        args = mock_alert.call_args[0]
        assert "ALARM" in args[0]
