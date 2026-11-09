# Task 1: Pandas Series Basic

import pandas as pd

marks = [78, 85, 90, 66, 72]
marks_series = pd.Series(marks)

series_value = marks_series.values
series_index = marks_series.index
series_data_type = marks_series.dtype
first_element = marks_series[0]
last_element = marks_series[-2:]


print(f"Series values: {series_value}")
print(f"Index: {series_index}")
print(f"Data type: {series_data_type}")
print(f"First Element: {first_element}")
print(f"Last two elements:\n{last_element}")
