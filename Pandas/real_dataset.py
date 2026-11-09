import numpy as np
import pandas as pd


# data = pd.read_csv('../youtubeDataset/youtube_2025_dataset_202504061614.csv')
# data = pd.read_csv('../youtubeDataset/youtube_one_column.csv')
# df = data.squeeze('columns')
# # print(type(df))
# print(df)
# print('-' * 60)
data1 = pd.read_csv('../youtubeDataset/youtube_two_column.csv', index_col='Youtuber Name').astype('int32')
dataframe = data1.squeeze('columns')

# dataframes = type(data1)
# dataframes = data1.values
# dataframes = data1.dtype
# dataframes = data1.size
# dataframes = data1.shape
# dataframes = data1.ndim
# dataframes = data1.name
# dataframes = data1.is_unique
# dataframes = data1.head(2)
dataframes = data1.tail(2)
# print(data1)
print(dataframe)
print('-' * 60)
print(dataframes)
print('-' * 60)

