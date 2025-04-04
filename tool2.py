import random
from colorama import Fore, init

# Initialisiert colorama für Farben in der Konsole
init(autoreset=True)

def generate_german_number():
    """Generiert eine zufällige deutsche Telefonnummer"""
    # Deutsche Vorwahlen (Auswahl)
    area_codes = [
        '151', '152', '157', '160', '162', '170', '171', '172', 
        '173', '174', '175', '176', '177', '178', '179', # Mobilfunk
        '30', '40', '69', '89', # Großstädte
        '201', '211', '221', '231', '241', '251', '261', '271' # Weitere Städte
    ]
    
    # Wähle zufällige Vorwahl
    area_code = random.choice(area_codes)
    
    # Generiere Rufnummernteil
    if area_code.startswith('1'):  # Mobilfunk
        number_part = ''.join([str(random.randint(0, 9)) for _ in range(7)])
    else:  # Festnetz
        number_part = ''.join([str(random.randint(0, 9)) for _ in range(6, 9)])
    
    # Erstelle vollständige Nummer
    full_number = f"+49 {area_code} {number_part}"
    return full_number

def is_valid_german_number(number):
    """Einfache Validierung einer deutschen Telefonnummer"""
    # Entferne alle Nicht-Ziffern
    digits = ''.join(filter(str.isdigit, number))
    
    # Deutsche Nummern haben 10-12 Ziffern (inkl. Ländercode 49)
    if len(digits) < 10 or len(digits) > 12:
        return False
    
    # Prüfe Ländercode
    if not digits.startswith('49'):
        return False
    
    return True

def main():
    print("Deutscher Telefonnummern-Generator")
    print("Gültige Nummern werden in grün angezeigt\n")
    
    while True:
        try:
            num_to_generate = int(input("Wie viele Nummern generieren? (0 zum Beenden): "))
            if num_to_generate <= 0:
                break
                
            for _ in range(num_to_generate):
                number = generate_german_number()
                if is_valid_german_number(number):
                    print(Fore.GREEN + f"Gültig: {number}")
                else:
                    print(f"Ungültig: {number}")
                    
        except ValueError:
            print("Bitte eine Zahl eingeben!")
    
    print("\nProgramm beendet.")

if __name__ == "__main__":
    main()
