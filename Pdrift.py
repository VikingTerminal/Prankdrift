import time

fake_devices = ['iPhone di Marco Santini', 'Galaxy di Lauretta', 'iPad di Gianni', 'Laptop di Sofia', 'Telefono di Andrew']
fake_traffic = ['Richiesta di accesso a Facebook', 'Videochiamata su WhatsApp', 'Accesso al sito della banca', 'Streaming su Netflix', 'Navigazione su Instagram']

def print_colored(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

def print_progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█', print_end='\r'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=print_end)
    if iteration == total:
        print()

def save_logs(logs):
    with open("driftnet_logs.txt", "a") as log_file:
        log_file.write("\n".join(logs) + "\n")

def load_logs():
    try:
        with open("driftnet_logs.txt", "r") as log_file:
            return log_file.readlines()
    except FileNotFoundError:
        return []

print_colored("⚠️Inizializzazione dello sniffing ", "1;32")

time.sleep(2)
print_colored("📲Connessione alla rete eroporto di Roma Fiumicino - Leonardo da Vinci...", "1;31")
time.sleep(2)
print_colored("Caricamento dei moduli di intercettazione...", "1;36")
time.sleep(2)

print("\nIn cerca di dispositivi connessi...")

logs = []
for i, device in enumerate(fake_devices, 1):
    logs.append(f"Dispositivo rilevato: {device}")
    print_progress_bar(i, len(fake_devices), prefix=f"Dispositivo rilevato: {device}", length=30)
    time.sleep(1)

save_logs(logs)

print_colored("\nAnalisi del traffico in corso...", "1;36")
time.sleep(3)

traffic_logs = []
for i, traffic in enumerate(fake_traffic, 1):
    traffic_logs.append(f"Traffico rilevato: {traffic}")
    print_progress_bar(i, len(fake_traffic), prefix=f"Traffico rilevato: {traffic}", length=30)
    time.sleep(2)

save_logs(traffic_logs)

print_colored("\n⚠️processo completato con successo. i pacchetti e file logs sono stati clonati e aggiunti nel tuo archivio\n ", "1;34")

user_input = input("\033[1;32mdrift =>\033[0m")

print("\n\n📠 Esecuzione attività post-intercettazione:")
time.sleep(1)
print_colored("Analisi approfondita dei dati intercettati...", "1;36")
time.sleep(2)
print_colored("Generazione di report dettagliati...", "1;36")
time.sleep(2)
print_colored("Invio dei report alle autorità competenti...", "1;36")
time.sleep(2)

print_colored("\n🔍 Attività post-intercettazione completata con successo! 🔍", "1;34")

previous_logs = load_logs()
if previous_logs:
    print("\n\nLogs precedenti:")
    for log in previous_logs:
        print(log.strip())
