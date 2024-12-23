import numpy as np

# 广播两个不同形状的数组
# 维度不同时，广播规则是从最后一个维度开始比较，如果维度相同或者其中一个维度为1，则可以广播
a = np.zeros((4))
b = np.zeros((3, 4))
print(a*b)
print((a*b).shape)