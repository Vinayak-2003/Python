# class point:
    
#     def __init__(self, data):
#         self.num = data
        
#     def print_num(self):
#         print(self.num)
#         print(self)
        

# obj = point(100)
# obj.print_num()



# class person:
    
#     def __new__(cls):
#         print("1")
#         return object.__new__(cls)
    
#     def __init__(self):
#         print("2")
#         self.instance_method()
        
#     def instance_method(self):
#         print("3")
#         print("SUCCESS!!")
        

# personObj = person()


class MyClass:
    def __new__(cls, *args, **kwargs):
        print("Creating instance of ", cls)
        instance = super().__new__