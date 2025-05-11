def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if nums[min_index] > nums[j]:
                nums[min_index], nums[j] = nums[j], nums[min_index]

    return nums


nums = [6,2,1,9,5,4]
ans = selection_sort(nums)

print(ans)