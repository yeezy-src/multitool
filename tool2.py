import random
from colorama import Fore, init

# Initialisiert colorama für Farben in der Konsole
init(autoreset=True)

# Länderdaten mit Vorwahlen und Nummernformaten
COUNTRY_DATA = {
    "Deutschland": {
        "code": "49",
        "area_codes": [
            '151', '152', '157', '160', '162', '170', '171', '172', 
            '173', '174', '175', '176', '177', '178', '179', # Mobilfunk
            '30', '40', '69', '89', # Großstädte
            '201', '211', '221', '231', '241', '251', '261', '271' # Weitere Städte
        ],
        "mobile_length": 7,
        "landline_length": (6, 9)
    },
    "Österreich": {
        "code": "43",
        "area_codes": [
            '650', '660', '664', '676', '677', '678', '680', '681', # Mobilfunk
            '1', '316', '463', '512', '662' # Festnetz
        ],
        "mobile_length": 7,
        "landline_length": (7, 9)
    },
    "Schweiz": {
        "code": "41",
        "area_codes": [
            '74', '75', '76', '77', '78', '79', # Mobilfunk
            '21', '22', '24', '26', '31', '32' # Festnetz
        ],
        "mobile_length": 7,
        "landline_length": (7, 8)
    },
    "USA": {
        "code": "1",
        "area_codes": [
            '201', '202', '203', '205', '206', '212', '213', '214', # Beispiel-Area-Codes
            '310', '312', '315', '323', '415', '510', '650', '713'
        ],
        "mobile_length": 7,
        "landline_length": 7
    },
    "Frankreich": {
        "code": "33",
        "area_codes": [
            '6', '7', # Mobilfunk
            '1', '2', '3', '4', '5' # Festnetz (erste Ziffer)
        ],
        "mobile_length": 8,
        "landline_length": 8
    }
}

def generate_number(country):
    """Generiert eine zufällige Telefonnummer für das ausgewählte Land"""
    data = COUNTRY_DATA[country]
    is_mobile = random.choice([True, False])
    
    if is_mobile and 'mobile_length' in data:
        # Mobilfunknummer generieren
        area_code = random.choice([ac for ac in data["area_codes"] if len(ac) > 2 or random.random() > 0.7])
        number_length = data["mobile_length"]
    else:
        # Festnetznummer generieren
        area_code = random.choice(data["area_codes"])
        number_length = random.randint(*data["landline_length"]) if isinstance(data["landline_length"], tuple) else data["landline_length"]
    
    # Nummernteil generieren
    number_part = ''.join([str(random.randint(0, 9)) for _ in range(number_length)])
    
    # Formatierung nach Land
    if country == "USA":
        return f"+{data['code']} ({area_code}) {number_part[:3]}-{number_part[3:]}"
    elif country == "Frankreich":
        return f"+{data['code']} {area_code} {number_part[:2]} {number_part[2:4]} {number_part[4:6]} {number_part[6:]}"
    else:
        return f"+{data['code']} {area_code} {number_part}"

def is_valid_number(number, country):
    """Einfache Validierung der Telefonnummer"""
    digits = ''.join(filter(str.isdigit, number))
    data = COUNTRY_DATA[country]
    
    # Prüfe Ländercode
    if not digits.startswith(data["code"]):
        return False
    
    # Prüfe Länge
    expected_length = len(data["code"]) + (data["mobile_length"] + len(random.choice(data["area_codes"])))
    if not (expected_length - 3 <= len(digits) <= expected_length + 3):
        return False
    
    return True

def select_country():
    """Lässt den Benutzer ein Land auswählen"""
    print("\nVerfügbare Länder:")
    for i, country in enumerate(COUNTRY_DATA.keys(), 1):
        print(f"{i}. {country}")
    
    while True:
        try:
            choice = int(input("\nWählen Sie ein Land (1-" + str(len(COUNTRY_DATA)) + "): "))
            if 1 <= choice <= len(COUNTRY_DATA):
                return list(COUNTRY_DATA.keys())[choice-1]
            print("Ungültige Auswahl!")
        except ValueError:
            print("Bitte eine Zahl eingeben!")

def main():
    print("Internationaler Telefonnummern-Generator")
    print("Gültige Nummern werden in grün angezeigt\n")
    
    country = select_country()
    
    while True:
        try:
            num_to_generate = int(input(f"\nWie viele Nummern für {country} generieren? (0 zum Beenden): "))
            if num_to_generate <= 0:
                break
                
            for _ in range(num_to_generate):
                number = generate_number(country)
                if is_valid_number(number, country):
                    print(Fore.GREEN + f"Gültig: {number}")
                else:
                    print(f"Ungültig: {number}")
                    
        except ValueError:
            print("Bitte eine Zahl eingeben!")
    
    print("\nProgramm beendet.")

if __name__ == "__main__":
    main()
