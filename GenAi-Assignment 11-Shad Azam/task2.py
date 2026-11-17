# Task 2: Scatter Plot()

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./sales_data.csv')

df = pd.DataFrame(data)


x = df['Discount']
y = df['Sales_Amount']


plt.figure(figsize=(10, 7))
plt.title('Relationship Between Discount and Sales Amount')
plt.xlabel('Discount')
plt.ylabel('Sales Amount')
plt.scatter(x, y, linewidth=1.5, linestyle='--', color='red', marker='o')
plt.show()
