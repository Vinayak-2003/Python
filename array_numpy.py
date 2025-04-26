import numpy as np

l_arr = np.array([1,2,3,4,5, 'hello', True])
t_arr = np.array((1,2,3,4,5, 'hello', True))
s_arr = np.array({1,2,3,4,5, 'hello', True})
print(t_arr)
# print(type(s_arr))

# print(np.__version__)


#------------------------Dimensions in Array--------------------------
arr0 = np.array([5])
# print(arr0)
# print(type(arr0))
# print(arr0.ndim)

arr1 = np.array([1,2,3,4,5])
# print(arr1)
# print(type(arr1))
# print(arr1.ndim)

arr2 = np.array([[1,2,3], 
                 [4,5,6]])
# print(arr2)
# print(type(arr2))
# print(arr2.ndim)

arr3 = np.array([[[1,2,3], 
                  [4,5,6]], 
                 
                 [[1,2,3], 
                  [4,5,6]]])
# print(arr3)
# print(type(arr3))
# print(arr3.ndim)


arr5 = np.array([1,2,3,4,5], ndmin=5)
# print(arr5)


#------------------------Accessing Array Items--------------------------
# print(arr1[2])
# print(arr2[0, 1], arr2[1, 2])
# print(arr3[0, 1, 2])


#------------------------Slicing in Array--------------------------
print(arr1[1:4])