from monitoring.ram_code import get_memory_usage, get_disk_usage, get_process_count
from monitoring.alarm import check_limit

def main():
    ram_usage = get_memory_usage()
    disk_usage = get_disk_usage()
    process_count = get_process_count()

    print(f"RAM Nutzung: {ram_usage}%")
    print(f"Festplattennutzung: {disk_usage}%")
    print(f"Anzahl der Prozesse: {process_count}")

    # Grenzwerte setzen (Soft Limit: 70%, Hard Limit: 90%)
    check_limit(ram_usage, 70, 90, "RAM")
    check_limit(disk_usage, 80, 95, "Festplatte")

if __name__ == "__main__":
    main()
