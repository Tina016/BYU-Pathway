#Week 6 | Team Activity - Human Resources System

"""
Author: Martina Toebe

Purpose: Write a program to iterate through each line of this file, gather the information from each field and display or take certain actions depending on the data. 

"""

hr_file = open("hr_system.txt")

with open("hr_system.txt") as hr_file:
    for line in hr_file:
        line = line.strip()
        break_line = line.split()

        name = break_line[0]
        id_number = break_line[1]
        job_title = break_line[2]
        salary = break_line[3]
        
        # Convert salary to floating-point
        salary_float = float(salary)
        # Format salary to 2 decimal
        salary_decimal = f"{salary_float:.2f}"

        # Print Core Requirements
        print(f"Name: {name}, Title: {job_title}") 
        # Print Strech Challenge
        print(f"{name} ({id_number}), {job_title} - ${salary_decimal}")