def bubble_sort(nums):
    n = len(nums)
    already_sorted = True
    for i in range(n):
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

                # if any swap occurs it will make the falg as false
                already_sorted = False
    
    if already_sorted:
        return nums
    
    return nums

nums = [6,2,1,9,5,4]
ans = bubble_sort(nums)

print(ans)