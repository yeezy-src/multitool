import os
import sys

def check_termux_api():
    """Prüft Termux-API Installation"""
    if not os.path.exists("/data/data/com.termux/files/usr/bin/termux-reboot"):
        print("Termux-API nicht installiert! Bitte zuerst installieren:")
        print("pkg install termux-api")
        sys.exit(1)

def instant_reboot():
    check_termux_api()
    print("⚠️ Gerät wird sofort neugestartet!")
    os.system("termux-notification -t 'Neustart gestartet' -c 'Device rebootet jetzt'")
    os.system("termux-reboot")  # Sofortiger Neustart

if __name__ == "__main__":
    instant_reboot()
