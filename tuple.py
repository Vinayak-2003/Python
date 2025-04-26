myTuple = ('apple', 'banana', 3, 'apple', "cherry", "orange", "kiwi", True, 1, 2)
# print(myTuple)
# print(len(myTuple))

#single element tuple
singleTuple = ('Apple',)
# print(type(singleTuple))

thisTuple = tuple(('banana', 3, 'apple'))
# print(thisTuple)


#------------------Access tuples-----------------------
# print(myTuple[2])
# print(myTuple[2:5])
# print(myTuple[-1])
# print(myTuple[-4:-1])
# print(myTuple[3:])

# if 'banana' in myTuple:
#     print("Yes, it is present")


#------------------update tuples-----------------------
temp = list(myTuple)
temp[1] = 'strawberry'
temp.append('mango')
temp.insert(2, 10000)
temp.remove('apple')
myTuple = tuple(temp)

# print(myTuple)
# print(type(myTuple))

addTuple = (100, 200, 300)
myTuple += addTuple
# print(myTuple)

# del myTuple
# print(myTuple)


#------------------unpack tuples-----------------------
fruits = ('apple', "cherry", "orange")
# print(fruits)

(*a, c) = fruits
# print(c)
# print(type(c))


#------------------loop tuples-----------------------
# for i in myTuple:
#     print(i)

# for i in range(len(myTuple)):
#     print(myTuple[i])

n = len(myTuple)
i = 0
# while i < n:
#     print(myTuple[i])
#     i+=1


#------------------join tuples-----------------------
tuple1 = ('a', 'b', 'c')
tuple2 = (1, 2, 3, 4)

tuple1 = tuple1 + tuple2

tuple4 = tuple1 * 2
# print(tuple4)
print(tuple4.count('a'))
print(tuple4.index('a'))