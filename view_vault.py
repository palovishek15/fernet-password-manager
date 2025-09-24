#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet

VAULT = "passwords.txt"
KEY = "key.key"

def main():
    if not os.path.exists(KEY):
        print("key.key not found. Run key.py to generate the key.")
        return
    if not os.path.exists(VAULT):
        print("No vault file (passwords.txt) found.")
        return

    key = open(KEY,"rb").read()
    f = Fernet(key)

    print("Decrypted entries:")
    with open(VAULT,"r") as fh:
        for lineno, line in enumerate(fh, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                account, username, token = line.split("|", 2)
            except ValueError:
                print(f"{lineno}: Malformed line: {line}")
                continue
            try:
                password = f.decrypt(token.encode()).decode()
            except Exception as e:
                password = f"<decryption error: {e}>"
            print(f"{lineno:03d} | {account:<10} | {username:<30} | {password}")

if __name__ == "__main__":
    main()

