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

for pwd in range(num_pass): # from 0- to 2,
    password = ""            # password is initailized to nothing
    for c in range (len_pass):
      password+= random.choice(char)  #password= nothing plus a random character from the characters list
    print(password)                   # this process is done ten times then another password is generated.

# password = "" 
# for x in range(len_pass):
#   password += random.choice(char)
  
  
# print(password)

