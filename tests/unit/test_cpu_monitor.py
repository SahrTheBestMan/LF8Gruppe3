from monitoring import cpu_monitor

def test_get_cpu_usage():
    usage = cpu_monitor.get_cpu_usage()
    assert isinstance(usage, float)
    assert 0 <= usage <= 100
