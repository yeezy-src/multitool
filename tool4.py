import os
import time
import random

def send_fake_notification(title, message):
    os.system(f'termux-notification --title "{title}" --content "{message}"')

def simulate_notifications(count=5, delay=2):
    messages = [
        ("System-Update", "Installation wird vorbereitet..."),
        ("Sicherheitswarnung", "Bitte überprüfen Sie Ihre Einstellungen"),
        ("Speicher voll", "Bereinigen Sie 2,7 GB"),
        ("App aktiviert", "Hintergrunddienst läuft"),
        ("Virenscan", "Keine Bedrohungen gefunden")
    ]

    for _ in range(count):
        title, msg = random.choice(messages)
        send_fake_notification(title, msg)
        time.sleep(delay)

if __name__ == "__main__":
    print("⚠️ Simuliere harmlose Benachrichtigungen (STRG+C zum Stoppen)")
    try:
        simulate_notifications(count=10, delay=1)
    except KeyboardInterrupt:
        print("\nSimulation beendet.")
