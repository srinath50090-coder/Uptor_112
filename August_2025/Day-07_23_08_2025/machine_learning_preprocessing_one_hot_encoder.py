import pandas as pd
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv('diamonds.csv')

# one_hot_encoding_object = OneHotEncoder()
# encoded_result = one_hot_encoding_object.fit_transform(df[['cut']])
# print(encoded_result)

one_hot_encoding_object = OneHotEncoder(sparse_output=False)
encoded_result = one_hot_encoding_object.fit_transform(df[['cut']])
# print(encoded_result)

new_df = pd.DataFrame(encoded_result)
# print(new_df)

"""To change array to dataframe"""
new_df = pd.DataFrame(encoded_result,columns=one_hot_encoding_object.get_feature_names_out())
# print(new_df)


final_df = pd.concat([df,new_df],axis=1)
final_df.drop('cut',axis=1,inplace=True)
# print(final_df)

