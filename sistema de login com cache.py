import bcrypt
from cachetools import TTLCache

# Temporary cache: username -> password hash
user_cache = TTLCache(maxsize=100, ttl=60)


def hash_password(password: str) -> bytes:
    """Create a bcrypt hash from a password."""
    if not password:
        raise ValueError("Password cannot be empty.")

    return bcrypt.hashpw(
        password.encode("utf-8"),
        bcrypt.gensalt()
    )


def verify_password(password: str, password_hash: bytes) -> bool:
    """Verify a password against a stored hash."""
    return bcrypt.checkpw(
        password.encode("utf-8"),
        password_hash
    )


def register_user(username: str, password: str) -> None:
    """Store user temporarily in cache."""
    if not username:
        raise ValueError("Username cannot be empty.")

    user_cache[username] = hash_password(password)
    print(f"User '{username}' registered.")


def login_user(username: str, password: str) -> bool:
    """Verify login credentials."""
    if username not in user_cache:
        print("User not found or session expired.")
        return False

    stored_hash = user_cache[username]

    if verify_password(password, stored_hash):
        print("Login successful!")
        return True

    print("Invalid password.")
    return False


# Example usage
if __name__ == "__main__":

    # Registration
    username = input("Create username: ")
    password = input("Create password: ")

    register_user(username, password)

    print("\n--- Login ---")

    # Login
    username_input = input("Username: ")
    password_input = input("Password: ")

    login_user(username_input, password_input)