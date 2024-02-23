#Week 5 | Activity 2 - Lists

"""
Author: Martina Toebe

Purpose: Practice using lists and list indexes.

"""
# List to store names
shopping_list = []


print("\nPlease enter the items of the shopping list (type: quit to finish):")
# Get user input
while True:
    shopping_input = input("Item: ")
    if shopping_input == "quit":
        break  # Exit the loop
    else:
        # Append the valid input to the list
        shopping_list.append(shopping_input)

# Print the shopping list
print("\nThe shopping list is:")
for item in shopping_list:
    print(item)

# Print the shopping list with indexes
print("\nThe shopping list with indexes is:")
for i, item in enumerate(shopping_list):
    print(f"{i}. {item}")

# Change an item
change_index = int(input("\nWhich item would you like to change? "))
new_item = input("What is the new item? ")
shopping_list[change_index] = new_item

# Print the updated shopping list with indexes
print("\nThe shopping list with indexes is:")
for i, item in enumerate(shopping_list):
    print(f"{i}. {item}")

# End