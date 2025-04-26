# Find the Maximum Product of Two Integers
# Given an array, find the maximum product of two distinct elements.
# Example: [3, 5, -2, 8, -1] → 40 (from 5 * 8)

list1 = [3, 5, -2, 8, -1]
max_prod = 1

for i in range(0, len(list1)):
    prod = 1
    for j in range(0, len(list1)):
        if i == j:
            pass
        else:
            prod = list1[i] * list1[j]
        
        if prod > max_prod:
            max_prod = prod

print(max_prod)