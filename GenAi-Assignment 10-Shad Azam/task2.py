# Task 2: Mathematical Operations Series

import pandas as pd

marks = [78, 85, 90, 66, 72]
marks_series = pd.Series(marks)

add_marks = marks_series + 5
sub_marks = marks_series - 2
mul_marks = marks_series * 1.05
div_marks = marks_series / 2

print(f"Add 5 grace marks:\n{add_marks}")
print(f"Subtract 2 marks:\n{sub_marks}")
print(f"Multiply all marks by 1.05:\n{mul_marks}")
print(f"Divide all marks by 2:\n{div_marks}")
