import numpy as np

# zeros() 函数创建一个给定形状和类型的用0填充的数组，第一个参数是形状，第二个参数是数据类型，默认是 float64
# 3行4列的二维数组，元素都是0
array = np.zeros((3, 4))
print(array)
# ndim 属性返回数组的维数
print(array.ndim)
# shape 属性返回一个元组，表示数组的维度
print(array.shape)
# size 属性返回数组中元素的个数
print(array.size)
# dtype 属性返回数组中元素的类型，包括 int64、float64 等类型
print(array.dtype)
# itemsize 属性返回数组中每个元素的字节单位长度，int64 类型的 itemsize 为 8(64/8)
# float64 类型的 itemsize 为 8
print(array.itemsize)