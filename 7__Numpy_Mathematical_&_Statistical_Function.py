######  COMMON MATHEMATICAL & STATISTICAL FUNTIONS
import numpy as np
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])

# finding minimum value
print(np.min(arr))
print(np.amin(arr,axis=0)) # in vertical
print(np.amin(arr,axis=1)) # in horziontal

# finding maximum value
print(np.max(arr))
print(np.amax(arr,axis=0)) # in vertical
print(np.amax(arr,axis=1)) # in horziontal

print(np.median(arr))             # for median
print(np.mean(arr))               # for mean
print(np.std(arr))                # for standard
print(np.var(arr))                # for variant
print(np.percentile(arr,60))      # to find percentile (0-100)

from numpy import pi
deg = np.array([0,15,30,45,60,75,90])
print(np.sin(deg*pi/180))

print(np.cos(deg*pi/180))
print(np.tan(deg*pi/180))
print(np.arccos(deg*pi/180))
print(np.arccos(deg*pi/180))
print(np.arctan(deg*pi/180))

arr = np.array([0.1,-9,-4,3,-3])
print(np.floor(arr))
print(np.ceil(arr))
