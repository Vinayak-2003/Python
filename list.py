myList = ['apple', 'banana', 3, 'apple', "cherry", "orange", "kiwi", True, 1, 2]

# print(myList)
# print(type(myList))
# print(len(myList))

lst = list(('a', 'y', 7))
# print(lst)

singleList = ['Apple']
print(type(singleList))

#--------------Access list items------------------
# List is ordered

# print(myList[0])
# print(myList[2:5])          # 2 included, 5 excluded
# print(myList[-1])
# print(myList[-5:-1])

#if "apple" in myList:
    # print("Yes, apple exist in myList")
    

#--------------change list items / add items------------------
# list is changeable

myList[1] = 'icecream'
myList[1:3] = ['ice', 'cream']
myList[6:] = ['chocolate', 'ice', 'cream']
# print(myList)

myList[1:4] = ['chocolateIceCream']
# print(myList)

myList.insert(2, 'apple')
# print(myList)
# print(len(myList))

myList.append(27)
# print(myList)

x10 = [100, 200, 300]
myList.extend(x10)
# print(myList)


#--------------remove list items------------------
# print(myList)

myList.remove('apple')
myList.pop(2)
myList.pop()
del myList[3]
# del myList
# myList.clear()

# print(myList)


#--------------loop list items------------------
n = len(myList)
# for i in myList:
#     print(i)
    
# for i in range(n):
#     print(myList[i])

# i=0
# while i < n:
#     print(myList[i])
#     i+=1

# [print(x) for x in myList]


#--------------list comprehension------------------
# to add/create a new list from the existing list

# temp = []
# for x in myList:
#     temp.append(x)

temp = [x for x in myList if x!='apple']

newList = [x for x in range(10)]
    
# print(newList)


#--------------sort list items------------------
newList = ['9pineapple', "Cherry", "Orange", "kiwi"]
newList.sort()
newList.sort(reverse = True)
# print(newList)

#customize sort function - based on how close the number is to 50
numList = [100, 54, 29, 73, 87, 11]
def myFun(n):
    return abs(n-50)

# numList.sort(key = myFun)
# print(numList)

newList.reverse()
# print(newList)


#--------------copy list items------------------
#can be modified if original is modified (reference)
cpyList = numList
# print(cpyList)

#cannot be modified if original is modified
copyList = numList.copy()
# print(copyList)

numList[1] = 200
# print(cpyList)
# print(copyList)


#--------------join list items------------------
list1 = [1,2,3]
list2 = ['a', 'b', 'c']

# list3 = list1 + list2
# list1.extend(list2)

for i in list2:
    list1.append(i)
print(list1)