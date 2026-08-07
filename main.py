"""Encrypt and decrypt messages with a Caesar cipher."""

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
VALID_MODES = {"encrypt", "decrypt"}


def caesar_cipher(message: str, key: int, mode: str) -> str:
    """Return ``message`` encrypted or decrypted by ``key`` positions.

    Letter case is preserved, while spaces, punctuation, and numbers are left
    unchanged.

    Raises:
        ValueError: If the key or mode is invalid.
    """
    if not 0 <= key < len(ALPHABET):
        raise ValueError("The key must be between 0 and 25.")
    if mode not in VALID_MODES:
        raise ValueError("The mode must be 'encrypt' or 'decrypt'.")

    direction = 1 if mode == "encrypt" else -1
    shifted_message: list[str] = []

    for character in message:
        uppercase_character = character.upper()

        if uppercase_character in ALPHABET:
            initial_position = ALPHABET.index(uppercase_character)
            shifted_position = (initial_position + direction * key) % len(ALPHABET)
            shifted_character = ALPHABET[shifted_position]

            if character.islower():
                shifted_character = shifted_character.lower()

            shifted_message.append(shifted_character)
        else:
            shifted_message.append(character)

    return "".join(shifted_message)


def get_key() -> int:
    """Prompt until the user enters an integer from 0 to 25."""
    while True:
        try:
            key = int(input("What is the key? Choose a number from 0 to 25: "))
        except ValueError:
            print("Please enter a whole number from 0 to 25.")
            continue

        if 0 <= key < len(ALPHABET):
            return key

        print("The key must be between 0 and 25.")


def get_mode() -> str:
    """Prompt until the user chooses encryption or decryption."""
    while True:
        mode = input("Do you want to encrypt or decrypt? ").strip().lower()
        if mode in VALID_MODES:
            return mode
        print("Please enter 'encrypt' or 'decrypt'.")


def main() -> None:
    """Run the interactive Caesar cipher program."""
    print(
        "Welcome! This program encrypts or decrypts a message using a "
        "Caesar cipher.\nLetters will be shifted; all other characters will "
        "remain unchanged.\n"
    )

    message = input("What is your message? ")
    key = get_key()
    mode = get_mode()
    result = caesar_cipher(message, key, mode)

    action = "Encrypted" if mode == "encrypt" else "Decrypted"
    print(f"{action} message: {result}")


if __name__ == "__main__":
    main()
