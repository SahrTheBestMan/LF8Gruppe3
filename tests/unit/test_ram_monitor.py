import unittest
from monitoring.ram_monitor import get_memory_usage, get_disk_usage

class TestRamMonitor(unittest.TestCase):
    def test_memory_usage_range(self):
        usage = get_memory_usage()
        self.assertIsInstance(usage, float)
        self.assertTrue(0 <= usage <= 100)

    def test_disk_usage_exists(self):
        self.assertTrue(get_disk_usage() > 0)