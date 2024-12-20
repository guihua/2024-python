import numpy as np

# uniform()函数是numpy.random模块中的函数，用于生成随机数，生成的随机数服从均匀分布
# uniform(low, high, size)函数的参数：
# low: 生成的随机数的最小值
# high: 生成的随机数的最大值
# size: 生成的随机数的维度
# uniform()函数生成的随机数服从均匀分布，取值范围是[low, high)，均值是(low + high) / 2
# uniform()函数生成的随机数的数据类型是float64，如果需要生成其他数据类型的随机数，可以使用astype()函数进行转换
# 生成一个在[1.4, 2.8) 范围内的随机数
value = np.random.uniform(1.4, 2.8)
print(value)

# 生成9个在[0.5, 3.5) 之间的随机数
array_1 = np.random.uniform(0.5, 3.5, 9)
print(array_1)
print(array_1.mean())

# 生成一个维度是(3, 4) 的数组，元素在[0.5, 3.5)范围内随机
array_2 = np.random.uniform(0.5, 3.5, (3, 4))
print(array_2)