#!usr/bin/python

#########################
#      Passwords Generator
#      Name: Mercy Muiruri
#      
###########################

import random

print("Welcome to our Password generator😊")
char ="Marley@7345"
num_pass = int(input("What number of passwords would you like to generate? "))
len_pass = int(input("Enter your preferred password length: "))
print("\n Here are your passwords! ")

for pwd in range(num_pass):
    password =random.choice(char)
    for c in range (len_pass):
      password+= random.choice(char)
    print(password)