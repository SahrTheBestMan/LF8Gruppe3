import unittest
from unittest.mock import patch, MagicMock
from monitoring.alert import check_threshold

class TestAlert(unittest.TestCase):
    @patch('monitoring.alert.send_alert')
    @patch('monitoring.alert.logging')
    def test_thresholds(self, mock_logging, mock_send):
        # Test soft limit (65 > 61)
        check_threshold(65, "Festplatte")
        mock_send.assert_called_once_with(
            "Warnung: Festplatte >61%",
            "⚠ WARNUNG! Festplatte >61% (Aktuell: 65%)"
        )
        
        # Reset mock für hard limit Test
        mock_send.reset_mock()
        
        # Test hard limit (85 > 80)
        check_threshold(85, "Festplatte")
        mock_send.assert_called_once_with(
            "ALARM: Festplatte >80%",
            "🚨 KRITISCH! Festplatte >80% (Aktuell: 85%)"
        )