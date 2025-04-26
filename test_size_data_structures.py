import sys

# test_tuple = (1,2,3,4)
# print(type(test_tuple))
# print(sys.getsizeof(test_tuple))
# print(test_tuple.__sizeof__())

# test_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
# print(sys.getsizeof(test_list))

# create_list = list([1,2,3,4,5])
# print(sys.getsizeof(create_list))


# print(8 >> 3)


test_set = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
test_set_str = {'a', 'b', 'c', 'd', 'e', ''}
print(sys.getsizeof(test_set))
print(sys.getsizeof(test_set_str))

create_set = set((1,2,3,4,5,6,7))
print(sys.getsizeof(create_set), type(create_set))