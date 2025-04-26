# ----------------------------- log decorator ---------------------------------

def log_decorator(func):
    
    def work_function(*args):
        print(f"executing {func.__name__} with arguments {args}")
        result = func(*args)
        print(f"{func.__name__} returns {result}")
        return result
    
    return work_function

@log_decorator
def add(a,b):
    return a+b

add(6,9)


# ----------------------------- class based decorator ---------------------------------

# class doubleDecorator:
    
#     def __init__(self, func):
#         self.func = func
        
#     def __call__(self, *args, **kwargs):
#         print(f"calling from {self.func.__name__}")
#         result = self.func(*args, **kwargs)
#         print(f"returning {self.func.__name__} with result = {result}")
#         return result*2

# @doubleDecorator
# def add(x,y):
#     return x+y

# print(add(2,3))
# print(add(3,4))


# ----------------------------- class based decorator ---------------------------------

class print_decorator:
    
    def __init__(self, func):
        self.func = func
    
    def __call__(self):
        print("before"+self.func.__name__)
        self.func()
        self.another_function()
        print("after"+self.func.__name__)
        
    def another_function(self):
        print("another before"+self.func.__name__)
        self.func()
        print("another after"+self.func.__name__)


@print_decorator
def hello():
    print("HELLOOO")
    
hello()