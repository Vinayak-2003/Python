# You are given a list of n unique numbers from 1 to n+1, but one number is missing. 
# Write a function to find the missing number in the sequence and take arr as an argument in it and 
# array can be (ex. - missing_number([1,3,4,5]) , missing_number([1,2,3,4,5,6,8,9,10])) anything 
# according to user


def missing_number(numbers):
    max_number = max(numbers)
    for i in range(1,max_number):
        if i not in numbers:
            return i
    
num = missing_number([1,3,4,5])
print(num)