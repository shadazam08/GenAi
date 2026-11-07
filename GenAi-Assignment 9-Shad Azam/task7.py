# Task 7: Mini use case: Scale Analysis

import numpy as np

sales = np.array([1200, 1500, 900, 2000, 1800, 1700, 1600])

weekly_sales = np.sum(sales)
average_daily = np.mean(sales)
highest_sales = np.max(sales)
lowest_sales = np.min(sales)
std_sales = np.std(sales)
above_average_sales = sales[sales > average_daily]

print("Total Weekly Sales:", weekly_sales)
print("Average Daily Sales:", average_daily)
print("Highest Sales: ", highest_sales, "and Lowest Sales: ", lowest_sales)
print("Standard Deviation:", std_sales)
print("Above Average Sales:", above_average_sales)
