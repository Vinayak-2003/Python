def myFun(data, email):
    print("My name is " + data)
    print("My email is " + email)
    
# myFun("Vinayak", "vinaykkanchan03@gmail.com")

# -----------*args--------------
def myFun2(*data):
    print("My name is " + data[0])
    print("My email is " + data[1])
    
# myFun2("Vinayak", "vinaykkanchan03@gmail.com")

# -----------Keywords args--------------
def myFun2(a, b):
    print("My name is " + a)
    print("My email is " + b)
    
# myFun2(a = "Vinayak", b = "vinaykkanchan03@gmail.com")

# -----------**kwargs--------------
def myFun2(**data):
    print("My name is " + data["name"])
    print("My email is " + data["email"])
    
# myFun2(name = "Vinayak", email = "vinaykkanchan03@gmail.com")


# -----------Default parameter value--------------
def myName(name="VInayak"):
    print("My name is " + name)

# myName("Naman")
# myName()


# -----------Passing a List--------------
def basket(fruits):
    print(fruits[0])

# basket(['apple', 'mango', 'cherry'])
# basket({'apple', 'mango', 'cherry'})
# basket(('apple', 'mango', 'cherry'))


# -----------Recurssion--------------
def recursion(k):
    if(k>0):
        print('aaaaaaaaaa')
        result = k + recursion(k-1)
        print(result)
    else:
        print('bbbbbbbbbbbbb')
        result = 0
    print('cccccccccccccc')
    return result


# recursion(6)


# -----------lambda function--------------
x = lambda a: a+10
# print(x(5))

y = lambda p,q,r: p+q+r
# print(y(2,3,4))

def myfun(n):
    return lambda a: a*n

myDubler = myfun(2)

print(myDubler(11))