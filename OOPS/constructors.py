class Person:
    clg = "Manipal University Jaipur"           #class variable

    def __init__(self, name, occ):
        print("HELLOOO")
        self.name = name                #instance variable
        self.occ = occ                  #instance variable

    def info(self):
        print(f"{self.name} is a {self.occ} from {self.clg}")
        
    def display(x):
        print("BYEE")
    
    @staticmethod   
    def static_display():
        print("BYEE BYEE")


a = Person("Vinayak", "Developer")
b = Person("DIvya", "HR")
c = Person("Honey", "Businessman")
a.info()
b.info()
c.info()
a.display()
b.static_display()