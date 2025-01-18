class Person():
    def __new__(cls, name):
        print(f"creating a new class method: {cls.__name__}")
        obj = object.__new__(cls)
        print(obj)
        print(obj.__dict__)
        # return obj
    
    def __init__(self, name):
        print(f"Initializing a new class object...")
        self.name = name
        print(self.__dict__)
        

person = Person("john")


# -----------------USE of __new__-------------------------
# when you want to tweak the object at creation time
class squareNum(int):
    def __new__(cls, val):
        return super().__new__(cls, val**2)
    
x = squareNum(3)
print("--------->", x)