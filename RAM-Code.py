import psutil
import logging

# Logging einrichten
logging.basicConfig(filename="monitoring.log", level=logging.INFO, format="%(asctime)s - %(message)s")

def check_memory_usage():
    """Überprüft den RAM-Verbrauch und speichert ihn in einer Logdatei."""
    memory = psutil.virtual_memory()
    used_percent = memory.percent
    log_message = f"Arbeitsspeicher: {used_percent}% genutzt"
    logging.info(log_message)
    print(log_message)

if __name__ == "__main__":
    check_memory_usage()
