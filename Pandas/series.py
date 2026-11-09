import numpy as np
import pandas as pd

# series_data = pd.Series(data=[40, 50, 60], index=[
#                         'Bread', 'Milk', 'Butter'], name='Price of Grocery Items', dtype='int32')

# print(series_data)
# print('-' * 30)

# country = ['India', 'China', 'USA', 'UAE']

# country_data = pd.Series(country)

# print(country_data)
# print("-" * 30)

# batsman_runs = [48, 64, 72, 98, 114, 183]
# batsman_data = pd.Series(batsman_runs, dtype='int32')
# print(batsman_data)
# print("-" * 30)

# subject_names = ['Math', 'Physics', 'Chemistry', 'Biology', 'English']
# subject_marks = [48, 92, 64, 35, 98]
# marks = pd.Series(data=subject_marks, index=subject_names,
#                   name="Subject Marks Data", dtype='int32')
# print(marks)
# print('-' * 30)

# # Creating as Series using a Numpy Array

# valuse = np.arange(10, 21)
# series_np_data = pd.Series(valuse, dtype='int32')
# print(series_np_data)
# print('-' * 30)

# # Creating Dictionary to Series

# data_items = {'Math': 78, 'English': 92, 'Physics': 88, 'Chemistry': 64}

# items_data = pd.Series(data_items)
# print(items_data)
# print('-' * 30)

# # custome index to series

# values = [1, 2, 3, 4, 5]
# values_data = pd.Series(data=values, index=['a', 'b', 'c', 'd', 'e'])
# print(values_data)
# print('-' * 30)

# # scalar value inside on series
# print(pd.Series(4,index=['a', 'b', 'c', 'd', 'e']))
# print('-' * 30)

# Mathmetical Function in Pandas
marks = [78, 85, 90, 66, 72]

subs = pd.Series(marks)
# print(subs)
# print(subs.sum())
# print(subs.product())
# print(subs.mean())
# print(subs.median())
# print(subs.mode())
# print(subs.std())
# print(subs.var())
# print(subs.min())
# print(subs.max())
# print(subs.describe())
# print(subs[::-1])
print(subs[[1, 3, 4]])
subs[0]=100

print(subs)