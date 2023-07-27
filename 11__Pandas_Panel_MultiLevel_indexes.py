import pandas as pd
df = pd.read_csv("Housing.csv",parse_dates=True)
print(df.head())

print(df.set_index(['price','airconditioning'],inplace=True))
print(df.index)

print(df.loc[1750000]) # show only whose price is <---
print(df.loc[1750000].loc['no']) # show only whose price is <---
