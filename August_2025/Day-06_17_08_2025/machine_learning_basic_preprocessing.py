import pandas as pd


df = pd.read_csv("diamonds.csv")
# print(df)

"""To find total number of null data for each column"""
# finding_null_data = df.isna().sum()
# print(finding_null_data)

"""Filling the null data by forward fill (above value) """
# df.ffill(inplace=True)
# print(df)

"""Filling the null data by backward fill (below value)"""
# df.bfill(inplace=True)
# print(df)

"""Filling a specific column using its mean value"""
# df['carat'] = df['carat'].fillna(df['carat'].mean())
# print(df)

"""Filling a specific column using another column's mean value"""
# df['x'] = df['x'].fillna(df['carat'].mean())
# print(df)










