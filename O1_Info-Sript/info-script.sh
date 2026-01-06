#!/bin/bash

echo "Welcome to a easy Recon script for checking on a Linux Env"

echo
echo "=== SYSTEMINFO ==="
uname -a
date
df
ps
echo
uptime

echo
env | grep auth.sock
echo
du

echo
echo "=== USER ==="
echo $USER
w
id
groups

echo
echo "=== User w SHELL ==="
cat /etc/passwd | grep "sh$"

echo
echo "=== Network ==="
ip a | grep inet
ifconfig -a | grep -A 1 wlan
echo
echo "=== Curl Public IP INFO  ==="
curl ipinfo.io/ip
arp

echo
echo "=== RAM Usage  ==="
free -h

echo
echo "=== CPU INFO  ==="
lscpu | grep Core
