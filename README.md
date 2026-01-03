# NetScanner 

A simple and beginner-friendly network port scanner written in Python.

## Description

NetScanner scans common ports on a specified IP address to identify open services. Perfect for monitoring your homelab network and learning the basics of network scanning and Python socket programming.

## Installation

### Prerequisites
- Python 3.6 or later
- Git (optional)

### Download

**Option 1: Using Git**
```bash
git clone https://github.com/RobertTVu/NetScanner.git
cd NetScanner
```

**Option 2: Direct Download**
Download `simple_scanner.py` directly from the repository.

## Usage

### Linux / macOS
```bash
# Method 1: Run with Python
python3 simple_scanner.py

# Method 2: Make executable and run
chmod +x simple_scanner.py
./simple_scanner.py
```

### Windows
```powershell
# In Command Prompt or PowerShell
python simple_scanner.py
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