# Single inheritance
class animal:
    def __init__(self, name):
        self.name = name
    
    def eating(self):
        print("EATINGGG")
    
class dog(animal):
    def bark(self):
        print("BARKKK")
        
    def display_var(self):
        print(self.name)
        

# d = dog()
# d.eating()
# d.bark()

# d2 = dog("babydog")
# d2.display_var()


# multilevel inheritance
class person:
    def display(self):
        print("Helloo!! this is person class")

class employee(person):
    @staticmethod
    def printing():
        print("Helloo!! this is employee class")
        
class programmer(employee):
    def show(self):
        print("Hellooo! this is programmer class")
        

# p1 = programmer()
# p1.printing()
# p1.display()
# p1.show()


# multiple inheritance
class land_animal:
    def land(self):
        print("Animal lives on Land")

class water_animal:
    def water(self):
        print("Animal lives in water")
        
class frog(land_animal, water_animal):
    @staticmethod
    def both():
        print("Animal lives on both land and water")
    
    # method overriding
    def water(Self):
        print("Fishes in water")
        
# f1 = frog()
# f1.both()
# f1.water()
# f1.land()


# hierarchy inheritance
class animal:
    def __init__(self, name):
        self.name = name
        
    def speak():
        pass
    
class dog(animal):
    def speak():
        print("dog is barking")
        
class cat(animal):
    def speak():
        print("cat is doing meow")
        

# dog.speak()
# cat.speak()


# hybrid inheritance
class animal:
    def __init__(self, name):
        self.name = name
        
    def speak():
        pass
    
class dog(animal):
    def speak():
        print("dog is barking")
        
class cat(animal):
    def speak():
        print("cat is doing meow")
        
class dog_cat(dog, cat):
    def speak():
        print("cat is doing meow, dog is barking")
    
# dog_cat.speak()

# --------------------------------------------------------
class phone:
    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.__price = price
        

class smartphone(phone):
    pass
    
phone_1 = smartphone("m31", "samsung", "20,000")
print(phone_1.name)