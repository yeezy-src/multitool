import os
import time
from datetime import datetime

def check_termux_api():
    """Prüft ob Termux-API installiert ist"""
    if not os.path.exists("/data/data/com.termux/files/usr/bin/termux-torch"):
        print("❌ Termux-API nicht installiert!")
        print("Installiere zuerst: pkg install termux-api")
        exit()

def torch_blink(duration=10, interval=0.5):
    """Blinkt mit der Taschenlampe"""
    check_termux_api()
    
    print(f"🔦 Blinkmodus aktiviert (Dauer: {duration}s, Intervall: {interval}s)")
    print("Drücke STRG+C zum Beenden\n")
    
    end_time = time.time() + duration
    try:
        while time.time() < end_time:
            os.system("termux-torch on")
            time.sleep(interval)
            os.system("termux-torch off")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nBlinken gestoppt")
    finally:
        os.system("termux-torch off")

if __name__ == "__main__":
    torch_blink(duration=60, interval=0.5)  # 1 Minute blinken
