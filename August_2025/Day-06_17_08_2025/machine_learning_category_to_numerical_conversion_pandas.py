import pandas as pd
import numpy as np

df = pd.read_csv('diamonds.csv')
print(df)

cut_detailing = df['cut'].unique()
print(cut_detailing)

# [nan 'Premium' 'Good' 'Very Good' 'Fair' 'Ideal']

df['cut'] = df['cut'].map({"Good":1,np.nan:0,"Premium":4,'Fair':3,'Very Good':8})
print(df)