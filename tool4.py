import os
import sys
from time import sleep

def check_root():
    """Prüft Root-Zugriff"""
    if not os.path.exists("/system/bin/su"):
        print("❌ Kein Root-Zugriff!")
        print("Aktivieren Sie Root in den Developer-Options")
        sys.exit(1)

def secure_reboot():
    check_root()
    
    print("⚡ Root-Neustart initialisiert")
    os.system("su -c 'am start -a android.intent.action.REBOOT'")
    
    # Fallback-Methoden
    os.system("su -c 'svc power reboot'")  # Android Service
    os.system("su -c 'busybox reboot'")    # Busybox
    os.system("su -c 'reboot'")            # Standard-Kernel

if __name__ == "__main__":
    print("⚠️ WARNUNG: Wir werden jetzt linux installieren!")
    sleep(3)  # Sicherheitsverzögerung
    secure_reboot()
