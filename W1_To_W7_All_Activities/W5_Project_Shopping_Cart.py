#Week 5 | Project - Shopping Cart

"""
Author: Martina Toebe

Purpose: For this project you will create a program that stores a list of products in a shopping cart along with their prices.
The user should have the ability to add items to the list, remove them, and see the total price of the cart.

For the milestone deliverable, you only need to worry about storing a list of the names of the items (not the prices yet), 
and only need to be able to add new items and display the list. Then, for the complete project, you'll add the ability to store the prices, remove items, and compute the total.

Assigment:

1 - Add a new item

2 - Display the contents of the shopping cart

3 - Remove an item (only needed for the final project deliverable)

4 - Compute the total (only needed for the final project deliverable)

5 - Quit

"""

# The Easy Test Shopping is a simple shopping cart application that allows users to add items with prices, display the cart, remove items, compute the total, and quit the program.
# I've added functionality to remove items from the cart using what I learned until now in the course. There are other ways to better achieve the results, but I tried to do it in a simple way.

print("\nWelcome to Easy Test Shopping!\n")

# Lists to store inputs 
list_items = []
list_prices = []

while True:
    print("\nPlease select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

    option = input("\nPlease enter an action: ")

    if option == '1':
        # Ask the user for an item
        item = input("\nWhat item would you like to add?\n")
        list_items.append(item)

        # Validate price input
        valid_price = False
        while not valid_price:
            price_input = input(f"\nWhat is the price of {item}?\n")
            # Check if the input is a float
            if price_input.replace('.', '', 1).isdigit():  # validate if it's a float
                price = float(price_input)
                list_prices.append(price)
                print(f"'{item}' has been added to the cart.")
                valid_price = True
            else:
                print("\nInvalid value. Please enter a valid price.\nEx: 5.00\n")
    
    # Show the cart to the user
    elif option == '2':
        print("\nThe contents of the cart are:")
        for index, (item, price) in enumerate(zip(list_items, list_prices), 1): # enumerating the chart itens
            print(f"{index}. {item} - ${price:.2f}")

    # Remove an item from the list
    elif option == '3':
        remove_option = input("\nWhich item would you like to remove? ")
        
        if remove_option.isdigit():
            remove_index = int(remove_option) - 1
            if 0 <= remove_index < len(list_items):
                removed_item = list_items.pop(remove_index)
                removed_price = list_prices.pop(remove_index)
                print(f"Item removed.")
            else:
                print("Invalid item number.")
        else:
            print("Invalid input. Please enter a valid item number.")

    # Show the total price of all items
    elif option == '4':
        total_prices = sum(list_prices)
        print(f"\nThe total price of all items in the cart is ${total_prices:.2f}")

    # Quit the program
    elif option == '5':
        print("Thank you. Goodbye.")
        break

    else:
        print("Please select a valid option.")

# End