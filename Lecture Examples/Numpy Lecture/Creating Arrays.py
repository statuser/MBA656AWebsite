import numpy as np

a = np.array([1, 2, 3])

print(type(a))
print(a.shape)
print(a[0], a[1], a[2])
a[0] = 5
print(a)

b = np.array([[1,2,3], [4, 5, 6]])
print(b)

print(b.shape)
print(b[0,0], b[0,1], b[1,0])


# You can also create a lot of different types of arrays
a = np.zeros((2,2))
print(a)

b = np.ones((3,2))
print(b)

c = np.full((1,2), 7)
print(c)

d = np.eye(3)
print(d)

e = np.random.random((3,3))
print(e)

# There are more in the documentation: http://docs.scipy.org/doc/numpy/user/basics.creation.html#arrays-creation

# Array Indexing is very similar to the way that we would index and slice lists

slicing_demo = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(slicing_demo)

slicing_demo2 = slicing_demo[:2, 1:3]
print(slicing_demo2)
# Remember that the :2 means up to, but not including row number 2.  (Indexing starts at 0)

print(slicing_demo[0, 1])
slicing_demo2[0,0] = 77
print(slicing_demo[0,1])
# This demonstrates a weird thing about slicing and objects.  When we assign an 
# object we are not copying the object we are just crating another reference to 
# that object.  The same things occurs when we slice an object.  This is a little
#  tricky and unexpected.

# There is a lot more in the documentation, but you won't use most of it unless 
# you are doing scientific programming or writing your own algorithms in matrix algebra

### Array Math
x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

# Elementwise sum; both produce the array
# [[ 6.0  8.0]
#  [10.0 12.0]]
print(x + y)
print(np.add(x, y))

# Elementwise difference; both produce the array
# [[-4.0 -4.0]
#  [-4.0 -4.0]]
print(x - y)
print(np.subtract(x, y))

# Elementwise product; both produce the array
# [[ 5.0 12.0]
#  [21.0 32.0]]
print(x * y)
print(np.multiply(x, y))

# Elementwise division; both produce the array
# [[ 0.2         0.33333333]
#  [ 0.42857143  0.5       ]]
print(x / y)
print(np.divide(x, y))

# Elementwise square root; produces the array
# [[ 1.          1.41421356]
#  [ 1.73205081  2.        ]]
print(np.sqrt(x))

### Matrix Operations

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

v = np.array([9,10])
w = np.array([11, 12])

# Inner product of vectors; both produce 219
print(v.dot(w))
print(np.dot(v, w))

# Matrix / vector product; both produce the rank 1 array [29 67]
print(x.dot(v))
print(np.dot(x, v))

# Matrix / matrix product; both produce the rank 2 array
# [[19 22]
#  [43 50]]
print(x.dot(y))
print(np.dot(x, y))

print(np.sum(x))  # Compute sum of all elements; prints "10"
print(np.sum(x, axis=0))  # Compute sum of each column; prints "[4 6]"
print(np.sum(x, axis=1))  # Compute sum of each row; prints "[3 7]"

### Reshaping an array pr matrix
print(x)    # Prints "[[1 2]
            #          [3 4]]"
print(x.T)  # Prints "[[1 3]
            #          [2 4]]"

# Note that taking the transpose of a rank 1 array does nothing:
v = np.array([1,2,3])
print(v)    # Prints "[1 2 3]"
print(v.T)  # Prints "[1 2 3]"