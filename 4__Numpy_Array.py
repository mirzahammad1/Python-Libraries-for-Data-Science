import numpy as np
# zero Dimension array
array = np.array(24)
print (array)

# one D array
one_D_array = np.array([1,2,3,4])
print(one_D_array)

# Two D array
two_D_array = np.array([[1,2,3,4],[5,6,7,8]])
print(two_D_array)

# three D array
three_D_array = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[1,1,1]]])
print(three_D_array)

print (three_D_array.shape)
print (three_D_array.ndim)

numpy_1D_array = np.array([x for x in range(1,10)])
print(numpy_1D_array)

# converting 1D array to 2D
print(numpy_1D_array.reshape(3,3))

# converting 1D array to 3D
numpy_1D_arr = np.array([x for x in range(1,13)])

print(numpy_1D_arr.reshape(3,2,2))

# for unknown dimension
print(numpy_1D_arr.reshape(2,2,-1)) # usfull when dealing with dynamic dataset

numpy_array = numpy_1D_arr.reshape(3,2,2)
print(numpy_array.reshape(-1))
