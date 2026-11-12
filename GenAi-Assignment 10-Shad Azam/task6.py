# Task 6: Filtering & Conditional Selection

import pandas as pd

students = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks': [78, 85, 90, 66, 72],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}

df = pd.DataFrame(students)
filter_75 = df[df['Marks'] > 75]
filter_math = df[df['Subject'] == 'Math']
avg_marks = df['Marks'].mean()
filter_above_avg = df[df['Marks'] > avg_marks]
filter_failed = df[df['Marks'] < 70]


print(f"More Than 75 marks:\n{filter_75}")
print(f"\nStudent Belong to Math Subject:\n{filter_math}")
print(f"\nScored More than avarage marks:\n{filter_above_avg}")
print(f"\nFailed Student:\n{filter_failed}")
