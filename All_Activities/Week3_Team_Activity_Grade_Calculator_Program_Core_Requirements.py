#Week 3 | Team Activity - Grade Calculator Program - Core Requirements
"""
Author: Martina Toebe

Purpose: Write a program that determines the letter grade for a course according to the following scale:

A >= 90

B >= 80

C >= 70

D >= 60

F < 60

"""
# Variables

user_grade_percentage = float(input("\nPlease inform your grade percentage:\n"))

letter = " "
sign = " "
grade_reminder = user_grade_percentage % 10

# Sentences 

if user_grade_percentage >= 90 :
    letter = "A"
elif user_grade_percentage >= 80 :
    letter = "B"
elif user_grade_percentage >= 70 :
    letter = "C"
elif user_grade_percentage >= 60 :
    letter = "D"
else :
    letter = "F"

if letter != "A" and letter != "F" and grade_reminder >= 7 :
    sign = "+"
elif letter != "F" and grade_reminder <= 2 :
    sign = "-" 
else :
    grade_reminder
# Printing the letter grade
print(f"\nYour grade is {letter}{sign}\n")

# Checking if the user passed the course
if user_grade_percentage >= 70:
    print("\nCongratulations, you passed in this term! Keep up the good work on your further studies!\n")
else:
    print("\nUnfortunately, you did not pass in this term. Don't give up, we encourage you to talk to your mentor, who could give you some advice on your further studies.\n")

# End
    
"""
Stretch Challenge: 


1 - Add to your code the ability to include a "+" or "-" next to the letter grade, such as B+ or A-. For each grade, you'll know it is a "+" if the last digit is >= 7. You'll know it is a minus if the last digit is < 3 and otherwise it has no sign.

2 - After your logic to determine the grade letter, add another section to determine the sign. Save this sign into a variable. Then, display both the grade letter and the sign in one print statement.

Hint: To get the last digit, you could divide the number by 10, and get the remainder. You might refer back to the Week 02 preparation material to see the operators and find the one that does division and gives you the remainder.

3 - At this point, don't worry about the exceptional cases of A+, F+, or F-.

Recognize that there is no A+ grade, only A and A-. Add some additional logic to your program to detect this case and handle it correctly.

Similarly, recognize that there is no F+ or F- grades, only F. Add additional logic to your program to detect these cases and handle them correctly.

"""