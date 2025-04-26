# # class method
# from datetime import date

# class Student:
#     school_name = "alpha school"
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
        
#     @classmethod
#     def calculate_age(cls, name, birth_year):
#         return cls(name, date.today().year-birth_year)
    
#     def school(cls):
#         print("school name is", cls.school_name)
        
#     def change_school(cls, new_school_name):
#         cls.school_name = new_school_name
    
#     def show(self):
#         print(f"{self.name}'s age is {self.age} studying in {Student.change_school}")
        
# student_1 = Student("vinayak", 20)
# student_1.show()

# student_2 = Student.calculate_age("vinayak", 2003)
# student_2.show()

# student_2.school()





import datetime

class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first+last+"@gmail.com"
        self.pay = pay
        
        Employee.num_of_emps += 1
        
    def fullname(self):
        return self.first + " " + self.last
    
    @classmethod
    def set_raise_amnt(cls, amount):
        cls.raise_amount = amount
        
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
       
# emp1 = Employee("vinayak", "kanchan", 10000)
# emp2 = Employee("naman", "gupta", 10000)
 
# emp1.set_raise_amnt(1.07)
# print(emp1.raise_amount)
# print(emp2.raise_amount)
# print(Employee.raise_amount)
# Employee.raise_amount = 1.05
# print(emp1.raise_amount)
# print(emp2.raise_amount)
# print(Employee.raise_amount)

my_date = datetime.date(2024,12,26)

print(Employee.is_workday(my_date))

# print(Employee.num_of_emps)
# print(Employee.raise_amount)
# print(emp1.fullname())