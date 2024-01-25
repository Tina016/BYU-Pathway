#Project 01: Clever Stories
"""
Author: Martina Toebe

Purpose: For this assignment, you will implement a program that asks the user for a series of words and then displays the story 
with the user's words inserted into the appropriate places.

"""
print("Please enter the following:")

print()

# Ask for the series of words
adjective = input("Adjective: ")
animal = input("Animal: ")
verb_1 = input("Verb 1: ")
exclamation = input("Exclamation: ")
verb_2 = input("Verb 2: ")
verb_3 = input("Verb 3: ")
print()
# Print the story with the provided words
print("Your story is:")
print()
print("The other day, I was really in trouble. It all started when I saw a very", adjective, animal, verb_1 , "down the hallway.", exclamation , "!I yelled. But all",
"I could think to do was to", verb_2 , "over and over. Miraculously, that caused it to stop, but not before it tried to", verb_3 , "right in front of my family.")
print()
# End