def generators():
    yield(7)
    yield("Hello")
    yield(True)
    # return "False"
    
for val in generators():
    print(val)
    print(type(val))
    
x = generators()
print(next(x))
print(next(x))