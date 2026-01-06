# MD5 Hash Generator & Cracker with HashCat

**Description:**
This project demonstrates how MD5 hashing works and its weaknesses against rainbow table attacks.

## Files
- `md5-hasher-unsecure.py` - Original script from https://github.com/cyber-fs
- `md5-hasher.py` - Modified version that generates 10 passwords with 9 digits each
- `md5-hashcat.sh` - Bash script to decrypt/crack hashes using Hashcat
- `mina_hashar.txt` - Generated MD5 hashes for testing

## Results
- Rainbow tables (CrackStation) can decrypt/crack passwords up to **8 digits**
- Passwords with **9 digits or more** are not found in rainbow tables
- Hashcat can successfully brute-force 9-digit passwords (time depends on your system)

## Usage
```bash
# Generate hashes and save to file
python3 md5-hasher.py > mina_hashar.txt

# chmod 766 md5-hashcat.sh before using it
# Crack hashes with Hashcat (uses default: mina_hashar.txt, 9 digits)
./md5-hashcat.sh

# Custom file and password length (example: 6 digits)
./md5-hashcat.sh  ?d?d?d?d?d?d
```

## Notes
- `?d` represents a digit (0-9) in Hashcat mask attack
- Adjust the number of `?d` to match your password length
- This is for educational purposes only - MD5 is cryptographically broken

## Learning Outcomes
- Understanding rainbow table limitations
- Hands-on experience with Hashcat mask attacks
- Git workflow and documentation

