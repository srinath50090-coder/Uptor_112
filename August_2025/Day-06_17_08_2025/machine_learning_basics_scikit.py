import pandas as pd

"""We can do filling using Pandas but in large dataset the efficiency of Pandas 
is low. So, we go for a SimpleImputer to handle large dataset easily"""

from sklearn.impute import SimpleImputer

df = pd.read_csv("diamonds.csv")
# print(df)

"""Simple imputer fills null data using mean value automatically"""
# simple_imputer_object = SimpleImputer()
# df["carat"] = simple_imputer_object.fit_transform(df[['carat']])
# print(df)

"""Simple imputer is only for numerical data so below code will fail"""
# simple_imputer_object = SimpleImputer()
# df["cut"] = simple_imputer_object.fit_transform(df[['cut']])
# print(df)

"""In below code simple imputer fills the null data using most frequent value(mode)"""
# simple_imputer_object = SimpleImputer(strategy="most_frequent")
# df["carat"] = simple_imputer_object.fit_transform(df[['carat']])
# print(df)

"""In below code simple imputer fills the null data using a constant value"""
# simple_imputer_object = SimpleImputer(strategy="constant",fill_value=100)
# df["carat"] = simple_imputer_object.fit_transform(df[['carat']])
# print(df)

