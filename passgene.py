import random
import string

def generate_password(length=12, use_uppercase=True, use_lowercase=True, use_digits=True, use_punctuation=True):
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

def get_user_input(prompt, valid_responses):
    response = input(prompt).strip().lower()
    while response not in valid_responses:
        print("Invalid input. Please enter one of the following:", ', '.join(valid_responses))
        response = input(prompt).strip().lower()
    return response

def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired length of the password: "))
        
        use_uppercase = get_user_input("Include uppercase letters? (yes/no): ", {'yes', 'no'}) == 'yes'
        use_lowercase = get_user_input("Include lowercase letters? (yes/no): ", {'yes', 'no'}) == 'yes'
        use_digits = get_user_input("Include digits? (yes/no): ", {'yes', 'no'}) == 'yes'
        use_punctuation = get_user_input("Include symbols? (yes/no): ", {'yes', 'no'}) == 'yes'
        
        if not (use_uppercase or use_lowercase or use_digits or use_punctuation):
            raise ValueError("At least one character type must be selected.")

        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_punctuation)
        print("Generated password:", password)
        
    except ValueError as e:
        print("Error:", e)
        print("Please try again.")

if __name__ == "__main__":
    main()
