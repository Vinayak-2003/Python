mySet = {'apple', 'banana', 3, 'apple', "cherry", "orange", "kiwi", True, 1, 2, 1}

# print(mySet)
# print(len(mySet))
# print(type(mySet))


#--------------------Access sets items-----------------------
# for x in mySet:
#     print(x)

# if 'apple' in mySet:
#     print("Yes, apple is present")

# ----ERROR----
# mySet[1] = 1000
# print(mySet)
# print(mySet[0])


#--------------------Add sets items-----------------------
# mySet.add('orange')

# newSet = {100, 200, 300}
# mySet.update(newSet)

# newSet2 = [700, 800]
mySet.add([700, 800])
# mySet.update(newSet2)
print(mySet)
print(type(mySet))


#--------------------Remove set items-----------------------
# remove and discard can be used to remove the item from set 
# but remove brings an error when the key is not present, but discard will not

# mySet.remove(100000)              
mySet.discard(100000)
# mySet.discard('banana')
# mySet.pop()
# mySet.clear()
# del mySet

# print(mySet)


#--------------------loop set items-----------------------
# for x in mySet:
#     print(x)

# for i in range(len(mySet)):
#     print(mySet[i])
#TypeError: 'set' object is not subscriptable


#--------------------join set items-----------------------
set1 = {'a', 'b', 'c'}
set2 = {1, 2, 3, False}
set5 = {'x', 'y', 'z', 'a', 'b'}
set6 = {100, 200, 300, True, 0}
list1 = [50, 150, 250]

set3 = set1.union(set2)
set4 = set1 | set2
set7 = set3.union(set5, set6)
set8 = set2.union(list1, set5)
set1.update(set2)
set9 = set1.intersection(set5)
set10 = set1 & set5
set1.intersection_update(set5)
set11 = set2 & set6
set12 = set5.difference(set1)
set13 = set5 - set1
set14 = set1.symmetric_difference(set2)
set15 = set1 ^ set2

# print(set15)
# print(type(set15))


#--------------------frozen set-----------------------
t = ('hello', 'my', 'name', 'is', 11)
s = {'hello', 'my', 'name', 'is', 11}
s.add('Vinayak')
# print(type(s))
frznSet = frozenset(s)
# print(type(frznSet))
# print(frznSet)

# frznSet.add('Vinayak')
# print(frznSet)
# AttributeError: 'frozenset' object has no attribute 'add'