class Phone():
    def __init__(self, brand, price, camera):
        self.brand = brand
        self.price = price
        self.camera = camera
        print("inside phone")
        
class smartPhone(Phone):
    def __init__(self, brand, price, camera, os, ram):
        super().__init__(brand, price, camera)
        self.os = os
        self.ram = ram
        print("inside smartphone")        

s = smartPhone("samsung", 20000, "64", "android", 8)
print(s.brand)
print(s.os)