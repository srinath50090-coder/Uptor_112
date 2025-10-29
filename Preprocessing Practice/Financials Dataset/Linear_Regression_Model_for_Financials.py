import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

df = pd.read_csv('Processed_Financials.csv')

x = df[[' Units Sold ', ' Manufacturing Price ', ' Sale Price ',' Gross Sales ', ' Discounts ', '  Sales ',' COGS ']]
y = df[[' Profit ']]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 42)

model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

accuracy = r2_score(y_test, y_pred)
print(accuracy)
