import pytest
import psutil
from RAM_Code import check_memory_usage

# Mock für psutil.virtual_memory()
class MockMemory:
    def __init__(self, percent):
        self.percent = percent

def test_check_memory_usage_softlimit_warning():
    # Simuliere 85% RAM-Nutzung (über Softlimit)
    psutil.virtual_memory = lambda: MockMemory(85)
    check_memory_usage(soft_limit=80, hard_limit=90)
    # Hier solltest du prüfen, ob eine Warnung in der Logdatei erstellt wurde.

def test_check_memory_usage_hardlimit_alarm():
    # Simuliere 95% RAM-Nutzung (über Hardlimit)
    psutil.virtual_memory = lambda: MockMemory(95)
    check_memory_usage(soft_limit=80, hard_limit=90)
    # Hier solltest du prüfen, ob eine E-Mail gesendet wurde.
