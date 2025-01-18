class Employee:
    noOfEmp = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
        Employee.noOfEmp += 1
            
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = (self.pay * Employee.raise_amount)

# print(Employee.noOfEmp)
        
emp_1 = Employee("Rohan", "Yadav", 70000)
emp_2 = Employee("Smriti", "Yadav", 60000)

# print(emp_1.first)
# print(emp_2.email)
# print(emp_1.fullname())
# print(Employee.fullname(emp_2))

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)
# print(emp_1.raise_amount)
# print(Employee.raise_amount)
# print(emp_2.raise_amount)
# print(emp_2.__dict__)
# print(Employee.__dict__)
# emp_2.raise_amount = 1.05
# print(emp_1.raise_amount)
# print(Employee.raise_amount)
# print(emp_2.raise_amount)
# print(Employee.noOfEmp)


# --------------------------------------------------------------- #
class animal:
    def cat(self):
        print("CCCCCAAAAAAAAAAATTTTTTTTT")
        print(self)
        print(type(self))
        
# c1 = animal()
# c1.cat()
# print(type(animal))
# print(type(animal.cat))



# --------------------------------------------------------------- #
class students:
    
    university = "MANIPAL UNIVERSITY JAIPUR"
    
    def __init__(self, m1, m2, m3):
        # instance variables
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    
    # Instance method because it works with the instance object variables
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    
    # Accessor methods -> fetch the values
    def get_m1(self):
        return self.m1
    
    # Mutator methods -> assign the value
    def set_m1(self, val):
        self.m1 = val
          
    @classmethod   
    def get_clg(cls):
        return cls.university
    
    @staticmethod
    def info():
        print("This is a student class .......")
    
    
    

s1 = students(32,54,66)
s2 = students(52,72,22)

print(s1.avg())
print(s2.get_m1())
s2.set_m1(55)
print(s2.get_m1())

print(students.get_clg())
students.info()