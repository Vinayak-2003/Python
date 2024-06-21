st = "bxsu sjc nxis"
iter_st = iter(st)

print(next(iter_st))
print(next(iter_st))


def topTen():
    yield 1
    yield 3
    yield 5
    yield 7

val = topTen()
    
print(next(val))
print(next(val))
print(next(val))
print(val.__next__())