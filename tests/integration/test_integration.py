import unittest
from unittest.mock import patch
from monitoring.alert import check_threshold

class TestIntegration(unittest.TestCase):
    @patch('monitoring.alert.send_alert')
    def test_full_alert_workflow(self, mock_send):
        # Test mit disk usage 65% (> soft limit 61%)
        check_threshold(65, "Festplatte")
        mock_send.assert_called_once_with(
            "Warnung: Festplatte >61%",
            "⚠ WARNUNG! Festplatte >61% (Aktuell: 65%)"
        )
        
        # Reset mock
        mock_send.reset_mock()
        
        # Test mit disk usage 85% (> hard limit 80%)
        check_threshold(85, "Festplatte")
        mock_send.assert_called_once_with(
            "ALARM: Festplatte >80%",
            "🚨 KRITISCH! Festplatte >80% (Aktuell: 85%)"
        )