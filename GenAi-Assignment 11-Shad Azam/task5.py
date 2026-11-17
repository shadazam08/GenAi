# Task 5: Stacked Bar Chart()

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

north.index = pd.CategoricalIndex(north.index, categories=[ 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], ordered=True)
west.index = pd.CategoricalIndex(west.index, categories=[ 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], ordered=True)
south.index = pd.CategoricalIndex(south.index, categories=[ 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], ordered=True)
east.index = pd.CategoricalIndex(east.index, categories=[ 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'], ordered=True)

north = north.sort_index()
west = west.sort_index()
south = south.sort_index()
east = east.sort_index()

plt.figure(figsize=(12, 7))
plt.title('Region and year by amount calculate')
plt.xlabel('Region')
plt.ylabel('Total Amount')
plt.bar(north.index, north.values, color='#250E75', width=0.2, label='North')
plt.bar(south.index, south.values, color='#8B1C62', width=0.2, label='South', bottom=north.values)
plt.bar(west.index, west.values, color='#f44336', width=0.2, label='West',bottom=north.values+south.values)
plt.bar(east.index, east.values, color='#0A9975', width=0.2, label='East',bottom=north.values+south.values+west.values)
plt.legend()
plt.show()
