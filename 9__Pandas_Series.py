import pandas as pd
# Pandas Series is a one-Dimentional Ndarray with access labels where you can access the element using the labels
# it also uses Numpy as its underlying architecture.

l = [x for x in range (5)]
print(pd.Series(l)) # to make series from
print(pd.Series(l,index=['a','b','c','d','e'])) # naming the indexes

data = {'a':1,'b':2,'c':3,'d':4,'e':5}
print(pd.Series(data)) # to make series from dictionary
print(pd.Series(data,index=['a','b'])) # to pick known data

s = pd.Series([x for x in range (11)])
print(s.iloc[0]) # shows the element at nth index
print(s.iat[5]) # shows the element at nth index

print(s[4:9]) # for slicing
print(s.where(s%2==0)) # for condition
print(s.where(s%2==0,s**2)) # for condition when we want square of odd number
print(s.dropna) # to drop all null values
print(s.fillna(4)) # to fill all null values