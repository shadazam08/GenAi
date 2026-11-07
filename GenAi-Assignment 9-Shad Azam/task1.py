# Task 1: Creating NumPy Arrays
import numpy as np


array_1d = np.arange(1,11)
array_2d = np.arange(1,10).reshape(3,3)
array_from_list = np.array([10,20,30,40,50])


print("Values: ", array_1d)
print("Shape: ", array_1d.shape)
print("Data Type: ", array_1d.dtype)

print("\n")
print("Values: ", array_2d)
print("Shape: ", array_2d.shape)
print("Data Type: ", array_2d.dtype)

print("\n")
print("Values: ", array_from_list)
print("Shape: ", array_from_list.shape)
print("Data Type: ", array_from_list.dtype)