# Task 7: Grouping & Basic Analysis

import pandas as pd

students = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks': [78, 85, 90, 66, 72],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}

df = pd.DataFrame(students)

avg_marks = df.groupby('Subject')['Marks'].mean()
count_name = df.groupby('Subject')['Name'].count()
max_marks = df.groupby('Subject')['Marks'].max()


print(f"Average Marks per Subject:\n{avg_marks}")
print(f"\nNumber of Students per Subject:\n{count_name}")
print(f"\nMaximum Marks per Subject:\n{max_marks}")
