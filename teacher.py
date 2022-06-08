

class Teacher:
    def __init__(self,name,tsc_number,subject,salary):
        self.name = name
        self.tsc_number = tsc_number
        self.subject = subject
        self.salary = salary

    def print_teacher_name(self,name):
        print(self.name)

    def increment_salary(self,salary):
        self.salary += 10000
        return self.salary

    def get_subject(self,name):
        return self.subject

#self,name,tsc_number,subject,salary
teacher_one = Teacher("Mary",1294657,"Chemistry",200000)

teacher_one.print_teacher_name(teacher_one.name)

print(str(teacher_one.increment_salary(teacher_one.salary)))

print("Teacher one's new salary is "+ str(teacher_one.salary))
