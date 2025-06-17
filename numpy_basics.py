import numpy as np
a = np.array([1,2,3])
b = np.array([4,5,6])

# print(a + b)
# print(a * b)
# print(a / b)

arr = np.array([4,25,64])
# print(np.sqrt(arr))
# print(np.sum(arr))
# print(np.mean(arr))
# print(np.max(arr))


arra = np.array([10,20,30,40,50,60])
# print(arra[2])
# print(arra[-1])

# print(arra[1:4])  #Slice
# print(arra[:3])
# print(arra[3:])

reshaped = arra.reshape(2,3)
# print(reshaped)


matrix = np.array([[1,2,3,8], [4,5,6,6], [7,8,9,8], [10,11,12,54]])
# Calculate sum of each row
row_sums = np.sum(matrix, axis=1)
# print("\nSum of each row:")
# print(row_sums)

# Calculate sum of each column
col_sums = np.sum(matrix, axis=0)
# print("\nSum of each column:")
# print(col_sums)


def findMinMaxFromArray(arr):
   return np.min(arr)

array = np.array([1,2,3])   
result = findMinMaxFromArray(array)
print(result)