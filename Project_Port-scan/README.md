# Port_Scanner 

A simple and beginner-friendly network port scanner written in Python for educational purposes.

## Description

Port Scanner scans common ports on a specified IP address to identify open services. Perfect for monitoring your homelab network and learning the basics of network scanning and Python socket programming.

## Installation

### Prerequisites
- Python 3. latest version
- Git (optional)

### Download

**Option 1: Using Git**
```bash
git clone https://github.com/RobertTVu/AS20.git
cd AS20
```

**Option 2: Direct Download**
Download `port_scan.py` directly from the repository.

## Usage

### Linux / macOS
```bash
# Method 1: Run with Python
python3 port_scan.py

# Method 2: Make executable and run
chmod +x port_scan.py
./port_scan.py
```

### Windows
```powershell
# In Command Prompt or PowerShell
python port_scan.py
```

## Details

**Tech in use**
- Python 3
- Socket library

**How it works**
1. Create a TCP socket for each port
2. Attempts to connect to target IP:port
3. Reports connection success (Open) or failure (Closed)
4. Timeout set to 1 second per port