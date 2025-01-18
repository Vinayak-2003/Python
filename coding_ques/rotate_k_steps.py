# Question. Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# Input:
# nums = [1, 2, 3, 4, 5, 6, 7], k = 3
# Output:
# nums = [5, 6, 7, 1, 2, 3, 4]


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
ans = []

for i in range(0, len(nums)):
    ans[(i+k)%len(nums)] = nums[i]
    
print(ans)