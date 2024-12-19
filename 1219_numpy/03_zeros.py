import numpy as np

# 创建一维数组
# zeros 函数用于创建元素全为 0 的数组，参数是数组的长度
zero_array = np.zeros(3)
print(zero_array)
# empty 函数用于创建元素全为 0 的数组，参数是数组的长度，元素的值是未初始化的
zero_array = np.empty(3)
print(zero_array)

# ones 函数用于创建元素全为 1 的数组，参数是数组的长度
one_array = np.ones(5)
print(one_array)

# 创建二维数组
# zeros 函数用于创建元素全为 0 的数组，参数是一个元组，表示数组的形状
# 元组的第一个元素是数组的行数，第二个元素是数组的列数
zero_array_2d = np.zeros((3, 4))   # 3行4列
print(zero_array_2d)
# empty 函数用于创建元素全为 0 的数组，参数是一个元组，表示数组的形状，元素的值是未初始化的
zero_array_2d = np.empty((3, 4))
print(zero_array_2d)

# ones 函数用于创建元素全为 1 的数组，参数是一个元组，表示数组的形状
# 元组的第一个元素是数组的行数，第二个元素是数组的列数
one_array_2d = np.ones((5, 2))   # 5行2列
print(one_array_2d)

# arange 函数用于创建数组，参数是数组的长度
# arange 函数创建的是一维数组，数组的元素是从 0 到 9 的整数
array_1 = np.arange(10)
print(array_1)

# arange 函数用于创建数组，参数是数组的起始值和结束值
# arange 函数创建的是一维数组，数组的元素是从 3 到 9 的整数
array_2 = np.arange(3, 10)
print(array_2)

# arange 函数用于创建数组，参数是数组的起始值、结束值和步长
# arange 函数创建的是一维数组，数组的元素是从 3 到 9 的整数，步长为 2
# start 表示数组的起始值，stop 表示数组的结束值，step 表示数组的步长
# 数组的元素是从 start 开始，到 stop 结束，步长为 step
array_3 = np.arange(3, 10, 2)
print(array_3)

# linspace 函数用于创建数组，参数是数组的起始值、结束值和元素的个数
# linspace 函数创建的是一维数组，数组的元素是从 0 到 10 的 5 个等间距的数
# start 表示数组的起始值，stop 表示数组的结束值，num 表示数组的元素个数
array = np.linspace(0, 10, num=5)
print(array)

# start 表示数组的起始值，stop 表示数组的结束值，num 表示数组的元素个数，dtype 表示数组的数据类型，np.float64 表示 64 位浮点数，np.int64 表示 64 位整数
array = np.linspace(0, 10, num=5, dtype=np.float64)
print(array)

array = np.linspace(0, 10, num=5, dtype=np.int64)
print(array)