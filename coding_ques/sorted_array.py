list1 = [23, 3, 2, 7, 5, 43, 98, 54]
list2 = [1,2,3,4,5,6,7]
flag = 1
for i in range(0, len(list2)-1):
    if list2[i] <= list2[i+1]:
        continue
    else:
        flag = 0
        break
    
if flag == 1:
    print("Sorted")
else:
    print("Not sorted")