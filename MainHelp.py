import subprocess, sys

def menu():
    print("\nSystem Monitoring")
    print("1 - CPU | 2 - RAM | 3 - Festplatte | all - Alle | C - Beenden")

def run(choice):
    if choice == 'all':
        choice = '123'
    if not all(c in '123' for c in choice):
        print("Ungültige Eingabe!")
        return

    tags = {'1': 'CPU:', '2': 'RAM:', '3': 'Festplatte:'}
    # Erzeuge einen Filter-String wie "CPU:|RAM:"
    filters = [tags[c] for c in choice]
    pattern = "|".join(filters)

    if sys.platform == 'win32':
        # Windows: findstr akzeptiert mehrere Begriffe mit /C: pro Begriff
        findstr_args = []
        for f in filters:
            findstr_args += ["/C:" + f]
        proc = subprocess.Popen([sys.executable, "main.py"], stdout=subprocess.PIPE)
        proc.wait()  # Warten auf den Abschluss von main.py
        result = subprocess.run(["findstr"] + findstr_args, stdin=proc.stdout)
        proc.stdout.close()
    else:
        # Unix/macOS: grep -E "CPU:|RAM:"
        cmd = f'{sys.executable} main.py | grep -E "{pattern}"'
        result = subprocess.run(cmd, shell=True)

    if result.returncode != 0:
        print("Keine passenden Werte gefunden.")

while True:
    menu()
    inp = input("Ihre Auswahl: ").strip().lower()
    if inp == 'c':
        break
    run(inp)
    print("\n" + "=" * 30)
