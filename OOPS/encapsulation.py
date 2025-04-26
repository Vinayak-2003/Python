class car:
    __maxspeed = 0
    __name = " "
    def __init__(self):
        # self.__updateSoftware()
        self.__maxspeed = 200
        self.__name = "lambo"
        
    def drive(self):
        print("driving")
        print(self.__maxspeed)
        print(self.__name)

    # def __updateSoftware(self):
    #     print("Updating the software")
    
    def setspeed(self, speed):
        self.__maxspeed = speed
        print(self.__maxspeed)
        

# blackCar = car()
# blackCar.drive()
# blackCar.setspeed(100)
# blackCar.__name = "BMW"                 #cannot be changed from outside
# blackCar.drive()
# blackCar.__updateSoftware()           #cannot be accessed from outside
# blackCar._car__updateSoftware()


# ------------------------------------------ #
class Base:
    def __init__(self):
        self.a = "a ------> GeeksforGeeks"
        self._b = "b ------> GeeksforGeeks"
        self.__c = "c ------> GeeksforGeeks"

# Creating a derived class
# class Derived(Base):
#     def __init__(self):

        # Calling constructor of Base class
        # Base.__init__(self)
        
        # print("Calling public member of base class: ")
        # print(self.a)
        # print("Calling protected member of base class: ")
        # print(self._b)
        # print("Calling private member of base class: ")
        # print(self.__c)


# Driver code
# obj1 = Derived()
# print(obj1.__c)



# ------------------------------------------ #
# reason for not proper encapsultion

class Person:
    def __init__(self, name, password):
        self._name = name
        self.__password = password
        
    def get_password(self):
        return self.__password
    
    def set_password(self, new_password):
        self.__password = new_password
        
    def information(self):
        return f"my name is {self._name} and my password is {self.__password}"
    

person_1 = Person("vinayak", "hello")
print(person_1.information())

person_1._name = "kjaxkajsak"
print(person_1.information())

person_1.__password = "wrwyiryerui"
print(person_1.information())

person_1._Person__password = "kxzjkxaxxa"
print(person_1.information())

# print(person_1.get_password())
# person_1.set_password("1234567898765432")
# print(person_1.get_password())