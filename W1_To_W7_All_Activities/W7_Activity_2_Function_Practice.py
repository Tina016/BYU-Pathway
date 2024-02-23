#Week 7 | Activity 2 - Function Practice (2 of 2)

"""
Author: Martina Toebe

Purpose: Write functions to compute and return the areas of squares, rectangles, and circles. These functions should not display the values directly, but rather should return them, so they could be used in other parts of the program.

"""
#Import libraries
import math

# Function to compute area of a square
def compute_area_square(side_length):
    return compute_area_rectangle(side_length, side_length)

# Function to compute area of a rectangle
def compute_area_rectangle(length, width):
    return length * width

# Function to compute area of a circle
def compute_area_circle(radius):
    return math.pi * radius ** 2

# Loop to ask user for shape and dimensions
while True:
    shape = input("Enter the shape (square, rectangle, circle) or 'quit' to exit: ").lower()
    if shape == 'quit':
        break
    elif shape == 'square':
        side_length = float(input("Enter the side length of the square: "))
        area = compute_area_square(side_length)
    elif shape == 'rectangle':
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = compute_area_rectangle(length, width)
    elif shape == 'circle':
        radius = float(input("Enter the radius of the circle: "))
        area = compute_area_circle(radius)
    else:
        print("Invalid shape entered. Please try again.")
        continue

    print(f"The area of the {shape} is: {area:.2f}")

# End