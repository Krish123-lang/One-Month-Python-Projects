import secrets
import string


def generate_secure_password(length: int = 16) -> str:
    """Generates a secure, random password of a specified length."""
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    # Combine character sets: lowercase, uppercase, digits, and symbols
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Securely select random characters from the pool
    password = ''.join(secrets.choice(all_characters) for _ in range(length))
    return password


# Example usage:
if __name__ == "__main__":
    new_password = generate_secure_password(16)
    print(f"Generated Password: {new_password}")
