import numpy as np

np_sqrt = np.sqrt([2,3,4,5,6,7,8,9,16])
print (np_sqrt)                         # square root function

from numpy import pi
print(np.cos(0))                        # trignometric function
print(np.sin(pi/2))

print(np.floor([1.5,2.6,3.7,7.8,4.9,5.0,6.1,8.2,7.3]))   # return the floot of the input
 
print(np.exp([0,1,5]))                  # Exponrntial function for complex mathematical calculations

################################    SHAPE MANIPULATION     ################################

new_array = np.array([[22,34,56,54,86,21],[90,88,22,11,44,66]])
print(new_array.ravel())                # Flattens the dataset

print(new_array.reshape(3,4))                # change or re-shape the dataset

print(np.hsplit(new_array,2))                # splits the dataset

array1 = np.array([10,22,34,56,54,86,21])
array2 = np.array([90,88,22,11,44,66,29])
print(np.hstack(array1,array2))                # stacks the dataset together
