# Task 3: Python Functionalities on Series

import pandas as pd

marks = [78, 85, 90, 66, 72]
marks_series = pd.Series(marks)

max_marks = marks_series.max()
min_marks = marks_series.min()
sum_marks = marks_series.sum()
mean_marks = marks_series.mean()
passed_status = marks_series.apply(lambda x: x >= 70)
passed_count = passed_status.sum()

print(f"Maximum marks: {max_marks}")
print(f"Minimum marks: {min_marks}")
print(f"Sum of marks: {sum_marks}")
print(f"Mean marks: {mean_marks}")
print(f"Pass status for each student:\n{passed_status}")
print(f"Total number of students who passed: {passed_count}")

