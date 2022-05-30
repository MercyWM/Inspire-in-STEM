#!usr/bin/python

#########################
#      WHILE LOOPS
#      Name: Mercy Muiruri
#      Date: 26/5/22 
###########################

print(range(0,20))
for number in range(0,20):
    print(number)
    
# print a list of even and odd numbers
for number in range(0,20): # even numbers
    if (number%2):
        print(number-1)

for number in range(0,20): #even numbers
    if(number%2 == 0):
        print(number)


for number in range(0,20): #odd numbers
    if(number%2 == 1):
        print(number)

# sum of all even numbers between zero and twenty
sum_of_numbers = 0         
for number in range(0,20):
    if(number%2 == 0):
        sum_of_numbers = sum_of_numbers + number
print(sum_of_numbers)

# product of all odd numbers from zero to twenty
product = 1                # initial product is one
for number in range(0,20): # for each number from 1 to 10
    if(number%2 == 1):     # if the number is not divisible by two (odd) 
        product = product*number #product at that point is the previous product multiplied by the number at that point e.g 1*3=3then 3 is then 3 is the new initial product so does 3*5=15 and it continues..
print(product)              # print the final product

#get the factorial of six (6!)[6*5*4*3*2*1]
product = 1
for number in range(2,7):
    product = product*(number-1)
print(product)
# factorial of 9
product = 1
for number in range(2,10):
    product = product*(number-1)
print(product)

# # operators
# < less than
# <= less than or equal to
# > greater than
# >= greater than oir equal to
# == equals to
# != not equal to
# = assigning a value to something
# %(modulus) it shows the remainder of something

# while loops # print a list of even numbers using while loops
num = 0
while num < 10:
    if(num%2 == 0):
        print(num)
    num = num + 1
      
        
