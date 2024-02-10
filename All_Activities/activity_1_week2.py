#Activity 1 Week 2: Using Different Data Types
"""
Author: Martina Toebe

Purpose: Practice using mathematical expressions

"""
#Ask for the age and print it
age = input("How old are you?")
age_next = int(age) + 1
print(f"On your next birthday, you will be {age_next}.")
print()
#Ask for many egg cartoons and print it
egg_cartoons = input("How many egg cartons do you have?")
egg_multiple = int(egg_cartoons) * 12
print(f"You have {egg_multiple} eggs.")
print()
#Ask for many cookies and print it
cookies = input("How many cookies do you have?")
people = input("How many people are there?")
cookies_per_people = int(cookies) // int(people)
print(f"Each person may have {cookies_per_people} cookies.")
print()
# End
