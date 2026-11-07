# Task 6: Percentiles & Sorting

import numpy as np

marks = np.array([78, 85, 90, 66, 72, 88, 95, 60])

sorted_marks = np.sort(marks)
p25 = np.percentile(marks, 25)
p50 = np.percentile(marks, 50)
p75 = np.percentile(marks, 75)

average_marks = np.mean(marks)
above_avg_count = np.sum(marks > average_marks)


print("Sorted Array: ", sorted_marks)
print("25th percentile: ", p25)
print("50th percentile: ", p50)
print("75th percentile: ", p75)
print("Number of students scored above average: ", above_avg_count)
