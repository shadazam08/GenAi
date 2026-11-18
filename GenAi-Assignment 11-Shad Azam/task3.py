# Task 3: Bar Plot()

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./sales_data.csv')

df = pd.DataFrame(data)

group_data = df.groupby('Region')['Sales_Amount'].sum()

x = group_data.index
y = group_data.values

plt.figure(figsize=(10, 6))
plt.title('Vertical Bar Chart: Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales Amount')
plt.bar(x, y, color='red', width=0.8)
plt.show()

plt.figure(figsize=(10, 6))
plt.title('Vertical Bar Chart: Total Sales by Region')
plt.xlabel('Total Sales Amount')
plt.ylabel('Region')
plt.barh(x, y, color='red')
plt.show()
