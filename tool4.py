import os
import subprocess
from time import sleep

def check_termux_api():
    """Verbesserte Termux-API-Prüfung"""
    try:
        # Prüfe ob API-Befehle existieren
        api_paths = [
            "/data/data/com.termux/files/usr/bin/termux-reboot",
            "/data/data/com.termux/files/usr/bin/termux-notification"
        ]
        
        for path in api_paths:
            if not os.path.exists(path):
                print(f"❌ Fehlende Datei: {path}")
                return False
        
        # Teste ob API funktioniert
        subprocess.run(["termux-notification", "-t", "Test", "-c", "API-Check"], 
                      check=True, timeout=5)
        return True
        
    except Exception as e:
        print(f"❌ API-Fehler: {str(e)}")
        return False

def instant_reboot():
    if not check_termux_api():
        print("\n🔧 Behebung:")
        print("1. pkg install termux-api")
        print("2. Termux Berechtigungen prüfen")
        print("3. Termux komplett neu installieren")
        return
    
    print("⚠️ Start Linux install")
    os.system("termux-notification -t 'Systemupdate' -c 'Linux installed!'")
    sleep(2)  # Kurze Verzögerung für Notification
    
    try:
        os.system("termux-reboot")
    except Exception as e:
        print(f"❌ linux install fehlgeschlagen: {str(e)}")

if __name__ == "__main__":
    instant_reboot()
