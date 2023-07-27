#######     SOME COMMON ARTHMATIC OPERATIONS

import numpy as np

A = np.array([[1,2,3,4,5],[6,7,8,9,7]])
B = np.array([1,6,2,8,3])

# adding 
print(np.add(A,B))

# subracting 
print(np.subtract(B,A))

# multiply
print(np.multiply(A,B))

# divide
print(np.divide(A,B))

# power
print(np.power(A,2)) # square of every element in array A
print(np.power(A,B)) 