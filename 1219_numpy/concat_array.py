import numpy as np

# 创建一个全是 1 的数组，形状为 (3,)
array_1 = np.ones(3)
array_2 = np.ones(3)
print(array_1)
print(array_2)

# 数组相加，会将对应位置的元素相加，得到一个新的数组，而不是将两个数组拼接在一起
# array_1 和 array_2 的形状相同，可以相加
array_3 = array_1 + array_2
print(array_3)

# 创建一个全是 1 的数组，形状为 (2,)
# array_1 的形状为 (3,)，array_4 的形状为 (2,)，两个数组的形状不同，无法相加
array_4 = np.ones(2)
# 如果两个数组的形状不同，会报错
# ValueError: operands could not be broadcast together with shapes (3,) (2,)
array_5 = array_1 + array_4
print(array_5)