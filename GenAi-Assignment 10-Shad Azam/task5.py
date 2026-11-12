# Task 5: Important DataFrame Functions

import pandas as pd

students = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks': [78, 85, 90, 66, 72],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}

df = pd.DataFrame(students)
print("Info: ")
df.info()
print(f"\nDescribe:\n{df.describe()}")
print(f"\nHead:\n{df.head()}")
print(f"\nTail:\n{df.tail()}")
sorted_df = df.sort_values(by='Marks', ascending=False).reset_index()
print(f"\nSorted & Reset Index:\n{sorted_df}")