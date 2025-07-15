import random
import string

def generate_password(length):
    if length < 4:
        return "Password length should be at least 4."

    # Character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_chars = lowercase + uppercase + digits + symbols

    # Ensure at least one from each
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill remaining characters
    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)

    return ''.join(password)

# Main program
try:
    length = int(input("Enter desired password length: "))
    password = generate_password(length)
    print(f"\nGenerated Password: {password}")
except ValueError:
    print("Please enter a valid number.")

# Keep window open
input("\nPress Any Key to exit...")
