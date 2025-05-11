def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        j = i-1
        key = nums[i]
        while j>=0 and key < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key

    return nums

nums = [6,2,1,9,5,4]
ans = insertion_sort(nums)

print(ans)