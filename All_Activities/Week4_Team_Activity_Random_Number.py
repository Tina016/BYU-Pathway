#Week 4 | Team Activity - Grade Calculator Program - Core Requirements
"""
Author: Martina Toebe

Purpose: Write a program that determines the letter grade for a course according to the following scale:

Instructions
In the Guess My Number game the computer picks a magic number, and then the user tries to guess it. After each guess, the computer tells the user to guess "higher" or "lower" until they guess the magic number.

This assignment is a little tricky, because it brings together many of the concepts you've learned in this course including loops and if statements.

Having the computer pick a random number
There is a random number library included with Python that contains a number of different functions to generate random numbers, depending on if you want integers, floating point numbers, and from different statistical distributions.

The only function you will need from this library is called randint. To use it, you give it two numbers and it returns back a random number in that range. In order to use this function you need to import it from the random library.

The following code shows how to import the function and use it to get a random number from 1 to 10.



Core Requirements:

Work through these core requirements step-by-step to complete the program. Please don't skip ahead and do the whole thing at once, because others on your team may benefit from building the program up slowly.

1 - Start by asking the user for the magic number. (In future steps, we will change this to have the computer generate a random number, but to get started, we'll just let the user decide what it is.)

Ask the user for a guess.

Using an if statement, determine if the user needs to guess higher or lower next time, or tell them if they guessed it.

At this point, you won't have any loops.

2 - Add a loop that keeps looping as long as the guess does not match the magic number.

At this point, the user should be able to keep playing until they get the correct answer.

3 - Instead of having the user supply the magic number, import the random library and use it to generate a random number from 1 to 100.

Play the game and make sure it works!



Stretch Challenge:

Keep track of how many guesses the user has made and inform them of it at the end of the game.

After the game is over, ask the user if they want to play again. Then, loop back and play the whole game again and continue this loop as long as they keep saying "yes".

"""
# Import libraries

import random

# Loops

while True:
    print("\nTry to guess my number from 1-10\n")

    # Get user input with validation
    while True:
        user_input = input("What is your number guess? ")
        
        # Check if the input is a valid integer
        if user_input.isdigit():
            user_number = int(user_input)
            
            # Check if the integer is within the specified range
            if 1 <= user_number <= 10:
                break  # Exit the loop if the input is valid
            else:
                print("Invalid input. Please enter a number between 1 and 10.")
        else:
            print("Invalid input. Please enter a valid integer.")

    # Variables
    number = random.randint(1, 10)
    guesses = 1  # Initialize the number of guesses

    # Sentences
    
    while user_number != number:
        if user_number > number:
            print("\nTry lower.\n")
        else:
            print("\nTry higher.\n")
        
        user_input = input("What is your number guess? ")
        
        # Validate the new input

        while True:
            if user_input.isdigit():
                user_number = int(user_input)
                if 1 <= user_number <= 10:
                    break
                else:
                    print("Invalid input. Please enter a number between 1 and 10.")
            else:
                print("Invalid input. Please enter a valid integer.")

        guesses += 1  # Increment the number of guesses

    print(f"Congratulations! You guessed the correct number {number} in {guesses} guesses.")

    play_again = input("Do you want to play again? (yes/no) ").lower()
    if play_again != 'yes':
        print("Thanks for playing. Goodbye!")
        break

# End