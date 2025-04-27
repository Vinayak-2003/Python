x = 10
y = 20
print(id(x))
print(id(y))

y = x
# if id(x) == id(y): print("Same" + str(id(x)))


a = [0]
print(id(a))
print(type(a))