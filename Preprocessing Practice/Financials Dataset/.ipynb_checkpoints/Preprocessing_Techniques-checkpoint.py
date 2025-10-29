import pandas as pd

df = pd.read_csv('Processed_Financials.csv')
print(df)
print(df.columns)
print(df.info())
print(df.describe())

"""Finding Null Values in Dataset"""
finding_null = df.isna().sum().sum()
print(finding_null)

unique_values = df.nunique()
print(unique_values)

