#!usr/bin/python

#########################
#      LISTS 2
#      Name: Mercy Muiruri
#      Date: 23/5/22 
###########################

squares = [] # empty list
for number in range(0,10): # for each number in the range of 0 to 9
    square = number**2     # you do each number power two
    squares.append(square) # to the empty list add the squares
print(squares)             # print out the list with squares

cubes = []
for number in range(0,10):
    cube = number**3
    cubes.append(cube)
print(cubes)

# print out the sum of numbers between 1 and 100
sum = 0                     # the sum is initially zero
for number in range(0,100): # for each number in the range of 0 to 100
    sum = sum + number      # the new sum is the initial sum(0) plus the number(1,2,3..) like 0+1=2...
print(sum) # print out the final sum

###################################
# if statements

age = 12
if age >= 18:
    print("Driving license approved")
else :
    print("DRIVING LICENSE DENIED TO MINORS")

# write a program that gets the user input and adds 10,000 to her account if she is between 25 to 30 years
