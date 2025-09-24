# 🔐 Fernet Password Manager

A lightweight **Password Manager** in Python designed to **use my daily activity** while keeping passwords secure.  
This project uses the `cryptography` library (Fernet) to encrypt passwords, supports multiple-account entry flows, and includes features to view and delete stored credentials.

Repository: [https://github.com/palovishek15/fernet-password-manager](https://github.com/palovishek15/fernet-password-manager)

---

## Table of Contents
1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Tech Stack](#tech-stack)  
4. [Project Structure](#project-structure)  
5. [Quick Start (Kali Linux)](#quick-start-kali-linux)  
6. [Commands & Usage Examples](#commands--usage-examples)  
7. [Data Storage & Vault](#data-storage--vault)  
8. [Security Recommendations](#security-recommendations)  
9. [Next Steps](#next-steps)  
10. [Contributing & License](#contributing--license)

---

## Project Overview
This is a learning-oriented password manager that allows you to:  

- Encrypt and store passwords securely using **Fernet symmetric encryption**.  
- Manage multiple accounts in one run (multi-input flow).  
- View stored credentials (account & username).  
- Retrieve decrypted passwords when needed.  
- Delete specific credentials safely.

---

## Features
- Add multiple accounts at once.  
- Supports both **number** or **name** input for social/account selection:
  - LinkedIn, X/Twitter, Facebook, Instagram, Gmail, Snapchat.  
- Securely encrypt passwords before saving.  
- Interactive CLI for adding, viewing, and deleting credentials.  
- Encrypted vault file (`passwords.txt`) with separate encryption key (`key.key`).  

---

## Tech Stack
- **Language:** Python 3  
- **Libraries:** 
  - `cryptography` (Fernet encryption)
  - `os` & `getpass` (system & hidden input handling)  

---

## Project Structure
fernet-password-manager/
├── README.md
├── key.py # Generate encryption key (run once)
├── load_key.py # Helper to load key
├── password_manager_multi.py # Main program for adding multiple accounts
├── view_vault.py # Decrypt & view all entries
├── delete_entry.py # Interactive delete script
├── passwords.txt # Vault file (auto-created)
├── key.key # Encryption key (auto-created)
├── .gitignore # Recommended
└── tests/ # Optional unit tests



## Quick Start (Kali Linux)
Copy-paste these commands to set up the project:

bash
# 1. Clone the repo
git clone https://github.com/palovishek15/fernet-password-manager.git
cd fernet-password-manager

# 2. Create a Python virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install --upgrade pip
pip install cryptography

# 4. Generate encryption key (run once)
python3 key.py

# 5. Run the multi-account manager
python3 password_manager_multi.py

# 6. View stored credentials
python3 view_vault.py

# 7. Delete an entry (interactive)
python3 delete_entry.py
Commands & Usage Examples
Add multiple accounts

python3 password_manager_multi.py
Prompts: How many accounts do you want to store?

For each account: select by number (e.g., 4) or name (gmail).

Enter username/email and password (hidden), confirm password.

View decrypted credentials

python3 view_vault.py
Example output:

graphql
Copy code
001 | gmail      | me@example.com               | myS3cretP@ssw0rd
002 | facebook   | user123                      | anotherPass123
Delete a credential

python3 delete_entry.py
Lists entries with numbers.

Prompts for entry number to delete and confirmation.

Data Storage & Vault
Vault file: passwords.txt

Each line format:

Copy code
account_name|username|FERNET_TOKEN_BASE64
Encryption key file: key.key

Example line:

gmail|me@example.com|gAAAAABlZQ... (long base64 token)
Security Recommendations
Do not commit key.key or passwords.txt to Git. Add to .gitignore:


key.key
passwords.txt
Restrict file permissions:


chmod 600 key.key
chmod 600 passwords.txt
chmod 700 ~/Documents/password_manager
Use non-root user on Kali Linux.

Consider master password + KDF (Argon2/scrypt) for stronger security.

Encrypt usernames too if sensitive.

For secure deletion, use shred instead of simple file rewrite:

shred -u passwords.txt
Avoid leaving passwords in clipboard.

Next Steps
Move from file-based storage to encrypted SQLite (SQLCipher).

Add GUI using Tkinter or PySimpleGUI.

Implement master-password authentication with Argon2.

Add unit tests for add/view/delete flows.

Contributing
Fork the repo, add features or improvements, submit a pull request.

Never push key.key or passwords.txt in PRs.

License
This project is licensed under the MIT License.

MIT License
Copyright (c) 2025 Ovishek Pal
GitHub Tips

To publish your repo (if not already):
git init
git add .
git commit -m "Initial commit: Fernet Password Manager"
git branch -M main
git remote add origin git@github.com:palovishek15/fernet-password-manager.git
git push -u origin main
