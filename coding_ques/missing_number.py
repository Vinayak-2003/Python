# Question. Given an array nums containing n distinct numbers in the range [0, n], 
# return the one number that is missing from the array.
# Input:
# nums = [3,0,1]
# Output:
# ans=2

nums = [3,0,1]
# for i in range(0,len(nums)+1):
#     if i in nums:
#         continue
#     else:
#         print(i)
        
original_sum = 0
nums_sum = 0
for i in range(0,len(nums)+1):
    if i<len(nums) and nums[i] != 0:
        nums_sum += nums[i]
        
for i in range(1,len(nums)+1):
    original_sum += i
        
result = original_sum - nums_sum
print(result)