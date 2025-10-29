import pandas as pd


df = pd.read_csv("Financials.csv", parse_dates=['Date'], index_col=['Date'])
df.drop(['Month Number',' Month Name ', 'Year'],axis=1,inplace=True)

df[' Units Sold '] = df[' Units Sold '].replace({r"[^\d.]":""},regex=True).astype(float)
df[' Manufacturing Price '] = df[' Manufacturing Price '].replace({r"[^\d.]":""},regex=True).astype(float)
df[' Sale Price '] = df[' Sale Price '].replace({r"[^\d.]":""},regex=True).astype(float)
df[' Gross Sales '] = df[' Gross Sales '].replace({r"[^\d.]":""},regex=True).astype(float)

df[' Discounts '] = df[' Discounts '].replace(r'[^\d.-]', '', regex=True)
df[' Discounts '] = pd.to_numeric(df[' Discounts '],errors='coerce').fillna(0)

df['  Sales '] = df['  Sales '].replace({r'[^\d.]':''},regex=True).astype(float)
df[' COGS '] = df[' COGS '].replace({r'[^\d.]':''},regex=True).astype(float)

df[' Profit '] = df[' Profit '].replace(r'[^\d\.\-]','',regex=True)
df[' Profit '] = pd.to_numeric(df[' Profit '],errors='coerce').fillna(0)

df.to_csv('Processed_Financials.csv')
