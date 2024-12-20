import numpy as np

# 将标量广播到数组，即将标量复制到数组的每个元素上
array = np.arange(1, 5)
array = array*2
print(array)

# 广播两个相同形状的数组
# 维度相同时，广播规则是从最后一个维度开始比较，如果维度相同，则可以广播
array_1 = np.arange(1, 5)
array_2 = np.arange(2, 6)
print(array_1, array_2)
array_3 = array_1 + array_2
print(array_3)