#!usr/bin/python

##########################
#      MAKING A CALCULATOR
#      Name: Mercy Muiruri
#      
###########################

# make a simple calculator

# define the functions
def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

print(""" to add enter 1.
          To subtract enter 2.
          To multiply enter 3.
          To divide enter 4. """)

user_input = int(input("Enter the operation you want"))
if user_input == 1:
    num_1 = int(input("Enter the first number"))
    num_2 = int(input("Enter the second number"))
    answer = add(num_1,num_2)
    print("The sum of the numbers is " + str(answer))

elif user_input == 2:
    num_1 = int(input("Enter the first number"))
    num_2 = int(input("Enter the second number"))
    answer = subtract(num_1,num_2)
    print("The difference of the numbers is " + str(answer))

elif user_input == 3:
    num_1 = int(input("Enter the first number"))
    num_2 = int(input("Enter the second number"))
    answer = multiply(num_1,num_2)
    print("The product of the numbers is " + str(answer))

elif user_input == 4:
    num_1 = int(input("Enter the first number"))
    num_2 = int(input("Enter the second number"))
    answer = divide(num_1,num_2)
    print("The quotient of the numbers is " + str(answer))

print("That's it! All done!")