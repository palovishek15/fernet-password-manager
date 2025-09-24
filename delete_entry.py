#!/usr/bin/env python3
import os

VAULT = "passwords.txt"

def list_entries():
    if not os.path.exists(VAULT):
        print("No vault file found.")
        return []
    with open(VAULT, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    print("\nStored credentials:")
    for i, line in enumerate(lines, start=1):
        try:
            account, username, token = line.split("|", 2)
        except ValueError:
            print(f"{i:03d}: [corrupted entry] {line}")
            continue
        print(f"{i:03d}: {account} | {username}")
    return lines

def delete_entry():
    lines = list_entries()
    if not lines:
        return
    try:
        num = int(input("\nEnter the number of the entry to delete: "))
        if not (1 <= num <= len(lines)):
            print("Invalid entry number.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    confirm = input(f"Are you sure you want to delete entry {num}? (y/n): ").lower()
    if confirm != "y":
        print("Aborted.")
        return

    # Remove the chosen line
    deleted = lines.pop(num - 1)
    with open(VAULT, "w") as f:
        for line in lines:
            f.write(line + "\n")

    print(f"Deleted: {deleted}")

if __name__ == "__main__":
    delete_entry()

