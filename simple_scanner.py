#!/usr/bin/env python3

"""
Simple Network Port Scanner

"""

import socket

ip = input("\nEnter IP-address: ")

# Lista på portar 
ports = [21,22,23,80,443,3306,3389,8080]

print(f"\nScanning {ip} ....\n")

for port in ports:
    try:

        # Skapa socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        # Försök anslut
        result = sock.connect_ex((ip, port))

        # Om result = 0 då är porten öppen

        if result == 0:
            print (f" Port {port} is OPEN")
        else:
            print(f" Port {port} is CLOSED")

        sock.close()

    except:
        print(f" Port {port} - Could not Scan?!= ")

print("\nScan Done!")