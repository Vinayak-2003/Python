# class dog:
#     def sound(self):
#         print("bow bow")
        
# class cat:
#     def sound(self):
#         print("meow")
        
# def makeSound(animaltype):
#     animaltype.sound()
    
# cat1 = cat()
# dog1 = dog()
# makeSound(cat1)
# makeSound(dog1) 


#------------------------------------------
#python inbuilt polymorphism
print(len("HELLOOO"))
print(len([21,43,75]))


# user defined polymorphism
def add(x, y, z=2):
    return x+y+z

print(add(2,3))
print(add(2,3,4))


# polymorphism in class methods
class India():
    def capital(self):
        print("New Delhi is the capital of India.")
 
    def language(self):
        print("Hindi is the most widely spoken language of India.")
 
    def type(self):
        print("India is a developing country.")
 
class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")
 
    def language(self):
        print("English is the primary language of USA.")
 
    def type(self):
        print("USA is a developed country.")
 
obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()

    
# polymorphism in inheritance method overriding
class Bird:
  def intro(self):
    print("There are many types of birds.")
     
  def flight(self):
    print("Most of the birds can fly but some cannot.")
   
class sparrow(Bird):
  def flight(self):
    print("Sparrows can fly.")
     
class ostrich(Bird):
  def flight(self):
    print("Ostriches cannot fly.")
     
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()
 
obj_bird.intro()
obj_bird.flight()
 
obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()


# method overloading polymorphism
class summ:
    def add(a,b):
        print(f"{a}+{b}={a+b}")
        
    def add(a,b,c):
        print(f"{a}+{b}+{c}={a+b+c}")
        
a = summ()
a.add(2,6)