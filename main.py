from monitoring.ram_monitor import get_memory_usage, get_disk_usage
from monitoring.cpu_monitor import get_cpu_usage
from monitoring.alert import check_threshold
from datetime import datetime

LOG_FILE = "requirements.txt"  # Speichert die Werte in requiremnts

def save_results(cpu, ram, disk):
    """Speichert die aktuellen Werte mit Datum in requirements.txt"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as file:  # "a" = an Datei anhängen
        file.write(f"{timestamp} | CPU: {cpu:.1f}% | RAM: {ram:.1f}% | Festplatte: {disk:.1f}%\n")

def main():
    print("System Monitoring gestartet...")
    
    # Werte abfragen
    cpu = get_cpu_usage()
    ram = get_memory_usage()
    disk = get_disk_usage()
    
    # Ausgabe
    print(f"\nAktuelle Werte:")
    print(f"CPU: {cpu:.2f}%")
    print(f"RAM: {ram:.2f}%")
    print(f"Festplatte: {disk:.2f}%")

    # Werte speichern
    save_results(cpu, ram, disk)
    
    # Grenzwerte prüfen
    check_threshold(cpu, "CPU")
    check_threshold(ram, "RAM")
    check_threshold(disk, "Festplatte")

if __name__ == "__main__":
    main()

print("Für weitere Hilfe bitte 'python mainHelp.py' eingeben.")