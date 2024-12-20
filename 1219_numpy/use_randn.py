import numpy as np

# 生成一个随机数
# randn()函数是numpy.random模块中的函数，用于生成随机数
# randn()函数只有一个参数，表示生成的随机数的个数
# randn可以从标准正态分布中返回一个或多个样本值，取值范围是[-inf, inf]，均值为0，方差为1，即标准正态分布
# randn()与rand()的区别是：
# 1.randn()函数生成的随机数服从标准正态分布，均值为0，方差为1；
# 2.rand()函数生成的随机数服从均匀分布，取值范围是[0, 1)；
value = np.random.randn()
print(value)

# 一维数组随机数
# 生成一个包含90个随机数的一维数组
array_1 = np.random.randn(90)
# print(array_1)
# 计算数组的均值和方差，均值是数组元素的平均值，方差是数组元素的平均值与每个元素的差的平方的平均值
# mean()函数是numpy.ndarray对象的方法，用于计算数组的均值
# var()函数是numpy.ndarray对象的方法，用于计算数组的方差
print(array_1.mean(), array_1.var())

# 二维数组随机数
# 生成一个包含10行9列的二维数组
array_2 = np.random.randn(10, 9)
# print(array_2)
print(array_2.mean(), array_2.var())

# 生成指定均值和方差的正态分布，均值是2，方差是9
# 正态分布是一种连续概率分布，其概率密度函数是一个关于均值的对称函数，均值是分布的中心，方差是分布的离散程度
# 正态分布的应用非常广泛，例如在统计学、金融学、物理学、生物学等领域，用于描述随机变量的分布，例如测量误差、股票价格、粒子运动等
array = 3*np.random.randn(100) + 2
print(array.mean())
print(array.var())