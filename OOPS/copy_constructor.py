class Employee:
    employees=[]
    def __init__(self,name,hrm):
        self.name=name
        self.hrm=hrm
        self.email=self.generate_email()
        count=1
        # always unique employee name
        original_name = self.name
        for i in Employee.employees:
            if i["name"]==self.name:
                self.__dict__["name"]=original_name+f"{count}"
                count+=1
        Employee.employees.append(self.__dict__)
        
    @classmethod
    def from_employee(cls,other):
        return cls(other.name,other.hrm)
        
    def generate_email(self):
        first_name, last_name = self.name.split()
        return f"{first_name.lower()}.{last_name.lower()}@celebaltech.com"
    
    def __repr__(self):
        return f"Employee(name={self.name}, hrm={self.hrm}, email={self.email})"
    
emp = Employee("Mayank Sharma",4435)
emp3= Employee("Mayank Sharma",187)
emp2= Employee("Sumit Sharma",4384)
emp5= Employee("Vinayak Kanchan",4877)
emp4= Employee("Mayank Sharma",2853)
emp6 = Employee("Sumit Sharma",2384)
emp4= Employee("Mayank Sharma",2553)

print(Employee.employees)