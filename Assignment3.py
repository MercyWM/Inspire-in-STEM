#!usr/bin/python

# write a program that gets the user input and adds 10,000 to her account if she is between 25 to 30 years
age = input("What is your age?")
gender = input("What gender are you: male/female")
account_balance = 0
if (int(age) > 25) and (int(age) < 30) :
    account_balance= account_balance + 10000
    print("You have received Ksh 10000")
else :
    print("No money available.Kindly look elsewhere.")

