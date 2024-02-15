#Week 3 | Activity 2 - Qualifying for a loan
"""
Author: Martina Toebe

Purpose: Implement a simplistic system to determine if a user can qualify for a loan

"""
# Inputs
print("\nWelcome to the Loan Easy!\nTo start your request, please answear the following questions for our analysis:\n")
name = input("\nPlease provide your first and last name: \n")
print(f"\nThank you for providing the information above {name}!\nNow, we will be asking you some questions to check if you qualifies for the loan.\nTo do so, please rate from 1 to 10 on the following: \n")
large_loan = int(input("How large is the loan?"))
credit_history = int(input("How good is your credit history?"))
income = int(input("How high is your income?"))
down_payment = int(input("How large is your down payment?"))
print(f"\n{name} we are almost there!\nPlease wait a minute until we check your qualifications.\n")                        
#Sentences
if large_loan >= 5 and credit_history >= 7 and income >= 7 or down_payment >= 5:
    print(f"\n{name}, thank you for choosing Easy Loan!\nYor loan has been analyzed and we are pleased to inform you that it is already approved!\nThe money will be available for you in 10 minutes.") 
elif large_loan < 5 and income >= 7 or down_payment >= 7 :
    print(f"\n{name}, thank you for choosing Easy Loan!\nYor loan has been analyzed and we are pleased to inform you that it is already approved!\nThe money will be available for you in 10 minutes.")    
elif large_loan < 5 and income >= 4 and down_payment >= 4 :
    print(f"\n{name}, thank you for choosing Easy Loan!\nYor loan has been analyzed and we are pleased to inform you that it is already approved!\nThe money will be available for you in 10 minutes.")
elif large_loan < 5 and credit_history < 4 :
    print(f"\n{name}, thank you for choosing Easy Loan!\nYour loan has been analyzed and unfortunutaly, at this time we could not approve it. But you can request a new analysis in next 30 days.")
else : 
    print(f"\n{name}, thank you for choosing Easy Loan!\nYour loan has been analyzed and unfortunutaly, at this time we could not approve it. But you can request a new analysis in next 30 days.")

print()
