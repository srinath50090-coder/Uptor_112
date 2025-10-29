import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('diamonds.csv')

min_max_scaler_obj = MinMaxScaler()
df['converted_price'] = min_max_scaler_obj.fit_transform(df[['price']])
print(df[['price','converted_price']])
