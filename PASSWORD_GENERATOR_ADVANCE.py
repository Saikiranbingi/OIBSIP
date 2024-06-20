import random
import string
import argparse

def generate_password(length, include_letters=True, include_numbers=True, include_symbols=True):
    characters = ''
    if include_letters:
        characters += string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one option for character set must be selected.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description="Generate a random password.")
    parser.add_argument('length', type=int, help="Length of the password")
    parser.add_argument('--letters', action='store_true', help="Include letters (default: True)")
    parser.add_argument('--numbers', action='store_true', help="Include numbers (default: True)")
    parser.add_argument('--symbols', action='store_true', help="Include symbols (default: True)")
    args = parser.parse_args()

    try:
        password = generate_password(args.length, args.letters, args.numbers, args.symbols)
        print(f"Generated password: {password}")
    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()
