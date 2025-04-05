def vibrate(duration=500):
    os.system(f'termux-vibrate -d {duration}')
    print(f"📳 Vibration für {duration}ms")
