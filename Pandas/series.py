import numpy as np
import pandas as pd

series_data = pd.Series(data=[40, 50, 60], index=[ 'Bread', 'Milk', 'Butter'], name='Price of Grocery Items', dtype='int32')

print(series_data)
print('-' * 30)

country = ['India', 'China', 'USA', 'UAE']

country_data = pd.Series(country)

print(country_data)
print("-" * 30)

batsman_runs = [48, 64, 72, 98, 114, 183]
batsman_data = pd.Series(batsman_runs, dtype='int32')
print(batsman_data)
print("-" * 30)

subject_names = ['Math', 'Physics', 'Chemistry', 'Biology', 'English']
subject_marks = [48, 92, 64, 35, 98]
marks = pd.Series(data=subject_marks, index=subject_names, name="Subject Marks Data", dtype='int32')
print(marks)
print('-' * 30)

