import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('diamonds.csv')

std_scaler_obj = StandardScaler()
df['converted_price'] = std_scaler_obj.fit_transform(df[['price']])
print(df[['price','converted_price']])
