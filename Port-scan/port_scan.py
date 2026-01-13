#!/usr/bin/env python3

import socket
import sys
import argparse
import os
import datetime

# ============================================

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
    8443: "HTTPS-Alt",
    45552: "TailScale"
}

TIMEOUT = 1
VERSION = "1.4"
AUTHOR = "RTxVU"

# ============================================
#1.Get your IP
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except:
        return "N/A"

#2.Print your start banner
def print_banner():
    print("\n\n" + "=" * 45)
    print(f"          Port Scan v{VERSION}")
    print("=" * 45)
    print(f"Your IP: {get_local_ip()}")
    print(f"Protocol: IPv4 only")
    print("=" * 45)

#3.Check if ip format is valid
def validate_ip(ip_address):
    try:
        parts = ip_address.split('.')

        if len(parts) != 4:
            return False
        for part in parts:
            if not part.isdigit():
                return False
            num = int(part)
            if num < 0 or num > 255:
                return False
        return True
    except (ValueError, AttributeError):
        return False

#4.The Core work
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

#5.Scan all PORTS using w scan_port
def scan_target(ip, ports_dict):
    open_ports = []
    closed_ports = [] 

    print(f"\nScanning {ip} ..\n")
    for port, service_name in sorted(ports_dict.items()):
        is_open = scan_port(ip, port)

        if is_open:
            print(f" Port {port:5} ({service_name:12}) is OPEN")
            open_ports.append({"port": port, "service": service_name})
        else:
            closed_ports.append({"port": port, "service": service_name})
    return open_ports, closed_ports

#6.Display results
def display_results(open_ports, total_scanned):
    print("\n\n" + "=" * 45)
    print("Scan Complete")
    print(f"Total ports scanned: {total_scanned}")
    print(f"Open ports found: {len(open_ports)}")
    
    if open_ports:
        port_numbers = []
        for p in open_ports:
            port_numbers.append(str(p["port"]))
        print(f"Open ports: {', '.join(port_numbers)}")
        
    print("=" * 45)

#7.Save_results to file txt
def save_results(ip, open_ports, closed_ports, total_scanned):
    timestamp = datetime.now().strftime("%Y%m%d")
    safe_ip = ip.replace('.', '_')
    filename = f"scan_{safe_ip}_{timestamp}.txt"

    try:
        with open(filename, 'w', encoding='utf-8') as f:
            #Header
            f.write("=" * 60 + "\n")
            f.write(f"Port Scan Report - v{VERSION}\n")
            f.write("=" * 60 + "\n")
            f.write(f"Target IP:       {ip}\n")
            f.write(f"Scan Date/Time:  {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Scanner Version: {VERSION}\n")
            f.write(f"Author:          {AUTHOR}\n")
            f.write("=" * 60 + "\n\n")
            #Summary
            f.write("SCAN SUMMARY\n")
            f.write("-" * 60 + "\n")
            f.write(f"Total ports scanned: {total_scanned}\n")
            f.write(f"Open ports found:    {len(open_ports)}\n")
            f.write(f"Closed ports:        {len(closed_ports)}\n")
            f.write("\n")

            #Open ports
            if open_ports:
                f.write("OPEN PORTS\n")
                f.write("-" * 60 + "\n")
                for port_info in open_ports:
                    f.write(f"Port {port_info['port']:5} - {port_info['service']}\n")
                f.write("\n")
            else:
                f.write("No open ports found.\n\n")
            
            #End
            f.write("=" * 60 + "\n")
            f.write("End of Report\n")
            f.write("=" * 60 + "\n")
        
        return filename
    
    except IOError as e:
        print(f"\n[ERROR] Could not save file: {e}")
        return None

#8.Command-line argument 
def parse_arguments():
    parser = argparse.ArgumentParser(
        description="\nDescription:\nNetwork Port Scanner - Scan common ports on a target IP address",
        epilog=f"Example: python3 port_scan.py 192.168.1.1\nAuthor: {AUTHOR}",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        'target',
        nargs='?',
        help='target IP address to scan (Optional, will prompt if not provided)'
    )

    parser.add_argument(
        '-v', '--version',
        action='version',
        version=f'Port Scanner v{VERSION} by {AUTHOR}'
    )

    parser.add_argument(

        '-l', '--log',
        action='store_true',
        help='Save scan results to log file (scan_<IP>_<timestamp>.txt)'
    )
    return parser.parse_args()


def main():
    try:
        args = parse_arguments()                            #For -flags

        print_banner()                                      #Display banner

        if args.target:                                     # From Command line input w IP-target
            ip = args.target
            print(f"\nTarget: {ip} (from command line)")
        else:
            ip = input("\nEnter IP-address: ").strip()      #Get User input


        if not validate_ip(ip):                             #Valid IP format
            print(f"\nERROR Invalid IP address format: {ip}")
            print("\nValid format: X.X.X.X (where X is 0-255)")
            sys.exit(1)

        open_ports, closed_ports = scan_target(ip, PORTS)    #Scan Target
        display_results(open_ports, len(PORTS))              #Display results

        if args.log:                                         #Save if -l is used
            filename = save_results(ip, open_ports, closed_ports, len(PORTS))
            if filename:
                print(f"\nResults saved to: {filename}")
                full_path = os.path.abspath(filename)
                print(f"    Location: {full_path}")

    except KeyboardInterrupt:                               #Ctrl+c
        print("\n\nScan cancelled by user")
    except Exception as e:                                  #Something went wrong
        print(f"\nError - An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()