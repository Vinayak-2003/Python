# Given an array arr of positive integers. Reverse every sub-array group of size k.
# Note: If at any instance, k is greater or equal to the array size, then reverse the entire array.
# You shouldn't return any array, modify the given array in place.

# Examples:
# Input: arr[] = [1, 2, 3, 4, 5], k = 3
# Output: [3, 2, 1, 5, 4]
# Explanation: First group consists of elements 1, 2, 3. Second group consists of 4,5.
# 
# Input: arr[] = [5, 6, 8, 9], k = 5
# Output: [9, 8, 6, 5]
# Explnation: Since k is greater than array 

nums = [1, 2, 3, 4, 5]
k = 3

nums = [5, 6, 8, 9]
k = 4

n = len(nums)
def reverse(nums, start , end):
    while start <= end:
        nums[start] , nums[end] = nums[end] , nums[start]
        start += 1
        end -= 1
    return nums

if k < n:
    nums = reverse(nums, 0, k-1)
    nums = reverse(nums, k, n-1)
else:
    nums = reverse(nums, 0, n-1)
    
print(nums)