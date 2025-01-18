# Find the Kth Largest Element in an Array
# Input: A list of integers and an integer k.
# Output: The kth largest element in the list.

list1 = [2,5,1,7,4,9,13,11,15,3,11,13,4,7,9]
k = 5

for n in range(0, len(list1), 1):
    swapped = False
    for i in range(len(list1)-1):
        if list1[i]>list1[i+1]:
            temp = list1[i+1]
            list1[i+1] = list1[i]
            list1[i] = temp
            swapped = True

    if not swapped:
        break

# print(list1[len(list1)-k])
list_set = set(list1)
list1 = list(list_set)
print(list1)
print(list1[len(list1)-k])
        
        

# list1.sort(reverse=True)
# print(list1)
# print(list1[k-1])

# def kth_largest(list1, k):
#     max_element = -99
#     min_element = 999999
#     for i in list1:
#         if i>max_element:
#             max_element = i
            
#         if i<min_element:
#             min_element = i
            
#     count_arr = [0] * (max_element-min_element+1)

#     for num in list1:
#         count_arr[num-min_element] += 1
        
#     remaining = k
#     for cnt in range(len(count_arr)-1, -1, -1):
#         remaining -= count_arr[cnt]
#         if remaining == 0:
#             return cnt+min_element
        
# kth_large = kth_largest(list1, k)
# print(kth_large)