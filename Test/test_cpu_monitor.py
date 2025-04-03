import unittest
from monitoring.cpu_monitor import (
    get_cpu_usage,
    get_cpu_cores,
    get_cpu_threads
)

class TestCpuMonitoring(unittest.TestCase):
    def test_cpu_usage(self):
        usage = get_cpu_usage()
        self.assertIsInstance(usage, float)
        self.assertTrue(0 <= usage <= 100)

    def test_cpu_cores(self):
        cores = get_cpu_cores()
        self.assertIsInstance(cores, int)
        self.assertGreater(cores, 0)

    def test_cpu_threads(self):
        threads = get_cpu_threads()
        self.assertIsInstance(threads, int)
        self.assertGreaterEqual(threads, get_cpu_cores())

if __name__ == "__main__":
    unittest.main()