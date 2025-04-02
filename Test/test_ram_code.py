import unittest
from monitoring.ram_code import get_memory_usage, get_disk_usage, get_process_count

class TestMonitoring(unittest.TestCase):

    def test_get_memory_usage(self):
        ram_usage = get_memory_usage()
        self.assertIsInstance(ram_usage, float)
        self.assertGreaterEqual(ram_usage, 0)
        self.assertLessEqual(ram_usage, 100)

    def test_get_disk_usage(self):
        disk_usage = get_disk_usage()
        self.assertIsInstance(disk_usage, float)
        self.assertGreaterEqual(disk_usage, 0)
        self.assertLessEqual(disk_usage, 100)

    def test_get_process_count(self):
        process_count = get_process_count()
        self.assertIsInstance(process_count, int)
        self.assertGreater(process_count, 0)

if __name__ == "__main__":
    unittest.main()
