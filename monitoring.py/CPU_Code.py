import psutil

def get_cpu_usage():
    """Ermittelt die aktuelle CPU-Auslastung in Prozent."""
    return psutil.cpu_percent(interval=1)
