#Project 02: Meal Price Calculator
"""
Author: Martina Toebe

Purpose: Practice using mathematical expressions

"""
#Import libraries
import math

# Meals price questions
price_child = float(input("What is the price of a child's meal?"))
price_adult = float(input("What is the price of an adult's meal?"))
children_there = int(input("How many children are there?"))
adults_there = int(input("How many adults are there?"))
subtotal = (price_child * children_there) + (price_adult * adults_there)

print()
print(f"Subtotal: ${subtotal:.2f}")
print()

# Tax questions
tax_rate = int(input("What is the sales tax rate?"))
sales_tax = (tax_rate / 100) * subtotal
total = subtotal + sales_tax
print()
print(f"Sales Tax: ${sales_tax:.2f}")
print(f"Total: ${total:.2f}")
print()

# Payment Amount
payment_amount = float(input("What is the payment amount?"))
change = payment_amount - total
print()
print(f"Change: ${change:.2f}")
print()

# End