import pandas as pd

from utils import dataframe_modifier

a = 3

for cnt in range(a+1):
    b = a - cnt
    print(a / b)

df = pd.DataFrame([[1,2],[2,3]], columns=["a","b"])
print(df)

df = dataframe_modifier(df, a)

print(df)