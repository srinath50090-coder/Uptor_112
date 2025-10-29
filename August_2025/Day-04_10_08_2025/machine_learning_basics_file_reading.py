import pandas as pd

# pd.set_option("display.max_columns",None)
# pd.set_option('display.max_rows',None)

"""below line is actually to read the csv file from current file"""
df = pd.read_csv('diamonds.csv')
# print(df)

"""below line is actually to read only the column names"""
# columns=df.columns
# print(columns)

"""below lines is to read the data types of the given dataset"""
# column_data_types=df.dtypes
# print(column_data_types)

"""below lines is to get the general information about the dataset"""
# df_information=df.info()
# print(df_information)

"""below function will work only on the numerical columns"""
# df_description=df.describe()
# print(df_description)

"""reading a single column and its data"""
# data=df['carat']
# print(data)

"""reading more than one column data"""
# data=df[['carat','cut']]
# print(data)

"""reading first 5 number of rows"""
# data=df.head()
# print(data)

"""reading last 5 number of rows"""
# data=df.tail()
# print(data)

"""reading specific number of rows"""
# data=df.head(10)
# print(data)

"""below concept is called slicing that cuts the rows  in the given numeric order"""
# data=df[10:20]#it will return the rows from 10 to 19
# print(data)

"""locator function that returns all the specified number of rows"""
# data=df.loc[10:20]#it will return the rows from 10 to 20
# print(data)

# data=df.loc[10:20,"carat"]#it will return the rows from 10 to 20 for specific column
# print(data)

# data=df.loc[10:20,['carat','cut']]#it will return the rows from 10 to 20 for specific columns
# print(data)

# data=df.iloc[10:20,1:3]#it will return the rows from 10 to 19 for specific column in numbers
# print(data)

# data=df.iloc[10:20,[1,5,7]]#it will return the rows from 10 to 19 for specific column in numbers
# print(data)

"""type checking for specific column"""
# data_type=df['carat'].dtype
# print(data_type)





