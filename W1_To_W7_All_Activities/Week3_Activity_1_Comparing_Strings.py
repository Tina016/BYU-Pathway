#Week 3 | Activity 1 - Comparing Strings
"""
Author: Martina Toebe

Purpose: Practice writing programs that compare strings and numbers.

"""
# Inputs
print("\nWelcome to the Ativity 1 - Week 3!\nTo start, please provide two integers on the following questions:\n")
a = input("\nInteger A: \n")
b = input("\nInteger B: \n")
                      
#Sentences
if a > b :
    print("\nThe first number is greater\n")
else : ("\nThe first number is not greater\n")
if a == b :
    print("\nThe numbers are equal\n")
else : ("\nThe numbers are not equal\n")
if b > a :
    print("\nThe second number is greater\n")
else : ("\nThe second number is not greater\n")  
print()

#new input
animal = input("\nWhat is your favorite animal?")

#Sentences
if animal.lower() == "bear":
    print("That's my favorite animal too!")
else:
    print("That one is not my favorite.")
"""
-- Comparing Numbers

Write a program that asks the user for two integers.

Then, write three separate if/else statements as follows:

If the first number is greater than the second, print "The first number is greater". Otherwise, print "The first number is not greater".

If the two numbers are equal print "The numbers are equal". Otherwise, print "The numbers are not equal".

If the second number is greater than the first, print "The second number is greater". Otherwise, print "The second number is not greater".

Check to see if the user's favorite animal is the same as your favorite animal (meaning you, the programmer). If it is, print "That's my favorite animal too!" If it's not, print "That one is not my favorite." Verify that it works regardless of the capitalization.

-- Testing Procedure

Verify that your program works correctly by following each step in this testing procedure:

Test the first part of your program with pairs of numbers where the first is greater and also where the second is greater. Verify that all three values that are printed are correct.

Test it with two numbers that are equal. Verify that all three values that are printed are correct.

Test the second part of your program with an animal that is different. Verify that the correct message is shown.

Test it with an animal that is the same. Verify that the correct message is shown.

Test it with an animal that is the same, but using different capitalization. Verify that it still matches, even with different capitalization.
"""
