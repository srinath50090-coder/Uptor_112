import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OrdinalEncoder

df = pd.read_csv('diamonds.csv')
# print(df)

"""This code converts the categorical data into numerical using Alphabetical order
(If cut column contains Fair,Good,Very Good,Ideal,Premium , Then F-0,G-1,I-2,P-3,VG-4,
NAN-5)"""

l_e = LabelEncoder()
df['cut'] = l_e.fit_transform(df['cut'])
print(df)

print(l_e.classes_)

"""This code also converts the categorical data into numerical using Alphabetical order
(If cut column contains Fair,Good,Very Good,Ideal,Premium , Then F-0,G-1,I-2,P-3,VG-4,
But null data is not filled in this code)"""

o_e = OrdinalEncoder()
df['cut'] = o_e.fit_transform(df[['cut']])
print(df)

print(o_e.categories_)
