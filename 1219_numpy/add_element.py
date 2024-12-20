import numpy as np

# arange 生成数组
# 生成一个一维数组，包含10个元素，元素值从0到9，步长为1
array = np.arange(10)
print('init array:', array)

# append 添加元素
# append() 函数在数组的末尾添加值，如需添加到特定位置，可以使用 insert() 函数。
# append() 函数会对输入数组进行复制，对原数组没有影响。
# append() 函数有两个参数，第一个是数组，第二个是值。其中，数组可以是多维的，但是值必须是标量。
newarray = np.append(array, 11)
print('old array:', array)
print('new array:', newarray)

# insert 插入元素
# insert() 函数在数组的指定位置插入值，如需在末尾添加值，可以使用 append() 函数
# insert() 函数会对输入数组进行复制，对原数组没有影响
# insert() 函数有三个参数，第一个是数组，第二个是索引值，第三个是值。其中，数组可以是多维的，但是值必须是标量。
insert_array = np.insert(array, 0, -1)
print('old array:', array)
print('insert array', insert_array)

array2 = np.array([11, 12])
# 数组拼接
# 数组拼接是指将两个或多个数组沿着指定的轴拼接在一起。
# 数组拼接有两种方式，一种是使用 concatenate() 函数，另一种是使用 stack() 函数。
# concatenate() 函数可以沿着指定的轴拼接多个数组
# concatenate() 函数有两个参数，第一个是数组，第二个是轴。其中，数组可以是多维的，但是轴必须是相同的。
concat_array = np.concatenate((array, array2))
print('concat array:', concat_array)