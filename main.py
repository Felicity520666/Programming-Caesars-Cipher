# Global variables
possibleCharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
initialPosition = 0
shiftedPosition = 0
shiftedMessage = ""

# Run code

# Introduction
print("Welcome! This program will encrypt or decrypt your secret message using the Caesar cipher. \n\nWhen creating your message, you may only chosse from the following characters: " + possibleChrarcters + "\n\nLet's get started!\n")

# Receive user input
initialMessage = input("What is your message? ")
key = int(input("What is the key? Choose a number from 0 to 25. "))
mode = input("Do you want to encrypt or decrypt? ")

# Encrypt or decrypt the message
for character in intialMessage:
    if character in possibleCharacters:
        initialPosition = possibleCharacters.find(character)

        if mode.lower() == "encrypt":
            shiftedPosition = initialPosition + key

        elif mode.lower() == "decrypt":
            shiftedPosition = initialPosition - key

        if shiftedPosition >= len(possibleCharacters):
            shiftedPosition = shiftedPosition - len(possibleCharacters)

        elif shiftedPosition < 0:
            shiftedPosition = shiftedPosition + len(possibleCharacters)

        shiftedMessage = shiftedMessage + possibleCharacters[shiftedPosition]

    else:
        shiftedMessage = shiftedMessage + character
    
# Print the shifted message
print("Your " + mode.lower() + "ed message is: " + shiftedMessage)