import numpy as np

# numpy_array = np.array([1, 2, 3, 4, 5])

# # print(type(numpy_array))
# print(numpy_array)

twoDArray = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# print(twoDArray)
# # print(type(twoDArray))

# threeDArray = np.array(
#     [[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])

# print(threeDArray)
# # print(type(threeDArray))

# dtyep_array = np.array([1, 2, 3, 4, 5], dtype=np.int32)

# print(dtyep_array)


# empty_array = []
# for i in range(16):
#     empty_array.append(i)
# print(empty_array)

# arange_array = np.arange(16)
# arange_array = np.arange(1,17)
# arange_array = np.arange(2,21,2)
# arange_array = np.arange(1,17)
# arange_data = arange_array.reshape(4,4)
# print(arange_data)

# Mathmetical Operations

# array = np.random.random((3, 3))*100
# print(array)
# print('-'*30)
# array = np.round(array)
# print(array)
# print('-'*30)

# array = array.astype('int32')
# print(array)
# print('-'*30)

# print(array.dtype)
# print('-'*30)

# array = array + 2
# print(array)
# print('-'*30)

# array = array - 5
# print(array)
# print('-'*30)

# array = array * 2
# print(array)
# print('-'*30)

# array = array / 2
# print(array)
# print('-'*30)


# array = array > 60

# print(array)
# print('-'*30)

# vector operation

arr_1 = np.arange(1, 17).reshape(4, 4)
# arr_2 = np.arange(17, 33).reshape(4, 4)

# sum_arr = arr_1 + arr_2
# print(arr_1)
# print("-" * 35)
# print(arr_2)
# print("-" * 35)
# print(sum_arr)

# print(np.log(arr_1))
# print(np.exp(arr_1))

print(np.sqrt(twoDArray))

