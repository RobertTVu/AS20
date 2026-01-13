# Port Scanner 

A network port scanner for educational purposes and homelab monitoring.

---

## Purpose

Learn network security fundamentals by building a TCP port scanner from scratch.

**Goals:**
- Understand TCP/IP and socket programing
- Monitor **[homelab](./Picture/env.png)** networks 
- Save scan logs for security documentation
- Practice python development

---

## Function

Scans 22 common TCP ports on a target IP address to identify open services.

**Features:**
- Scans 22 common service ports (SSH, HTTP, HTTPS, SMB, RDP, etc.)
- IPv4 address validation (X.X.X.X format, 0-255)
- 1-second timeout per port
- Results export to text file
- Command-line arguments support
- Cross-platform (Linux, Windows, macOS)

**How it works:**
1. Validates IP address format
2. Creates TCP socket for each port
3. Attempts connection with timeout
4. Reports open/closed status
5. Optionally saves results to file

**Program Flow:**
- **[Flow Chart](./Picture/FlowChartV1-4.png)**

---

## System Requirements

**Required:**
- Python 3.latest
- OS: Linux, Windows, or macOS

**Libraries:** Standard library only (socket, sys, argparse, os, datetime)

**Network:** Access to target, no firewall blocking, Bridged mode for VMs


## Instructions & Usage
```bash
# Download repo
git clone https://github.com/RobertTVu/AS20.git
cd port_scan/

# Verify Python
python3 --version  
```

### Basic Scanning

**[How it look like in use](./Picture/Usage.png)**

```bash
python3 port_scan.py                # Interactive mode:
python3 port_scan.py 192.168.1.1    # Direct scan:

# Linux/macOS: Make executable (optional)
chmod +x port_scan.py
./port_scan.py [flag] 127.0.0.1     # Run 
```

**Usage for flag:**
```bash
python3 port_scan.py [flag] [IP-Target] 
# -v, --version     # show version
# -h, --help        # show help manual 
# -l, --log         # Save to scan_[IP]_[Timestamp].txt 
```

---

## Limitations
- IPv4 only (IPv6 planned)
- TCP only (UDP planned)
- 22 ports (custom ranges planned)
- Single-threaded 
- **[NAT mode VMs cannot be scanned from host](./Picture/limitation.png)**

---

## Roadmap
**Planned features:**
- UDP port scanning (`-u` flag)
- IPv6 support
- Service version detection (`-s` flag)
    - verbose (`-v` flag)
- Scanning (faster)
- Custom port ranges
- JSON/CSV output formats

- Web/interface
- Docker container
- Integration with WorkTools project

---
