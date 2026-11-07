# Task 5: Statistical Operations

import numpy as np

marks = np.array([78, 85, 90, 66, 72, 88, 95, 60])

mean_value = np.mean(marks)
median_value = np.median(marks)
variance_value = np.var(marks)
standard_value = np.std(marks)
max_value = np.max(marks)
min_value = np.min(marks)
range_value = max_value - min_value

print("Mean: ", mean_value)
print("Median: ",median_value)
print("Variance: ", variance_value)
print("Standard Deviation: ", standard_value)
print("Maximum: ", max_value, "& Minimum: ", min_value)
print("Range: ",range_value)

