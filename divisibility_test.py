#!usr/bin/python

#########################
#      Divisibilty Tests
#      Name: Mercy Muiruri
#      Date: 30/5/22 
##########################

# print a list of even numbers
number = 0
while number<10:
    if (number%2 == 0):
        print(number)
    number += 1

# wite a program to check if a number is divisible by 5 or 7
number = int(input("Enter the number :"))
if number%5 ==0 and number%7== 0:
    print(f"The number {number} is divisible by both five and seven")
else:
    print("This number is not divisible by five nor seven")