import numpy as np

# 创建一个全是 1 的数组，形状为 (2,)
array_1 = np.ones(2)
print(array_1)
# 修改数组中的元素，索引从 0 开始，将第一个元素修改为 100
array_1[0] = 100
print(array_1)

# 创建一个全是 0 的二维数组，形状为 (3, 4)
array_2 = np.zeros((3, 4))
print(array_2)
# 修改数组中的元素，索引从 0 开始，将第二行第三列的元素修改为 100
array_2[2][2] = 100
print(array_2)

# arange 函数创建一个数组，元素从 0 开始，到 11 结束，步长为 1
array = np.arange(12)
print(array)
# reshape 函数将数组的形状修改为 (3, 4)，即将数组转换为一个二维数组
# reshape 函数会返回一个新的数组，不会对原数组进行修改
# reshape 函数的参数是一个元组，表示数组的形状
array = array.reshape((3, 4))
print(array)
# 将数组的形状修改为 (12,)，即将数组展开为一维数组
array = array.reshape((12, ))
print(array)

# 创建一个一维数组，形状为 (6,)
array = np.array([1, 2, 3, 4, 5, 6])
# 将数组的形状修改为 (6, 1)，即将数组转换为一个二维数组
array01 = array[:, np.newaxis]
print(array01)
print(array01.shape)

# 将数组的形状修改为 (1, 6)，即将数组转换为一个二维数组
# np.newaxis 是一个 None 的别名，可以用来增加数组的维度，相当于增加一个轴
# np.newaxis 的作用是在指定的位置增加一个维度，从而改变数组的形状
array02 = array[np.newaxis, :]
print(array02)
print(array02.shape)

# 将数组的形状修改为 (6, 1)，即将数组转换为一个二维数组
# expand_dims 函数也可以用来增加数组的维度，相当于增加一个轴，但是 expand_dims 函数更加灵活
# expand_dims 函数的第一个参数是数组，第二个参数是要增加的轴的位置，从 0 开始，-1 表示在最后一个位置增加一个轴，-2 表示在倒数第二个位置增加一个轴，以此类推
# expand_dims 函数会返回一个新的数组，不会对原数组进行修改
array03 = np.expand_dims(array, axis=1)
print(array03)
print(array03.shape)

# 将数组的形状修改为 (1, 6)，即将数组转换为一个二维数组
# axis=0 表示在第一个位置增加一个轴，相当于在最外层增加一个维度
array04 = np.expand_dims(array, axis=0)
print(array04)
print(array04.shape)