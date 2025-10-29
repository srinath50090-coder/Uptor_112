import pandas as pd

df = pd.read_csv("house_price_bd.csv")
# print(df)

# column_name = df.columns
# print(column_name)

df.drop(['Title','Location'],axis=1,inplace=True)
# print(df)

# print(df["Price_in_taka"])

"""This removes special characters, commas in unnecessary places in a string 
data type"""

df["Price_in_taka"] = df["Price_in_taka"].replace({'৳':'',',':''},regex=True)
# print(df["Price_in_taka"])

"""This removes special characters, commas in unnecessary places in a string 
data type and converts string into float"""

df["Price_in_taka"] = df["Price_in_taka"].replace({'৳':'',',':''},regex=True).astype(float)
print(df["Price_in_taka"])

"""This removes special characters, commas in unnecessary places in a string 
data type and converts string into float(same code given above)"""

df["Price_in_taka"] = df["Price_in_taka"].replace({"r^\d.":""},regex=True).astype(float)
print(df["Price_in_taka"])


