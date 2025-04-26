# if elif else
a = 10
b = 11

if a>b:
    print("a is greater than b")
elif a==b:
    print("a is equal to b")
else:
    print("b is greater than a")
    
    

# Short hand if & if else
c = 11
d = 12
e = 14
if c<d: print(str(c) + " is smaller than " + str(d))

# ternary operator or conditional expression
print(str(c) + " is smaller than " + str(d)) if c<d else print(str(d) + " is smaller than " + str(c))

# multiple else ternary operator
print("C") if c<d else print("D") if d<c else print("==")


if c<d and c<e: print(str(c) + " is smallest")
elif d<c and d<e: print(str(d) + " is smallest")
else: print(str(e) + " is smallest")


if c<d or d>e: print(f'{c} is smalller than {d} and is greater than {e}')
elif c<d or d<e: print(f'{c} is smaller than {d} and is smaller than {e}')

if not c<d:
    print("c is smaller than d")
else: print("d is smaller than c")