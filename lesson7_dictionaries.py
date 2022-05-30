#!usr/bin/python

# # print the squares of numbers from 1 to 9
print(str(1**1))
print(str(2**2))
print(str(3**3))
print(str(4**4))
print(str(5**5))
print(str(6**6))
print(str(7**7))
print(str(8**8))
print(str(9**9))

fruits = ["apples","lemons","melons","pineapples"]
print(fruits[-1])
fruits[3]= "berries"
print(fruits)

##########################
#      Dictionaries
#      Name: Mercy Muiruri
#      Date: 23/5/22  and 26/5/2022
###########################

# Initializing dictionaries.... dictionaries use curly brackets
student = {"Name":"Mercy","Age":24,"Gender":"Female","Hobby":"Performance"}
print(student["Name"])
print(student["Age"])
print(student["Gender"])
print(student["Hobby"])

# how to add a pair
student["id_No"] = "30999265467"
student["instrument"] = "Piano"
student["club"] = "Rotaract"
print(student)

# # how to initialize a empty dictionary
student = {}
student["favourite_food"] = "chips"
student["home_city"] = "Nairobi"
print(student)

# modifying a value in a dictionary
student["Name"] = "Joe"
student = {"Name":"Mercy","Age":24,"Gender":"Female","Hobby":"Performance"}
student["Name"] = "Joe"
print(student)

# deleting an item
del student ["Age"]
print(student)

# using a for loop in a dictionary
student = {"Name":"Mercy","Age":24,"Gender":"Female","Hobby":"Performance"}
for key,value in student.items():
    print(f"{key}:{value}")

#deleting a value
del student["Age"]
print(student)

# accessing a value
student = {"Name":"Mercy","Age":24,"Gender":"Female","Hobby":"Performance"}
print(student["Gender"])
# print(student["Password"])# the is no such key
print(student.get("Password","The location key is non existent")) # the get method takes two arguments. It looks for that key if it is not there, it prints the second argument.

# how to escape characters 
print("I am \"very\" angry" ) # the slash enables python to escape the commas and print them out and not think of them as another string

# lists inside dictionaries
mary_fav_food = ["beef","chicken","vegetable"]
jane_fav_food = ["rice","ugali","potatoes"]    
fav_food = {
    "mary_fav_food":"beef,chicken,vegetable",
    "jane_fav_food":"rice,ugali,potatoes"}
print(fav_food)

#assignment
person = ["Name":"Mercy Muiruri","Email":"mercywangui895@gmail.com","Password":"Yabo!"]
