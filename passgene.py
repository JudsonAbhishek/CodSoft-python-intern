import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_punctuation=True):
    """
    Generate a random password of the specified length with optional character types.

    Args:
        length (int): Length of the password (default is 12).
        use_uppercase (bool): Whether to include uppercase letters (default is True).
        use_lowercase (bool): Whether to include lowercase letters (default is True).
        use_digits (bool): Whether to include digits (default is True).
        use_punctuation (bool): Whether to include punctuation characters (default is True).

    Returns:
        str: Generated password.
    """
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be selected.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the length of the password: "))
        password = generate_password(length)
        print("Generated password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
