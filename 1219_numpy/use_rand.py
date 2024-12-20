import numpy as np

# 生成一个随机数，范围是[0, 1)，生成的随机数是一个浮点数，类型是float64
# rand()函数是numpy.random模块中的函数，用于生成随机数
# rand()函数只有一个参数，表示生成的随机数的个数
# 1.如果不传入参数，则生成一个随机数
# 2.如果传入参数，则生成一个一维数组，数组的元素是随机数
value = np.random.rand()
print(value, type(value))

# 一维数组随机数
# 生成一个包含6个随机数的一维数组
array_1 = np.random.rand(6)
print(array_1)
# 二维数组随机数
# 生成一个包含3行2列的二维数组
array_2 = np.random.rand(3, 2)
print(array_2)