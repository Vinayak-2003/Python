# def generators():
#     yield(7)
#     yield("Hello")
#     yield(True)
#     # return "False"
    
# for val in generators():
#     print(val)
#     print(type(val))
    
# x = generators()
# print(next(x))
# print(next(x))



# ------------------------------ #
def func_generate(n):
    print("Hello")
    i = 0
    while i < n:
        # print(i)
        yield i
        i += 1
    print("Done")
    
gen = func_generate(5)
for x in gen:
    print(x)
    

# def func(n):
#     i = 0
#     while i<n:
#         print(i)
#         i+=1

# func(5)