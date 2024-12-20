import numpy as np

# 产生一个随机数，范围是[0, 1)
# random()函数是numpy.random模块中的函数，用于生成随机数
# 与 rand() 函数的区别是：
# 1.random() 函数只有一个参数，表示生成的随机数的个数；
# 2.rand() 函数可以传入多个参数，表示生成的随机数的形状；
value = np.random.random()
print(value)

# 一维数组
# 生成一个包含8个随机数的一维数组
array_1 = np.random.random(8)
print(array_1)

# 二维数组
# 生成一个包含3行4列的二维数组
array_2 = np.random.random((3, 4))
print(array_2)