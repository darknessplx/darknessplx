import subprocess

# Polecenie stress-ng w jednej linii
cmd = [
    "stress-ng",
    "--cpu", "2",
    "--cpu-method", "all",
    "--vm", "2",
    "--vm-bytes", "2G",
    "--hdd", "2",
    "--hdd-bytes", "25G",  # UWAGA: więcej niż wolne miejsce, może zablokować system
    "--io", "2",
    "--timeout", "10m",
    "--metrics-brief"
]

# Wyświetlamy, co zostanie uruchomione
print("Uruchamiam stress-ng z parametrami:")
print(" ".join(cmd))

# Uruchamiamy test
try:
    subprocess.run(cmd, check=True)
except KeyboardInterrupt:
    print("\nTest przerwany przez użytkownika")
except Exception as e:
    print(f"Wystąpił błąd: {e}")
