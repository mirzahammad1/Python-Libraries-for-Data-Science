import pandas as pd
df = pd.DataFrame()
print(type(df))

df = pd.read_csv('Housing.csv') # will show the data in tabular form
print(df.head()) # will show first 5 rows
print(df.tail()) # will show last 5 rows

#print(df.iat[2]) # will show all the elements in index 2
print(df.values) # will show the values of the datafarme

df = pd.read_csv('Housing.csv',chunksize=2)
for chunk in df:
    print (chunk)  # will print chunk of 2 row in loop 

df = pd.read_csv('Housing.csv')
print(df = df['bedrooms']>2)
print (df)   # will show all the rows where Bedrooms is greater than 2