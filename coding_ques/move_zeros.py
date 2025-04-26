# Move Zeros to the End
# Move all zeros in an array to the end while keeping the order of other elements.
# Example: [0, 1, 0, 3, 12] → [1, 3, 12, 0, 0]

# l = [0, 1, 0, 3, 12]
l = [3,0,6,1,0,0,0,5]

# n = len(l)
# i = 0
# j = n-1
# while i<=j:
    
#     if l[i] == 0:
#         l[j], l[i] = l[i], l[j]
#         j -= 1
#         i += 1
#     elif l[j] == 0:
#         j -= 1
#     else:
#         i += 1

# ----- maintaining order ------
# i=0
# j=0
# while i<n and j<n:
#     if l[j] != 0:
#         l[i], l[j] = l[j], l[i]
#         i += 1
#         j += 1
#     elif l[j] == 0:
#         j += 1

# print(l)


# Question. Move all zeros to the end while keeping the order of the elemets same
# Input:
# nums = [3,0,6,1,0,5]
# Output:
# nums = [3,6,1,5,0,0]

 

nums = [5,0,6,1,0,5]

# solution 1
n = len(nums)
ans = []
for i in nums:
    if i != 0:
        ans.append(i)
        
m = len(ans)
for i in range(0,n-m):
    ans.append(0)
    
print(ans)

# solution 2
i,j=0,0
n=len(nums)
while i<n and j<n:
    if nums[j] == 0:
        j += 1
    else:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j += 1

print(nums)