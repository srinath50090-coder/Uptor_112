import pandas as pd

df = pd.read_csv("diamonds.csv")
# print(df)

"""below code is basically to find any duplicates in the rows"""
# finding_duplicates = df[df.duplicated()]
# print(finding_duplicates)
#
# print("--------------------------------------------------------------------------------")
#
"""To remove the duplicates from dataset"""
# df.drop_duplicates(inplace=True)
# print(df)
#
# print("-----------------------------------------------------")
#
# finding_duplicates = df[df.duplicated()]
# print(finding_duplicates)

"""below code has additional attribute keep = False will include original"""
"""This code shows duplicates and its original """
# finding_duplicates = df[df.duplicated(keep=False)]
# print(finding_duplicates)

"""below code has additional attribute keep = last will include last as original"""
finding_duplicates = df[df.duplicated(keep="last")]
print(finding_duplicates)

"""
1 Mohan
2 mohan
3 Mohan
Condition:1 df[df.duplicated()]
2 Mohan
3 Mohan     (here 1st is original 2nd and 3rd are duplicate )
Condition:2 df[df.duplicated(keep=False)]
1 Mohan
2 Mohan
3 Mohan     (It returns duplicates and original too) 
Condition:3 df[df.duplicated(keep="last)]
1 Mohan
2 Mohan     (here 1st and 2nd are duplicates and the original at last)
"""

"""Below code drops both duplicates and original also """
df.drop_duplicates(keep=False,inplace=True)
print(df)
