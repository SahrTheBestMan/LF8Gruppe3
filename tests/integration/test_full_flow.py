def test_full_alert_flow():
    with patch('monitoring.alert.send_alert') as mock_alert:
        # Simuliere hohe CPU-Last
        with patch('monitoring.cpu_monitor.get_cpu_usage', return_value=90):
            main()  # Ihr Hauptprogramm
            mock_alert.assert_called_once()