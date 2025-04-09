import subprocess
import sys

def menu():
    print("\nSystem Monitoring\n1 - CPU | 2 - RAM | 3 - Festplatte | all - Alle | C - Beenden")

def run(choice):
    mapping = {'1': 'CPU:', '2': 'RAM:', '3': 'Festplatte:'}
    if choice == 'all':
        filters = list(mapping.values())
    elif all(c in mapping for c in choice):
        filters = [mapping[c] for c in choice]
    else:
        print("Ungültige Eingabe!")
        return

    cmd = [sys.executable, "main.py"]
    if sys.platform == 'win32':
        with subprocess.Popen(cmd, stdout=subprocess.PIPE, text=True) as proc:
            for line in proc.stdout:
                if any(f in line for f in filters):
                    print(line.strip())
    else:
        grep_cmd = ["grep", "-E", "|".join(filters)]
        p1 = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        p2 = subprocess.Popen(grep_cmd, stdin=p1.stdout, stdout=subprocess.PIPE, text=True)
        p1.stdout.close()
        for line in p2.stdout:
            print(line.strip())

while True:
    menu()
    inp = input("Ihre Auswahl: ").strip().lower()
    if inp == 'c':
        break
    run(inp)
    print("\n" + "=" * 30)
