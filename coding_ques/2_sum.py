# Given an integer array nums and a target value, return two indices of two numbers such that
# they add up to target.
# Input:
# nums = [2,7,11,15,12, 5]     target = 13
# Output:
# ans = [0,2]

nums = [2,7,11,15,12,5]
target = 13
n = len(nums)

# solution 1
for i in range(0,n):
    for j in range(0,n):
        if i==j:
            continue
        if nums[i]+nums[j] == target:
            print([i,j])
            break
        
# solution 2
numMap = {}
for i in range(0,len(nums)):
    sub = target - nums[i]
    if sub in numMap:
        print([numMap[sub], i])
    else:
        numMap[nums[i]] = i