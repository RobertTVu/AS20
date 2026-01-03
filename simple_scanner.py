#!/usr/bin/env python3
import socket

# Lista på portar fyll mer?
ports = {21: "FTP", 22: "SSH",23: "Telnet",80: "HTTP", 443: "HTTPS", 3306: "MySQL", 3389: "RDP", 8080: "ALT-HTTP"}

print("=" * 40)
print("          Port Scan v1.1")
print("=" * 40)


ip = input("\nEnter IP-address: ")
print(f"\nScanning {ip} ....\n")

open_ports = 0
for port, name in ports.items():
    try:
        # Skapa socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)

        # Försök anslut
        result = sock.connect_ex((ip, port))

        # Om result = 0 då är porten öppen

        if result == 0:
            print (f" Port {port} ({name}) is OPEN")
            open_ports += 1
        else:
            print(f" Port {port} ({name}) is CLOSED")

        sock.close()

    except:
        print(f" Port {port} - Could not Scan?! ")


print("\n","=" * 40)
print(f"Found {open_ports} Open ports")
print("=" * 40)
