import random
import time
from colorama import Fore, Back, Style, init
import sys

# Initialisiert colorama
init(autoreset=True)

def generate_random_binary_stream():
    """Generiert einen endlosen Strom von bunten 1en und 0en"""
    try:
        while True:
            # Zufällige Länge für den nächsten Block (zwischen 10 und 50 Zeichen)
            block_length = random.randint(10, 50)
            
            for _ in range(block_length):
                bit = random.choice(['0', '1'])
                
                # Wähle zufällig zwischen grün und hellgrün
                color = random.choice([Fore.GREEN, Fore.LIGHTGREEN_EX])
                
                # Schreibe das Zeichen ohne Newline
                sys.stdout.write(color + bit)
                sys.stdout.flush()
                
                # Kurze Pause für den Matrix-Effekt
                time.sleep(0.05)
            
            # Neue Zeile nach jedem Block mit 50% Wahrscheinlichkeit
            if random.random() > 0.5:
                print()
                
    except KeyboardInterrupt:
        print("\n\n" + Fore.RED + "Stream gestoppt")

def main():
    print(Fore.GREEN + "Binärer Farbstrom Generator")
    print(Fore.LIGHTGREEN_EX + "Drücke STRG+C zum Beenden\n")
    
    # Starte den Generator
    generate_random_binary_stream()

if __name__ == "__main__":
    main()
