import sys

num = 54
print(sys.getsizeof(num))
print(num.__sizeof__())
"""
    28
"""

string = "vinayak"
print(sys.getsizeof(string))
print(string.__sizeof__())
"""
    empty string = 49 and +1 number of characters (here 56)
"""

tuple1 = (1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10)
print(sys.getsizeof(tuple1))
print(tuple1.__sizeof__())
"""
    empty tuple = 40 and +8 per number of elements
"""

list1 = [1,2,3,4,5,6,7,8,9,10]
print(sys.getsizeof(list1))
print(list1.__sizeof__())
"""
    empty list = 56 and +8 and +16 per number of elements
"""

set1 = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
print(sys.getsizeof(set1))
print(set1.__sizeof__())
"""
    empty set       64
    1 - 4           216
    5 - 7           472
    8 - 15          728
    16 ...          1240
"""