import numpy as np

# randint()函数是numpy.random模块中的函数，用于生成随机数
# randint()函数生成的随机数的范围是[low, high)，即包含下限值，不包含上限值
# randint()函数有三个参数：
# 1.第一个参数 low 表示生成随机数的下限，包含下限值；
# 2.第二个参数 high 表示生成随机数的上限，不包含上限值；
# 3.第三个参数 size 表示生成随机数的形状，可以是一个整数，也可以是一个元组，表示生成的随机数的形状；
# 生成一个随机整数，范围是[0, 4)
value = np.random.randint(4)
print(value)

# 生成一个包含8个随机整数的一维数组，范围是[3, 9)
value = np.random.randint(3, 9, size=8)
print(value)