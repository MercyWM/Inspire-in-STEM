#!usr/bin/python

#########################
#      FUNCTIONS!!!
#      Name: Mercy Muiruri
#      Date: 31/5/22 
###########################

# A function is a block of code that is executed together

# defining a function
# def say_hello():      # the function say_hello is carrying all the following code
#     print("Hello from JKUAT")
#     x = 4
#     y = 7
#     z = x + y
#     print(z)
# say_hello()         # this is calling the function. When the function is called it runs the whole block of code saved in it 

def animal_sounds():
    print("Dogs bark WOF! WOF! \nCats say meow!\nFrogs always croak\nCows go MOO!!")
animal_sounds()

def dogs():
    print("Dogs bark WOF! WOF!")
def cats():
    print("Cats say meow!")
def frogs():
    print("Frogs always croak")
dogs()
cats()
frogs()

###function parameters
# a function to add two numbers
def add_numbers(x,y):    # here you have created a function called add_numbers which adds the parameters x and y
    sum_nums = x+y
    print("The sum of the numbers:", sum_nums)
add_numbers(100,390)
add_numbers(4,5)
add_numbers(30,1990)  # here you call the function add_numbers which you created and now it adds the values in the parameters

# a function that multiplies numbers
def product_numbers(x,y): 
    product_of_numbers = x*y 
    print("the product of the parameters is ",product_of_numbers)
product_numbers(3,45)
product_numbers(24,56)

def print_name(name= "Mercy Muiruri"):
    print(name)
print_name()
print_name("Lonnie")

def get_sum(num1,num2):
    sum_nums= num1 + num2
    return sum_nums
get_sum(7,12)
#####################
#write a function that gets the square of numbers

def  powers(number,power):
     power_nums = number **power
     return power_nums
powers(6,4)

def get_full_name(f_name,s_name):
    full_name = f_name + s_name
    return full_name
get_full_name("Mercy","Muiruri")
#####################################
#returning a dictionary from a function
def create_full_name(first_name,second_name):
    person={'first':first_name,'second':second_name}
    return person
student= create_full_name ("Mercy","Muiruri")
print(student)

#passing a list in a function

def greet_friends(names):
    for name in names:
        msg = " hello! " + name.title() + "!"
        print(msg)
friends = ["Joshua","Alex"]
greet_friends(friends)
