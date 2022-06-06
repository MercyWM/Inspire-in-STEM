#!usr/bin/python

##########################
#      Functions
#      Name: Mercy Muiruri
#      
###########################

## functions are blocks of code
# initiaLIZE THE FUNCTION 
def sum_nums(f_num,s_num): # f_num and s_num are parameters
    sum_nums = f_num +s_num
    print(sum_nums)

# calling the function
sum_nums(4,3)

# y = mx +c
# y = ax^2 + bx + c
# linear equation
def linear_equation(m,x,c):
    y = (m*x) + c
    return y

# quadratic equation
def quadratic_equation(a,b,c,x):
    y = (a*x**2) + (b*x) + c
    return y

# all blocks of code are run together
x = 2
print(x) # possible
print("x is :" + str(x))

print("x is :" + str(x) + "  y is :" + str(linear_equation(2,x,7)))

# create a table showing values of x and their corresponding values of y in a quadratic equation
# y = ax**2 + bx + c
def quadratic_equation(a,b,c,x):
    y = (a*x**2) + (b*x) + c
    return y
a = int(input("Enter the co-efficient of the first term"))
b = int(input("Enter the co-effiecient of the second term"))
c = int(input("Enter the constant term"))

print("===========")
print("x \t y")
print("===========")
for x in range(1,11):
    print(str(x) + "\t" + str(quadratic_equation(a,b,c,x)))






    
    