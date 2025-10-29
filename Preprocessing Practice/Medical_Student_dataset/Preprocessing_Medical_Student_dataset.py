import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder,OrdinalEncoder,OneHotEncoder

df = pd.read_csv('medical_students_dataset.csv')
# print(df)
# print(df.columns)
# print(df.info())
# print(df.describe())


# ----------------------------------------- Handling Duplicates ----------------------------------------------
# print(df.duplicated().sum())
# print(df[df.duplicated()])
df.drop_duplicates(inplace=True)
# print(df.duplicated().sum())


# -------------------------------------- Filling Missing Values ---------------------------------------------------

# print(df.isna().sum())

df['Student ID'] = df['Student ID'].interpolate(method='linear')
# print(df['Student ID'].head(60))

# print(df['Age'].describe())
df['Age'] = df['Age'].fillna(np.random.randint(18,35))
# print(df['Age'])

df['Gender'] = df['Gender'].ffill()
# print(df['Gender'])

simple_imputer = SimpleImputer(strategy='mean')
df['Height'] = simple_imputer.fit_transform(df[['Height']])

simple_imputer = SimpleImputer()
df['Weight'] = simple_imputer.fit_transform(df[['Weight']])

df['Blood Type'] = df['Blood Type'].bfill()

df['BMI'] = df['BMI'].fillna(df['BMI'].mean())

df['Temperature'] = df['Temperature'].fillna(df['Temperature'].mean())

df['Heart Rate'] = df['Heart Rate'].fillna(df['Heart Rate'].median())

df['Blood Pressure'] = df['Blood Pressure'].fillna(df['Blood Pressure'].median())

simple_imputer = SimpleImputer(strategy='median')
df['Cholesterol'] = simple_imputer.fit_transform(df[['Cholesterol']])

df['Diabetes'] = df['Diabetes'].ffill()

df['Smoking'] = df['Smoking'].bfill()


# ----------------------------------------- Feature Engineering ------------------------------------------------------

label_encoder = LabelEncoder()
ordinal_encoder = OrdinalEncoder()
one_hot_encoder = OneHotEncoder()

df['Gender'] = label_encoder.fit_transform(df['Gender'])

encoded_df = pd.get_dummies(df['Blood Type'],prefix='Blood Type')
encoded_df = encoded_df.astype(int)
df = pd.concat([df,encoded_df],axis=1)
df.drop(['Blood Type'],axis=1,inplace=True)

df['Diabetes'] = ordinal_encoder.fit_transform(df[['Diabetes']])

df['Smoking'] = label_encoder.fit_transform(df['Smoking'])


# print(df.shape)
# print(df.info())
df.to_csv('Pre-Processed_Medical_Students_dataset.csv', index=False)



