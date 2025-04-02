import psutil

def get_memory_usage():
    """Ermittelt die aktuelle RAM-Auslastung in Prozent."""
    return psutil.virtual_memory().percent

def get_disk_usage():
    """Ermittelt die aktuelle Festplattenauslastung in Prozent."""
    return psutil.disk_usage('/').percent

def get_process_count():
    """Zählt die aktuell laufenden Prozesse."""
    return len(psutil.pids())
