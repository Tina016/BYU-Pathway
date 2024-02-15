#Week 4 | Activity 1 - Loops
"""
Author: Martina Toebe

Purpose: Demonstrate your understanding of loops by completing the following individual checkpoint assignment.

"""

# Import libraries

import random

# Start

print("\nWelcome to the word guessing game!\n\nThe context of the game is 'cars'.\n\nI hope you enjoy and have some fun!\n")

# Variables

secret_list = ["toyota", "mitsubishi", "honda", "hyunday", "mercedes", "nissan", "peugeut", "renault", "citroen", "jac", "byd", "tesla", "jaguar"]
secret_word = random.choice(secret_list)

# Hint

secret_letters = []
hint = "_ " * len(secret_word)
print(f"\nYour hint is: ({len(secret_word)} characters) {hint}\n")

# Loops

guesses = 0
while True:
    guess = input("\nWhat is your guess?\n").lower()

    if len(guess) != len(secret_word):
        print("\nOh no, note that the guess must have the same number of letters as the secret word.\nTry again!\n")
    else:
        secret_letters = list(guess)
        guesses += 1

        if secret_letters == list(secret_word):
            print(f"\nCongratulations! You guessed it!\nYou guessed, {guesses} guesses.")
            break
        else:
            hint = ""
            for i, letter in enumerate(secret_word):
                if letter in secret_letters:
                    if letter == secret_letters[i]:
                        hint += letter.upper() + " "
                    else:
                        hint += letter.lower() + " "
                else:
                    hint += "_ "
            print(f"\nYour hint is: ({len(secret_word)} characters) {hint}\n")

# End
