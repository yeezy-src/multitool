import random
import sys
from colorama import Fore

def turbo_binary_rain():
    """Absolut schnellste Implementierung"""
    colors = [Fore.GREEN, Fore.LIGHTGREEN_EX]
    sys.stdout.write('\033[?25l')  # Cursor verstecken
    
    try:
        while True:
            # Mega-Block mit 5000 Zeichen
            bits = ''.join(random.choices('01', k=5000))
            # Sofortige Ausgabe
            sys.stdout.write(''.join(random.choice(colors) + b for b in bits))
            sys.stdout.flush()
            
    except KeyboardInterrupt:
        sys.stdout.write('\033[?25h')  # Cursor wieder anzeigen
        print("\n" + Fore.RED + "TERMINATED")

turbo_binary_rain()
