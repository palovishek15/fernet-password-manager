from cryptography.fernet import Fernet

def write_key(path: str = "key.key"):
    key = Fernet.generate_key()
    with open(path, "wb") as f:
        f.write(key)
    print(f"Key written to {path} — keep this file safe!")

if __name__ == "__main__":
    write_key()

