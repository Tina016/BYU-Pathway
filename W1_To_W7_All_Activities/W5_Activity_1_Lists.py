#Week 5 | Activity 1 - Lists

"""
Author: Martina Toebe

Purpose: Practice creating lists, adding to them, and iterating through them.

"""

# List to store names
user_inputs = []

# Get user input
while True:
    user_input = input("Type the name of a friend: ")
    if user_input == "end":
        break  # Exit the loop
    else:
        # Append the valid input to the list
        user_inputs.append(user_input)

# Print the header outside the loop
print("Your friends are:")

# Print each friend's name below the header
for user_input in user_inputs:
    print(user_input)

# End