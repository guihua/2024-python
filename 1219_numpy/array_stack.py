import numpy as np

# 创建两个相同形状的二维数组，形状为 (2, 2)
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# 沿着轴 0 堆叠，得到一个新的数组，形状为 (2, 2, 2)
result = np.stack((a, b), axis=0)
print(result)
# 沿着轴 1 堆叠，得到一个新的数组，形状为 (2, 2, 2)
result = np.stack((a, b), axis=1)
print(result)
# 沿着轴 2 堆叠，得到一个新的数组，形状为 (2, 2, 2)
result = np.stack((a, b), axis=2)

# 创建两个不同形状的二维数组，形状分别为 (2, 2) 和 (2, 1)
c = np.array([[[1], [2]], [[3], [4]]])
d = np.array([[[5], [6]], [[7], [8]]])

# 沿着轴 0 堆叠，得到一个新的数组，形状为 (2, 2, 1)
result = np.stack((c, d), axis=0)
print(result)