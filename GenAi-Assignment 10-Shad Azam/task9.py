# Task 9: Mini Use Case: Sales Data Analysis

import pandas as pd
import matplotlib.pyplot as plt

sales = {
    'Day': ['Mon', 'Tue', 'Wes', 'Thu', 'Fri'],
    'Revenue': [1200, 1500, 900, 2000, 1800]
}

df = pd.DataFrame(sales)

total_rev = df['Revenue'].sum()
avg_rev = df['Revenue'].mean()
highest_day = df[df['Revenue'] == df['Revenue'].max()]['Day'].values[0]
above_avg_days = df[df['Revenue'] > avg_rev]
df.set_index('Day')['Revenue'].plot(kind='bar', title='Revenue vs Day')

print(f"Total Revenue: {total_rev}")
print(f"Average Daily Revenue: {avg_rev}")
print(f"Day with Highest Revenue: {highest_day}")
print(f"Days where revenue > average:\n{above_avg_days}")
plt.show()

