def load_key(path: str = "key.key") -> bytes:
    """Load the Fernet key from key.key"""
    with open(path, "rb") as f:
        return f.read()

