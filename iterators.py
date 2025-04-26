# st = "bxsu sjc nxis"
# iter_st = iter(st)

# print(next(iter_st))
# print(next(iter_st))


# def topTen():
#     yield 1
#     yield 3
#     yield 5
#     yield 7

# val = topTen()
    
# print(next(val))
# print(next(val))
# print(next(val))
# print(val.__next__())


# ------------------------------------------------ #
st = "Hello world"
iter_st = iter(st)

print(next(iter_st))
print(next(iter_st))
print(next(iter_st))


# ------------------------------------------------ #
class test:
    def __init__(self, limit):
        self.limit = limit
        print("__init__", self.limit)
        
    def __iter__(self):
        self.x = 10
        print("-----__iter__------", self)
        return self
    
    def __next__(self):
        x = self.x              # 10 11 
        print("__next__", x)
        
        if x > self.limit:
            raise StopIteration
        
        self.x += 1
        return self.x
    
    
for i in test(15):
    print("_________START_______")
    print(i)