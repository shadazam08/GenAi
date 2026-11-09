# Task 4: Creating a DataFrame

import pandas as pd

students = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks': [78, 85, 90, 66, 72],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}

df = pd.DataFrame(students)
print(df)
print("-" * 30)
print(f"First 3 Rows:\n{df.head(3)}")
print("-" * 30)
print(f"Last 2 Rows:\n{df.tail(2)}")
print("-" * 30)
print(f"Shape: {df.shape}")
print(f"Columns: {list(df.columns)}")
