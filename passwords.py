#!usr/bin/python

#########################
#      Passwords Generator
#      Name: Mercy Muiruri
#      
###########################



import random
num_password = int(input("What is the number of passwords you want to generate?"))
print(num_password)
len_password = int(input("What is the length of your password?"))
print(len_password)
character = "Laura Rege"

#print here are your passwords

for passwords in range (num_password):
    passwords = ""
for c in range(len_password): 
    passwords += random.choice(character)
print(passwords)

# password generator using classes
import random
character = 12356
num_of_passwords = int(input("Enter the number of passwords you want"))
length_of_passwords = int(input("Enter the length of the password"))
class Passwords:
    def __init__(self,account):
        self.account =  account
user = Passwords(input("Enter your email address"))
print("Your new password is:")
for passwords in range(num_of_passwords):
    passwords = " "
for c in range(length_of_passwords):
    passwords = passwords + random.choice(character)
    print(passwords)
