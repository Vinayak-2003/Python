def test_decorator(another_function):
    def execute_another(*args):
        result = another_function(*args)
        print("Result of adding is ", result)
        return result
        
    return execute_another

# @test_decorator
def add(a,b):
    return a+b

# ans = test_decorator(add(5,6))
# print(ans)




class test_iterator:
    def __init__(self, limit):
        self.limit = limit
        
    def __iter__(self):
        self.x = 10
        return self
    
    def __next__(self):
        x = self.x
        
        if x>self.limit:
            raise StopIteration
        
        self.x += 1
        return self.x
    
# for i in test_iterator(13):
#     print(i)

txt = "hello world!!"

# print(txt.capitalize())
# print(txt.casefold())
# print(txt.count("l"))
# print(txt.find("l"))
# print(id(txt))
print(ord('1'))
# print(txt.capitalize())
# print(txt.capitalize())
# print(txt.capitalize())
# print(txt.capitalize())