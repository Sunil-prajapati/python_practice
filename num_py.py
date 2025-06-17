# NumPy is basically for numerical computation (and it's very advanch in computing)
# better performance
# Ease to use
# Integration with other libraries

import numpy as np

arr = np.array([1,2,3,4,5])
# print(arr)

zeroes = np.zeros((3,3))
# print(zeroes)

ones = np.ones((2,4))
# print(ones)

rangeArray = np.arange(1,10,2)
# print(rangeArray)

linespace_array = np.linspace(0,1,5)
# print(linespace_array)

arr = np.array([1,2,3,4,5,6])
reshaped = arr.reshape((2,3))
# print(reshaped)

arr1 = np.array([1,2,3,4,5])
expanded = arr1[:, np.newaxis]
print(expanded)