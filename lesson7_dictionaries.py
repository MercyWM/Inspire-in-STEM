# print the squares of numbers from 1 to 9
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
#      Date: 23/5/22 
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

# how to initialize a empty dictionary
student = {}
student["favourite_food"] = "chips"
student["home_city"] = "Nairobi"
print(student)

# modifying the values 
student = {"Name":"Mercy","Age":24,"Gender":"Female","Hobby":"Performance"}
student["Name"] = "Joe"
print(student)

# deleting a value
del student["Age"]
print(student)