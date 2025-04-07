# tests/integration/test_full_flow.py
# tests/integration/test_full_flow.py
from unittest.mock import patch
from monitoring import alert

def test_full_alert_flow():
    with patch("monitoring.alert.send_alert") as mock_alert:
        alert.check_threshold(96, "CPU")
        mock_alert.assert_called_once()
