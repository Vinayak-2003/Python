# * = unpacks
# ** = packs

def add(a,b):
    return a+b

values = (1,2)
print(add(*values))

values = {"a":1, "b":2}
print(add(**values))



# lambda function
ans = lambda x,y: print(x+y)
ans = lambda x,y: print(x+y) if x<y else print(x-y)
ans(5,3)