import psutil
import os

def get_memory_usage():
    """Ermittelt den Speicherverbrauch des Systems"""
    memory = psutil.virtual_memory()
    return memory.percent

def get_disk_usage():
    """Ermittelt den Plattenverbrauch des Systems"""
    disk = psutil.disk_usage('/')
    return disk.percent

def get_process_count():
    """Ermittelt die Anzahl der laufenden Prozesse"""
    return len(psutil.pids())
