# Task 6: Histogram (Marks Distribution)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./sales_data.csv')
df = pd.DataFrame(data)


plt.figure(figsize=(12,7))
plt.title('Sales Amount Distribution')
plt.xlabel('Sales Amount')
plt.ylabel('Frequency')
plt.hist(df['Sales_Amount'].dropna(), bins=20)
plt.show()