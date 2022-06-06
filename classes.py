#!usr/bin/python

##########################
#      Classes
#      Name: Mercy Muiruri
#      
###########################

class Robot:
    def __init__(self,name,color,weight) :
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is " + self.name)

# r1 = Robot()
# r1.name = "Tom"
# r1.color =  "red"
# r1.weight = 30

# r2 = Robot()
# r2.name = "Jerry"
# r2.color = "blue"
# r2.weight = 40

r1 = Robot("tom","red",30)
r2 = Robot("Jerry","blue",40)

r1.introduce_self()
r2.introduce_self()

class Person:
    def __init__(self,age,weight,height,name,catch_phrase):
        self.age = age
        self.weight = weight
        self.height = height
        self.name = name
        self.catch_phrase = catch_phrase

user = Person(23,40,123,"Alex","Just do it!")
print(user.catch_phrase)

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def sayHi(self):
        print("The employee's name is ",str(self.name), "and he earns ",str(self.salary))
employee_one = Employee("Jonathan",1000000)
employee_one.sayHi()
employee_two = Employee("Mark",3000000)
employee_two.sayHi()

# class Vehicles:
#     def __init___(self,price,age,color):
#         self.price = price
#         self.age = age
#         self.color = color
#     def aboutTheCar(self):
#         print("This car was bought at ",str(self.price), " and is ",str(self.age), "years old. It is ",str(self.color)," in colour.")
# bugatti = Vehicles(10000,10,"red")

# bugatti.aboutTheCar()