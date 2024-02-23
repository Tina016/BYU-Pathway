#Week 7 | Activity 1 - Functions (1 of 2)

"""
Author: Martina Toebe

Purpose: This program is designed to help you practice writing basic functions.

"""
# Building our 3 functions
def print_regular(message):
    print(message)# Regular message

def print_uppercase(message):
    print(message.upper())# Uppercase message

def print_lowercase(message):
    print(message.lower())# Lowercase message

# Ask for a message
user_message = input("What is your message? ")

# Print messages
print_regular(user_message)
print_uppercase(user_message)
print_lowercase(user_message)
