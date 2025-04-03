import psutil

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_cpu_cores():
    return psutil.cpu_count(logical=False)

def get_cpu_threads():
    return psutil.cpu_count(logical=True)

if __name__ == "__main__":
    print(f"CPU: {get_cpu_usage()}%")
    print(f"Kerne: {get_cpu_cores()}")
    print(f"Threads: {get_cpu_threads()}")