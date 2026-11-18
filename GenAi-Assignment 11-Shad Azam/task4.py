# Task 4: Multiple Bar Plot()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./sales_data.csv')
df = pd.DataFrame(data)

df['Sale_Date'] = pd.to_datetime(df['Sale_Date'])
df['Sale_Date'] = df['Sale_Date'].dt.month_name()

north = df[df['Region'] == 'North']
west = df[df['Region'] == 'West']
south = df[df['Region'] == 'South']
east = df[df['Region'] == 'East']

north = north.groupby('Sale_Date')['Sales_Amount'].sum()
west = west.groupby('Sale_Date')['Sales_Amount'].sum()
south = south.groupby('Sale_Date')['Sales_Amount'].sum()
east = east.groupby('Sale_Date')['Sales_Amount'].sum()

north.index = pd.CategoricalIndex(north.index, categories=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], ordered=True)
west.index = pd.CategoricalIndex(west.index, categories=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], ordered=True)
south.index = pd.CategoricalIndex(south.index, categories=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], ordered=True)
east.index = pd.CategoricalIndex(east.index, categories=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], ordered=True)

north = north.sort_index()
west = west.sort_index()
south = south.sort_index()
east = east.sort_index()

months_order = ['January', 'February', 'March', 'April', 'May', 'June','July', 'August', 'September', 'October', 'November', 'December']

plt.figure(figsize=(12, 7))
plt.title('Total Sales by Region and Year')
plt.xlabel('Month')
plt.ylabel('Total Amount')
plt.bar(np.arange(len(months_order)) - 0.3, north.values, color='#250E75', width=0.2, label='North')
plt.bar(np.arange(len(months_order)) - 0.1, south.values, color='#8B1C62', width=0.2, label='South')
plt.bar(np.arange(len(months_order)) + 0.1, west.values, color='#f44336', width=0.2, label='West')
plt.bar(np.arange(len(months_order)) + 0.3, east.values, color='#0A9975', width=0.2, label='East')
plt.legend()
plt.xticks(np.arange(len(months_order)), months_order)
plt.show()
