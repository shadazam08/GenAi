# Task 8: Pandas Plotting (Simple Graphs)

import pandas as pd
import matplotlib.pyplot as plt

students = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Sneha', 'Pooja'],
    'Marks': [78, 85, 90, 66, 72],
    'Subject': ['Math', 'Math', 'Science', 'Science', 'Math']
}

df = pd.DataFrame(students)

df.set_index('Name')['Marks'].plot(kind='bar')
plt.show()
df['Marks'].plot(kind='line')
plt.show()
df['Marks'].plot(kind='hist')
plt.show()
