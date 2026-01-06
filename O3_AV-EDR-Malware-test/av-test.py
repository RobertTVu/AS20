#!/usr/bin/env python3
import platform
import os
import time

system = platform.system()

if system == "Windows":
    print("[+++] Windows upptäckt. Scriptet fortsätter...")
    

    eicar_str = r"X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"
    

    # Använd C:\temp (skapar om den inte finns)
    temp_dir = r"C:\temp"
    if not os.path.exists(temp_dir):
        print(f"[...] Skapar mapp: {temp_dir}\n")
        os.makedirs(temp_dir)
    

    file_path = os.path.join(temp_dir, "EICAR-test.com")
    print(f"[...] Försöker skapa: {file_path}\n")
    

    try:
        with open(file_path, "w", encoding="ascii") as f:
            f.write(eicar_str)
        
        print("[+++] Fil skapad framgångsrikt!")
        print("[...] Väntar 3 sekunder för AV/EDR reaktion...\n")
        time.sleep(3)
        
        if os.path.exists(file_path):
            print("[!!!] VARNING: Filen finns fortfarande kvar!")
            print("[!!!] AV/EDR reagerade INTE vid skapande")
            print(f"[...] Testa öppna filen: {file_path}")
        else:
            print("\n[---] Filen raderades av AV/EDR!")
            print("[---] Real-time protection fungerar korrekt!")

    except Exception as e:
        print(f"\n[!!!] Oväntat fel: {type(e).__name__}: {e}")


elif system == "Linux":
    print("Linux upptäckt. Detta script är avsett för Windows.")
    exit()
    
elif system == "Darwin":
    print("macOS upptäckt. Detta script är avsett för Windows.")
    exit()
    
else:
    print(f"Okänt OS ({system}). Detta script är avsett för Windows.")
    exit()