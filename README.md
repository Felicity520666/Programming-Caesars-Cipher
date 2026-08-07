# Caesar Cipher

## About this project

This project is a simple Python implementation of the classic Caesar cipher.
It encrypts or decrypts a message by shifting each letter through the alphabet
using a key from 0 to 25.

I created this project to practise Python fundamentals, including functions,
loops, conditionals, input validation, and string manipulation.

## Features

- Encrypts and decrypts messages
- Preserves uppercase and lowercase letters
- Supports messages containing multiple words
- Leaves spaces, punctuation, and numbers unchanged
- Validates the key and selected mode
- Wraps shifts around the beginning and end of the alphabet

## Requirements

- Python 3.9 or newer

No third-party packages are required.

## Running the program

Open a terminal in the project directory and run:

```bash
python3 main.py
```

Then enter your message, a key from 0 to 25, and either `encrypt` or `decrypt`.

```text
What is your message? Hello, World!
What is the key? Choose a number from 0 to 25: 3
Do you want to encrypt or decrypt? encrypt
Encrypted message: Khoor, Zruog!
```

Decrypting `Khoor, Zruog!` with the same key returns `Hello, World!`.

## Running the tests

Run the automated tests with Python's built-in test runner:

```bash
python3 -m unittest -v
```

## Important note

The Caesar cipher is useful for learning, but it is easy to break and should
not be used to protect sensitive information.

## Creator

Hi, my name is Felicity, and I am happy to share this project.
