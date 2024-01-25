#Week 2 | Team Activity - Areas of Shapes
"""
Author: Martina Toebe

Purpose: Practice using mathematical expressions

"""
#Import libraries
import math

# Square calculation questions - Square—The area is the length of a side squared.
square_lenght = float(input("What is the length of a side of the square?"))
square_area = square_lenght * square_lenght
print()
print(f"The area of the square is: {square_area:.2f}")
print()

# Rectangle calculation questions - Rectangle—The area is the length multiplied by the width.
rectangle_lenght = float(input("What is the length of rectangle?"))
rectangle_width = float(input("What is the width of the rectangle?"))
rectangle_area = rectangle_lenght * rectangle_width
print()
print(f"The area of the rectangle is: {rectangle_area:.2f}")
print()

# Circle calculation questions - Circle—The area is Pi (you can use 3.14) multiplied by the radius squared.
circle_radius = float(input("What is the radius of the circle?"))
circle_area = math.pi * circle_radius * circle_radius
print()
print(f"The area of the circle is: {circle_area:.2f}")
print()

# End





