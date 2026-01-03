#!/usr/bin/env python3
import socket

# Lista på portar 
ports = {
    20: "FTP-Data",
    21: "FTP", 
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    135: "RPC",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    1433: "MSSQL",
    1521: "Oracle",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    5900: "VNC",
    8080: "HTTP-Alt",
    8443: "HTTPS-Alt"
}
print("=" * 40)
print("          Port Scan v1.2")
print("=" * 40)


ip = input("\nEnter IP-address: ")
print(f"\nScanning {ip} ....\n")

open_ports = 0
for port, name in ports.items():
    try:
        # Skapa socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

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
