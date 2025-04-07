import psutil

def get_memory_usage():
    return psutil.virtual_memory().percent

def get_disk_usage():
    return psutil.disk_usage('/').percent

def get_process_count():
    return len(psutil.pids())

if __name__ == "__main__":
    print(f"RAM: {get_memory_usage()}%")
    print(f"Festplatte: {get_disk_usage()}%")
    print(f"Prozesse: {get_process_count()}")