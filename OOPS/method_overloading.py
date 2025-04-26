# class Geometry:
#     def area(self, r):
#         return 3.14*r*r
    
#     def area(self,l,b):
#         return l*b
    
# shape = Geometry()
# print(shape.area(2,2))


# technically method overloading is not allowed but can be applied using the default variables
class Geometry():
    def area(self,a,b=0):
        if b==0:
            print("Circle", 3.14*a*a)
        else:
            print("Rectangle", a*b)
            
shape = Geometry()
shape.area(2)
shape.area(3,4)