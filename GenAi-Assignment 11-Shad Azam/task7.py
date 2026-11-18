# Task 7: Pie Chart (Market Share)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./sales_data.csv')
df = pd.DataFrame(data)

sales_data = df.groupby('Region')['Sales_Amount'].sum()

plt.figure(figsize=(10,10))
plt.title('Percentage Contribution of Region in total Sales')
plt.pie(sales_data,labels=sales_data.index, autopct='%0.1f%%')
plt.legend()
plt.show()