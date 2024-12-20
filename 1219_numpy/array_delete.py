import numpy as np

# 创建一维数组，形状为 (6,)
array_01 = np.array([1, 2, 3, 4, 5, 6])
print(array_01)
# 删除数组中的元素
# delete 函数会返回一个新的数组，不会对原数组进行修改
# delete 函数有两个参数，第一个是数组，第二个是要删除的元素的索引，可以传入一个整数，也可以传入一个列表，表示要删除多个元素
# 索引从 0 开始，删除第一个元素和第四个元素
array_02 = np.delete(array_01, [0, 3])
print(array_02)

# 将数组的形状修改为 (2, 3)，即将数组转换为一个二维数组
array_03 = np.reshape(array_01, (2, 3))
print(array_03)
# 删除数组中的元素
array_04 = np.delete(array_03, [1])
print(array_04)