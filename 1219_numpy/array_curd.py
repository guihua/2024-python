import numpy as pd

# 创建两个一维数组，形状为 (2,)
left_ndarray = pd.array([1, 2])
right_ndarray = pd.array([4, 5])

# 加法
# 两个数组相加，对应元素相加，返回一个新的数组
# 两个数组的形状必须相同
result = left_ndarray + right_ndarray
print(result)

# 减法
# 两个数组相减，对应元素相减，返回一个新的数组
# 两个数组的形状必须相同
result = left_ndarray - right_ndarray
print(result)

# 乘法
# 两个数组相乘，对应元素相乘，返回一个新的数组
# 两个数组的形状必须相同
result = left_ndarray * right_ndarray
print(result)

# 除法
# 两个数组相除，对应元素相除，返回一个新的数组
# 两个数组的形状必须相同
result = left_ndarray / right_ndarray
print(result)

# 取整除法
# 两个数组取整除，对应元素取整除，返回一个新的数组
# 两个数组的形状必须相同
result = left_ndarray // right_ndarray
print(result)

# 创建两个一维数组，形状为 (2,)
left_ndarray = pd.array([7, 2])
right_ndarray = pd.array([4, 5])

# 加法
# 两个数组相加，对应元素相加，返回一个新的数组
# 两个数组的形状必须相同
left_ndarray += right_ndarray
print(left_ndarray)

# 减法
# 两个数组相减，对应元素相减，返回一个新的数组
# 两个数组的形状必须相同
left_ndarray -= right_ndarray
print(left_ndarray)

# 乘法
# 两个数组相乘，对应元素相乘，返回一个新的数组
# 两个数组的形状必须相同
left_ndarray *= right_ndarray
print(left_ndarray)

# 除法
# 两个数组相除，对应元素相除，返回一个新的数组
# 两个数组的形状必须相同
left_ndarray //= right_ndarray
print(left_ndarray)   # [7 2]

# 取整除法
# 两个数组取整除，对应元素取整除，返回一个新的数组
# 两个数组的形状必须相同
# 异常
# left_ndarray /= right_ndarray
# print(left_ndarray)

left_ndarray = pd.array([[1, 1], [0, 1]])
right_ndarray = pd.array([[2, 0], [3, 4]])
# 矩阵乘法
# 两个数组相乘，返回一个新的数组
# 两个数组的形状必须相同
result = left_ndarray @ right_ndarray
print(result)

left_ndarray = pd.array([[1, 1], [0, 1]])
right_ndarray = pd.array([[2, 0], [3, 4]])
# 矩阵乘法
# dot 函数也可以用来进行矩阵乘法，返回一个新的数组
# 两个数组的形状必须相同
result = left_ndarray.dot(right_ndarray)
print(result)