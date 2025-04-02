import unittest
from monitoring.ram_code import get_memory_usage, get_disk_usage, get_process_count

class TestSystemMonitoring(unittest.TestCase):
    
    def test_get_memory_usage(self):
        result = get_memory_usage()
        self.assertTrue(0 <= result <= 100, f"Speicherverbrauch sollte zwischen 0 und 100% liegen, aber es ist {result}%")
    
    def test_get_disk_usage(self):
        result = get_disk_usage()
        self.assertTrue(0 <= result <= 100, f"Plattenverbrauch sollte zwischen 0 und 100% liegen, aber es ist {result}%")
    
    def test_get_process_count(self):
        result = get_process_count()
        self.assertGreater(result, 0, "Es gibt keine laufenden Prozesse.")

if __name__ == "__main__":
    unittest.main()