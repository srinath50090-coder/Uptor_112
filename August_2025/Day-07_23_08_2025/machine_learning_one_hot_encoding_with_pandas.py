import pandas as pd

df = pd.read_csv('diamonds.csv')

encoded_df = pd.get_dummies(df['cut'],prefix='cut')
print(encoded_df)

final_df = pd.concat([df,encoded_df],axis=1)
final_df.drop('cut',axis=1,inplace=True)
print(final_df)