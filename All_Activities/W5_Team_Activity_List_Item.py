#Week 5 | Team Activity - Lists of Numbers

"""
Author: Martina Toebe

Purpose: Ask the user for a series of numbers, and append each one to a list. 

"""

print("\nEnter a list of numbers, type 0 when finished.\n")

# List to store inputs
user_inputs = []

# Get user input with validation
while True:
    user_input = int(input("\nEnter number: "))
        
    # Check if the integer is greater than zero or equal to
    if user_input == 0:
        break  # Exit the loop if the input is valid
    elif user_input < 0:
        print("Invalid input. Please enter a number greater than or equal to 0.")
    else:
        # Append the valid input to the list
        user_inputs.append(user_input)

# Sum the inputs
sum_inputs = sum(user_inputs)

# The average of the inputs
average_inputs = sum_inputs / len(user_inputs)

# The largest numbers of the inputs
largest_inputs = max(user_inputs)

# The smalest number of the inputs
smalest_inputs = min(user_inputs)

# The sorted list of the inputs
sorted_inputs = sorted(user_inputs)

# Prints
print("User inputs:", user_inputs)
print(f"The sum is: {sum_inputs}")
print(f"The average is: {average_inputs}")
print(f"The largest number is: {largest_inputs}")
print(f"The smalest number is: {smalest_inputs}")
print(f"The sorted list is:")
for user_inputs in sorted_inputs:
    print(user_inputs)

# End









