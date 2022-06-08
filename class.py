class Student:
    def __init__(self,name,hobby,fav_food,age):
        self.name = name
        self.hpbby = hobby
        self.fav_food = fav_food
        self.age = age

    def sayHello(self,name):
        print("Hello i am " + self.name.title())

    def run():
        print("Student is running")
# object is an instance of a class 
# object oriented programming
# class - template


first_student = Student("Mercy","Swimming","chapati",18)
second_student = Student("Bob","driving","ugali",40)
print(first_student.name.title())
print("The second student's age is " + str(second_student.age))

#second_student.run()

first_student.sayHello(first_student.name.title())