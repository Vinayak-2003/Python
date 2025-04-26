nums = [2,41,11,76,55,3]

first_max = -999999
second_max = -99999

for num in nums:
    if num > first_max:
        second_max = first_max
        first_max = num
    
    elif num>second_max and num<first_max:
        second_max = num
    
print(second_max)