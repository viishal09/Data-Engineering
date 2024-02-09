import numpy as np


arr = np.array([1, 2, 3, 4, 5])

print(arr)
print(arr[0:3])

print(np.__version__)

lis1 = [1,2,3,4]

array = np.array(lis1)

print(array)

print(type(lis1))
print(type(array))

# 0D array

lis2 = [42]
array2 = np.array(lis2)
print("0D array :",array2)

# #1D array
lis4 = [1,2,3,4]
array4 = np.array(lis4)
print("1D array :",array4)


# 2D array

lis3 = [[1,2,3,],[4,5,6]]
array3 = np.array(lis3)
print("2D array :",array3)

# print(array3.flatten())
print(array3.ndim)
print(array3.shape)
print(type(array3))
print(array3.dtype)
print(array3.size)

#numpy array creation

zero_array = np.zeros((3,6))
print(zero_array,"\n")

one_array = np.ones((2,3))
print(one_array,"\n")

random_array = np.random.random((2,2))
print(random_array,"\n")


# Array creation using Range()

a = np.arange(1, 10)
print(a)
x = range(1, 10)
print(x)    # x is an iterator
print(list(x))
x = np.arange(10.4)
print(x)
x = np.arange(0.5, 10.4, 0.8)
print(x)

line_array = np.linspace(0,10,15)
print(line_array)

# 50 values between 1 and 10:
print(np.linspace(1,10,7))
print(np.linspace(1, 10, 7, endpoint=False,retstep=True))
