from monitoring.ram_code import get_memory_usage, get_disk_usage, get_process_count
from alarm.alarm_system import check_limit

def main():
    # Festlegen der Grenzwerte
    soft_limit = 80
    hard_limit = 90

    # Systemdaten sammeln
    memory_usage = get_memory_usage()
    disk_usage = get_disk_usage()
    process_count = get_process_count()

    # Überprüfen, ob Grenzwerte überschritten wurden
    check_limit(memory_usage, soft_limit, hard_limit, "Memory Usage")
    check_limit(disk_usage, soft_limit, hard_limit, "Disk Usage")
    check_limit(process_count, soft_limit, hard_limit, "Process Count")

if __name__ == "__main__":
    main()
