# Numpy - Numerical python
# Mathematical operations on arrays
# Faster  operations

import numpy as np
from time import process_time

# List vs Numpy - time taken
python_list = [i for i in range(10000)]
start_time = process_time()
python_list = [i+5 for i in python_list]
end_time = process_time()
print(end_time)

np_array = np.array([i for i in range(10000)])
start_time = process_time()
np_array += 5
end_time = process_time()
print(end_time)


# Numpy array declaration
# 1d array
np_array = np.array([1, 2, 3, 4])
print(type(np_array))
print(np_array.shape)

np_2d_array = np.array([(1,2,3), (4,5,6)])
print(np_2d_array.shape)

# Initial placeholders in numpy arrays

# zeros array
x = np.zeros((4, 5))
print(x)

# ones array
y = np.ones((3, 3))
print(y)

# array of particular value
z = np.full((5, 4), 5)
print(z)

# Identity matrix
a = np.eye(4)
print(a)

# with random values
b = np.random.random((3, 4))
print(b)

# random int values with range
c = np.random.randint(10, 100, (3, 5))
print(c)

# array of evenly spaced values - 10, 30 range, 6 space and no of elements
d = np.linspace(10, 30, 6)
print(d)

# array of evenly spaced values - specifying only steps
e = np.arange(10, 30, 5)
print(e)

# convert list to np array
list1 = [1, 2, 3, 4]
np_array = np.asarray(list1)
print(np_array, type(np_array))

# Analyze numpy array
a = np.random.randint(10, 90, (5, 5))
print(a)
print(a.shape) # shape of array
print(a.ndim) # dimension of array
print(a.size) # number of elements in array
print(a.dtype) # datatype of array

# mathematical ops
a = np.random.randint(0, 10, (3, 3))
b = np.random.randint(10, 20, (3, 3))
print(a)
print(b)

print(a + b)
print(a - b)
print(a * b)
print(a / b)

print(np.add(a, b))
print(np.subtract(a, b))
print(np.multiply(a, b))
print(np.divide(a, b))

# Array manipulation
array = np.random.randint(0, 10, (2, 3))
print(array)

# transpose
print(array.shape)
trans = np.transpose(array)
print(trans)
print(trans.shape)

trans2 = array.T
print(trans)
print(trans.shape)

# rehshape an array
a = np.random.randint(0, 10, (2, 3))
print(a)
print(a.shape)

b = a.reshape(3,2)
print(b, b.shape)