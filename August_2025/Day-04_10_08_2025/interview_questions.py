"""How to get categorical and numerical data from the given dataset or csv?"""

import pandas as pd

# pd.set_option("display.max_columns",None)
# pd.set_option('display.max_rows',None)

"""below line is actually to read the csv file from current file"""
df = pd.read_csv('diamonds.csv')
column_names=df.columns

numerical_columns=[]
categorical_columns=[]

for col in column_names:
    if df[col].dtype=="O":
        categorical_columns.append(col)
    else:
        numerical_columns.append(col)

print(categorical_columns)
print(numerical_columns)



