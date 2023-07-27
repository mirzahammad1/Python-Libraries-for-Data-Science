import numpy as np
array = np.array([i for i in range(10)])
print(array)

# find even and odd
print(np.where(array%2 == 0,'ÉVEN','ODD'))

# select
condition_list = [array<5,array>5]
choice_List = [array**2,array**3]
print(np.select(condition_list,choice_List,default=array)) # every number less than 5 will be squared and greater than 5 is cubied
