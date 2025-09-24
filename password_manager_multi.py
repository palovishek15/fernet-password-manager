#!/usr/bin/env python3
"""
password_manager_multi.py

- Ask how many accounts the user wants to store.
- Show a numbered social media list.
- Accept number (e.g. 4) or name (e.g. gmail) to select account.
- Take username and password (password hidden) and store encrypted.
- Stores lines as: AccountName|ENCRYPTED_BASE64
"""

import os
import sys
import getpass
from cryptography.fernet import Fernet
from load_key import load_key

VAULT_FILE = "passwords.txt"

SOCIAL_LIST = [
    "linkedin",
    "x",          # twitter renamed to X
    "facebook",
    "instagram",
    "gmail",
    "snapchat",
]

def print_socials():
    print("Choose from the following social/media accounts:")
    for i, name in enumerate(SOCIAL_LIST, start=1):
        print(f"{i:2}. {name.capitalize()}")

def normalize_choice(choice: str):
    """Return account name if a valid number or name; else None."""
    choice = choice.strip()
    if not choice:
        return None
    # If choice is a pure integer and in range
    if choice.isdigit():
        idx = int(choice)
        if 1 <= idx <= len(SOCIAL_LIST):
            return SOCIAL_LIST[idx - 1]
        return None
    # else match against names (case-insensitive)
    low = choice.lower()
    # accept synonyms: twitter -> x
    if low == "twitter":
        low = "x"
    if low in SOCIAL_LIST:
        return low
    return None

def store_encrypted(account_name: str, username: str, encrypted_password_b64: bytes):
    """
    Append one line to VAULT_FILE in format:
    AccountName|username|encrypted_password_base64
    """
    # ensure folder exists if path contains directories (not here but safe)
    dirpath = os.path.dirname(VAULT_FILE)
    if dirpath and not os.path.exists(dirpath):
        os.makedirs(dirpath, mode=0o700, exist_ok=True)

    with open(VAULT_FILE, "a") as f:
        # store username as-is (not encrypted) — if you want to encrypt it too, change here
        line = f"{account_name}|{username}|{encrypted_password_b64.decode()}\n"
        f.write(line)
    # tighten file permissions (best-effort)
    try:
        os.chmod(VAULT_FILE, 0o600)
    except Exception:
        pass

def main():
    # Load key
    try:
        key = load_key()
    except FileNotFoundError:
        print("key.key not found. Run 'python3 key.py' first to generate a key.")
        sys.exit(1)

    fernet = Fernet(key)

    # Ask how many accounts
    while True:
        try:
            count_raw = input("How many accounts do you want to store? ").strip()
            count = int(count_raw)
            if count <= 0:
                print("Enter a positive integer.")
                continue
            break
        except ValueError:
            print("Please enter a valid number (e.g., 3).")

    for i in range(1, count + 1):
        print(f"\nAccount {i} of {count}:")
        print_socials()
        # Ask for choice until valid
        while True:
            choice_raw = input("Enter social-media name or number (e.g. 4 or gmail): ").strip()
            acct = normalize_choice(choice_raw)
            if acct is None:
                print("Invalid choice. Try again.")
                continue
            break

        # collect username/email (allow blank)
        username = input("Enter username/email for this account (or leave blank): ").strip()

        # collect password with getpass (hidden)
        while True:
            pwd = getpass.getpass("Enter password for this account (input hidden): ").strip()
            if pwd == "":
                print("Password cannot be empty. If you want to auto-generate, type 'gen' instead.")
                # allow user to type 'gen' to auto-generate? For now require manual; can extend later
                continue
            # ask for confirmation
            pwd2 = getpass.getpass("Confirm password: ").strip()
            if pwd != pwd2:
                print("Passwords do not match — try again.")
                continue
            break

        # encrypt
        token = fernet.encrypt(pwd.encode())  # bytes (base64 urlsafe)
        store_encrypted(acct, username, token)
        print(f"Stored {acct} successfully.")

    print("\nAll done. Vault file:", os.path.abspath(VAULT_FILE))
    print("Remember: keep 'key.key' safe and don't share it. If key.key is lost, you cannot decrypt passwords.")

if __name__ == "__main__":
    main()

