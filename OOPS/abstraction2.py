from abc import ABC, abstractmethod

# craete an abstract base class
class Car(ABC):
    def __init__(self, name, model, price):
        self.brand = name
        self.model = model
        self.price = price
    
    # create abstract method
    @abstractmethod
    def print_description(self):
        print("""The brand of the car is {} and model is {} which costs me {}"""
              .format(self.brand, self.model, self.price))
    
    # create concrete method
    def accelerate(self):
        print("Speed up ............")
        
    def break_applied(self):
        print("Stopped ............")
        
class Hatchback(Car):
    
    def print_description(self):
        print("Brand: {}".format(self.brand))
        print(f"Model: {self.model}")
        print("Price: "+str(self.price))
        
    def sunroof(self):
        print("feature not available")
        
class SUV(Car):
    
    def print_description(self):
        return super().print_description()
    # using inherited method raise an error:
    # TypeError: Can't instantiate abstract class SUV with abstract method print_description
    
    def sunroof(self):
        print("feature available")
        

car_1 = SUV("Maruti", "Alto", 500000)
car_1.print_description()
car_1.accelerate()
car_1.sunroof()