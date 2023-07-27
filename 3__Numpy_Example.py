# -------Create a one dimentional array with alias as np and perform the following methon ---------
# 1.np.zero()
# 2.np.ones()
# 3.np.empty()
# 4.np.arrange()
# 5.np.reshape()
# 6.np.linspace()

import numpy as np

first_numpr_array = np.array([1,2,3,4,5,6,7,8,9])
print(first_numpr_array)

array_with_zeros = np.zeros((3,3))
print(array_with_zeros)

array_with_ones = np.ones((4,5))
print(array_with_ones)

array_with_empty = np.empty((5,6))
print(array_with_empty)

array_arange = np.arange(12)
print(array_arange)

print(array_arange.reshape(3,4))

array_linspce = np.linspace(2,4,7)
print(array_linspce)

one_D_array = np.arange(15)
print(one_D_array)

two_D_array = one_D_array.reshape(3,5)
print(two_D_array)

three_D_array = np.arange(27).reshape(3,3,3)
print(three_D_array)