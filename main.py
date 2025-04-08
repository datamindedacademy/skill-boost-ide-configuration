import pandas as pd

from utils import dataframe_modifier

a = 3
b = 3-1

print(a / b)

df = pd.DataFrame([[1,2],[2,3]], columns=["a","b"])
print(df)

df = dataframe_modifier(df, b)

print(df)