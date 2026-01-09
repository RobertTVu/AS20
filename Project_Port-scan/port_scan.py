#!/usr/bin/env python3

import socket
import sys

PORTS = {
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

TIMEOUT = 1
VERSION = "1.3"

#För att underlätta användar upplevelsen skriv också ut 
#loopback address och nuvarande ip address av miljön.

#Även möjligen att det för nu endast funkar för ipv4.
#Lägg till om du orkar ipv6 funktionalitet.
def print_banner():
    print("=" * 40)
    print(f"          Port Scan v{VERSION}")
    print("=" * 40)


def scan_port(ip, port, timeout=TIMEOUT):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    except socket.error as e:
        print(f"  ERROR - Socket error on port {port}: {e}")
        return False


def scan_target(ip, ports_dict):
    open_ports = []
    closed_ports = [] 

    print(f"\nScanning {ip} ....\n")
    for port, service_name in sorted(ports_dict.items()):
        is_open = scan_port(ip, port)

        if is_open:
            print(f" Port {port:5} ({service_name:12}) is OPEN")
            open_ports.append({"port": port, "service": service_name})
    return open_ports, closed_ports


def display_results(open_ports, total_scanned):
    print("\n","=" * 40)
    print("Scan Complete")
    print(f"Total ports scanned: {total_scanned}")
    print(f"Open ports found: {len(open_ports)}")
    
    if open_ports:
        port_numbers = [str(p["port"]) for p in open_ports]
        print(f"Open ports: {', '.join(port_numbers)}")
        
    print("=" * 40)


def main():
    try:
        print_banner()

        ip = input("\nEnter IP-address: ").strip()

        open_ports, closed_ports = scan_target(ip, PORTS)

        display_results(open_ports, len(PORTS))

    except KeyboardInterrupt:
        print("\n\nScan cancelled by user")
    except Exception as e:
        print(f"\nError - An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()