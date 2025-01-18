#1 - assigning function to a variable
def say_hello(name):
    return f"hello {name}"

greet = say_hello

print(greet("vinayak"))


#2 - store function in a data structure
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

calculator = {
    "add": add,
    "sub": sub
}

result = calculator["add"](5,6)
print(result)


#3 - pass function as argument to other function
def mul(a,b):
    return a*b

def calculate(func,x,y):
    return func(x,y)

ans = calculate(mul,7,8)
print(ans)


#4 - return function from other function
def multi_cal(value):
    def multi(n):
        return n*value
    
    return multi

multi_val = multi_cal(6)
print(multi_val(2))


# --------------------Higher order function-----------------------
#5
def func():
    print("---------func---------")
    return 6

def multi_cal(func):
    print("---------multi_cal---------")
    def multi(n):
        print("---------multi---------")
        return n*func()
    
    return multi

multi_val = multi_cal(func)
print(multi_val(7))