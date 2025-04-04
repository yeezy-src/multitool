import os
import requests
import json
import socket
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import webbrowser
from datetime import datetime
import dns.resolver
import smtplib
import re
import subprocess
from bs4 import BeautifulSoup

def clear_screen():
    os.system('clear')

def print_banner():
    print("""
   ___  ___ _  _ _ _____ ___ ___ 
  / _ \| _ \ || |_   _/ __| _ \\
 | (_) |   / __ | | | \__ \  _/
  \___/|_|_\_||_| |_| |___/_|  
                                
    Termux Multi-Tool v2.0
    """)

def ip_lookup():
    clear_screen()
    print("[IP Lookup]")
    ip = input("Gib eine IP-Adresse ein: ")
    
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}?fields=66846719")
        data = response.json()
        
        if data['status'] == 'success':
            print("\n[Ergebnisse]")
            print(f"IP: {data['query']}")
            print(f"Land: {data['country']} ({data['countryCode']})")
            print(f"Region: {data['regionName']} ({data['region']})")
            print(f"Stadt: {data['city']}")
            print(f"ZIP: {data['zip']}")
            print(f"ISP: {data['isp']}")
            print(f"Org: {data['org']}")
            print(f"AS: {data['as']}")
            print(f"Breitengrad/Längengrad: {data['lat']},{data['lon']}")
            print(f"Zeitzone: {data['timezone']}")
            
            # Karte anzeigen
            map_url = f"https://www.google.com/maps/place/{data['lat']},{data['lon']}"
            print(f"\nKarte: {map_url}")
        else:
            print("IP nicht gefunden oder Fehler in der Abfrage.")
    except Exception as e:
        print(f"Fehler: {e}")

def phone_lookup():
    clear_screen()
    print("[Phone Lookup]")
    phone = input("Gib eine Telefonnummer ein (mit Ländervorwahl, z.B. +49123456789): ")
    
    try:
        parsed_number = phonenumbers.parse(phone)
        print("\n[Ergebnisse]")
        country = geocoder.description_for_number(parsed_number, 'en')
        provider = carrier.name_for_number(parsed_number, 'en')
        time_zone = timezone.time_zones_for_number(parsed_number)
        
        print(f"Land: {country}")
        print(f"Provider: {provider}")
        print(f"Zeitzone: {', '.join(time_zone)}")
        print(f"Valide Nummer: {phonenumbers.is_valid_number(parsed_number)}")
        print(f"Nummerntyp: {phonenumbers.number_type(parsed_number)}")
        print(f"Internationales Format: {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}")
        
        # Google Maps Suche für Standort
        if country:
            maps_url = f"https://www.google.com/maps/search/{country}+{provider}"
            print(f"\nStandort suchen: {maps_url}")
    except Exception as e:
        print(f"Fehler: {e}")

def port_scanner():
    clear_screen()
    print("[Port Scanner]")
    host = input("Gib eine IP-Adresse oder Domain ein: ")
    
    try:
        print("\nScanne häufig verwendete Ports...")
        common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 465, 587, 993, 995, 3306, 3389, 8080]
        
        for port in common_ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            if result == 0:
                service = socket.getservbyport(port, 'tcp') if port <= 1024 else "custom"
                print(f"Port {port} ({service}): Offen")
            sock.close()
    except Exception as e:
        print(f"Fehler: {e}")

def whois_lookup():
    clear_screen()
    print("[WHOIS Lookup]")
    domain = input("Gib eine Domain ein (ohne http://): ")
    
    try:
        webbrowser.open(f"https://www.whois.com/whois/{domain}")
        print("WHOIS-Informationen im Browser geöffnet.")
    except Exception as e:
        print(f"Fehler: {e}")

def email_verifier():
    clear_screen()
    print("[Email Verifier]")
    email = input("Gib eine E-Mail-Adresse ein: ")
    
    try:
        # Syntaxprüfung
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            print("Ungültiges E-Mail-Format")
            return
        
        domain = email.split('@')[1]
        
        # MX-Record prüfen
        try:
            mx_records = dns.resolver.resolve(domain, 'MX')
            mx_record = str(mx_records[0].exchange)
            print(f"\nMX Record gefunden: {mx_record}")
            
            # SMTP-Verbindung testen
            server = smtplib.SMTP(mx_record, 25, timeout=10)
            server.set_debuglevel(0)
            
            server.helo('example.com')
            server.mail('test@example.com')
            code, message = server.rcpt(email)
            
            if code == 250:
                print("E-Mail existiert wahrscheinlich (SMTP akzeptiert)")
            else:
                print("E-Mail existiert möglicherweise nicht (SMTP verweigert)")
            
            server.quit()
        except Exception as e:
            print(f"Fehler bei der Überprüfung: {e}")
    except Exception as e:
        print(f"Fehler: {e}")

def social_media_lookup():
    clear_screen()
    print("[Social Media Lookup]")
    username = input("Gib einen Benutzernamen ein: ")
    
    sites = {
        'Facebook': f'https://www.facebook.com/{username}',
        'Twitter': f'https://twitter.com/{username}',
        'Instagram': f'https://www.instagram.com/{username}',
        'LinkedIn': f'https://www.linkedin.com/in/{username}',
        'YouTube': f'https://www.youtube.com/user/{username}',
        'Reddit': f'https://www.reddit.com/user/{username}',
        'TikTok': f'https://www.tiktok.com/@{username}'
    }
    
    print("\nPrüfe Social Media Präsenz...")
    for site, url in sites.items():
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"{site}: Gefunden ({url})")
            else:
                print(f"{site}: Nicht gefunden")
        except:
            print(f"{site}: Fehler beim Überprüfen")

def wifi_password_finder():
    clear_screen()
    print("[WiFi Password Finder]")
    
    try:
        # Nur für Android/Termux
        if not os.path.exists('/data/misc/wifi'):
            print("WiFi-Informationen nicht zugänglich")
            return
        
        # WiFi-Konfiguration lesen
        with open('/data/misc/wifi/wpa_supplicant.conf', 'r') as f:
            content = f.read()
            
        networks = re.findall(r'network=\{.*?\}', content, re.DOTALL)
        
        print("\nGespeicherte WiFi-Netzwerke:")
        for net in networks:
            ssid = re.search(r'ssid="(.*?)"', net)
            psk = re.search(r'psk="(.*?)"', net)
            
            if ssid and psk:
                print(f"\nSSID: {ssid.group(1)}")
                print(f"Passwort: {psk.group(1)}")
            elif ssid:
                print(f"\nSSID: {ssid.group(1)}")
                print("Passwort: Nicht gespeichert")
    except Exception as e:
        print(f"Fehler: {e}")

def save_log(data):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("multitool_log.txt", "a") as f:
        f.write(f"[{timestamp}] {data}\n")

def main_menu():
    clear_screen()
    print_banner()
    print("1. IP Lookup")
    print("2. Phone Lookup (mit Standort)")
    print("3. Port Scanner")
    print("4. WHOIS Lookup")
    print("5. Email Verifier")
    print("6. Social Media Lookup")
    print("7. WiFi Password Finder")
    print("8. Beenden")
    
    choice = input("\nWähle eine Option: ")
    return choice

def main():
    while True:
        choice = main_menu()
        
        if choice == "1":
            ip_lookup()
            save_log("IP Lookup durchgeführt")
        elif choice == "2":
            phone_lookup()
            save_log("Phone Lookup durchgeführt")
        elif choice == "3":
            port_scanner()
            save_log("Port Scan durchgeführt")
        elif choice == "4":
            whois_lookup()
            save_log("WHOIS Lookup durchgeführt")
        elif choice == "5":
            email_verifier()
            save_log("Email Verifier durchgeführt")
        elif choice == "6":
            social_media_lookup()
            save_log("Social Media Lookup durchgeführt")
        elif choice == "7":
            wifi_password_finder()
            save_log("WiFi Password Finder durchgeführt")
        elif choice == "8":
            print("Programm wird beendet...")
            break
        else:
            print("Ungültige Auswahl!")
        
        input("\nDrücke Enter, um zum Hauptmenü zurückzukehren...")

if __name__ == "__main__":
    main()
