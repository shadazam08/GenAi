# Task 1: Line Plot (Sales Trend)

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./sales_data.csv')

df = pd.DataFrame(data)
df['Sale_Date'] = pd.to_datetime(df['Sale_Date'])
df['Sale_Date'] = df['Sale_Date'].dt.month_name()

group_data = df.groupby('Sale_Date')['Sales_Amount'].sum()

group_data.index = pd.CategoricalIndex(group_data.index, categories=[
                                       'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], ordered=True)

group_data = group_data.sort_index()

x = group_data.index
y = group_data.values

plt.figure(figsize=(14,7))
plt.title('Sales Trend Over Month')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.plot(x,y, linewidth=1.5, linestyle='--', color='red',marker='o')
plt.grid()
plt.show()
