import pandas as pd

df = pd.read_csv('../Day-06_17_08_2025/diamonds.csv')
# print(df)

df.drop(['Unnamed: 0'],axis=1,inplace=True)
print(df)

"""
axis=1 is basically to remove on column basis
inplace = True is basically to update the changes in all df """

