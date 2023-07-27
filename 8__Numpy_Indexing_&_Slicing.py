import numpy as np
array_1D = np.array([1,2,3,4,5,6])
array_2D = np.array([[1,2,3],[4,5,6]])
array_3D = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

# calling indexes
print(array_1D[3])
print(array_2D[1,2])
print(array_3D[1,1,2])

# slicing
print(array_1D[1:])
print(array_2D[1,1:])
print(array_3D[0,0,1:])