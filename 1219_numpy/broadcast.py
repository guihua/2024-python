import numpy as np

# 将标量广播到数组
# 例如
# 1.将一个标量广播到一个数组的每个元素上
# 2.将一个标量广播到一个数组的每一行或每一列上
# 3.将一个标量广播到一个数组的每一个维度上
array = np.array([1, 2, 3])
scalar = 2
# 将标量广播到数组，即将标量复制到数组的每个元素上
result = array * scalar
print(result)

# 广播两个不同形状的数组，例如将一个1D数组广播到2D数组，或将一个2D数组广播到3D数组
# 维度不同时，广播规则是从最后一个维度开始比较，如果维度相同或者其中一个维度为1，则可以广播
array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([1, 2, 3])
result = array1 + array2
print(result)

# 将一维阵列广播到二维阵列
array1 = np.array([[1], [2], [3]])
array2 = np.array([4, 5, 6])
result = array1 + array2
print(result)

# 不同维度的广播
array1 = np.array([1, 2, 3])
array2 = np.array([[1], [2], [3]])
result = array1 * array2
print(result)