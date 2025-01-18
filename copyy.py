import copy

# li1 = [1,2,[3,5], 6]
# li2 = copy.copy(li1)
# li3 = copy.deepcopy(li1)

# print("LI1 ID: ", id(li1), "VALUE: ", li1)
# print("LI2 ID: ", id(li2), "VALUE: ", li2)
# print("LI3 ID: ", id(li3), "VALUE: ", li3)

# li3[1] = 100
# li2[1] = 200
# li1[1] = 500
# print("LI1 ID: ", id(li1), "VALUE: ", li1)
# print("LI2 ID: ", id(li2), "VALUE: ", li2)
# print("LI3 ID: ", id(li3), "VALUE: ", li3)

#--------------------------------------------------
lst1 = [1,2,3,4]
# lst2 = lst1
# print(lst1, lst2)

# lst2[2] = 100
# print(lst1, lst2)



#shallow copy
# lst2 = lst1.copy()
# lst2[2] = 100
# print(lst1, lst2)

# lst1 = [1,2,[3,4],5]
# lst2 = lst1.copy()
# lst2[2][0] = 100
# print(lst1, lst2)


#deep copy
lst2 = copy.deepcopy(lst1)
lst2[2] = 100
print(lst1, lst2)

lst1 = [1,2,[3,4],5]
lst2 = copy.deepcopy(lst1)
lst2[2][0] = 100
print(lst1, lst2)