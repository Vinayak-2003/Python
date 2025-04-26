nums = [10,10,3,7,6]

def total(nums, start, end):
    total_sum = 0
    n = len(nums)
    for i in range(start , end):
        total_sum += nums[i]
    return total_sum

count = 0
n = len(nums)
for i in range(0,n-1):
    left_sum = total(nums, 0, i+1)
    righ_sum = total(nums, i+1, n)
    print(left_sum, righ_sum)
    if (left_sum-righ_sum)%2 == 0:
        count += 1
print(count)

