# Series 是 Pandas 库中的一种数据结构，它类似于一维数组，可以存储任何类型的数据，如整数、字符串、浮点数等。
# Series 对象由索引（index）和值（value）两部分组成。
# Series 对象的基本语法格式如下：
# pandas.Series(data, index, dtype, copy)
# 参数说明：
# data：可以是列表、元组、字典、ndarray 等数据类型。
# index：索引，默认为从 0 开始的整数序列。
# dtype：数据类型，默认为 None。
# copy：是否复制数据，默认为 False。
# 例如：
# import pandas as pd
#
from pandas import Series

# 创建 list 对象
lst = ['python', 'c++', 'c#', 'java']
# 通过列表创建 Series 对象，索引默认为从 0 开始的整数序列
ser1 = Series(lst)
print(ser1)

# 通过列表创建 Series 对象，指定索引，索引为 a、b、c、d，索引的长度必须和数据的长度一致，否则会报错
ser2 = Series(lst, index=['a', 'b', 'c', 'd'])
print(ser2)

# 创建 dict 对象，键为字符串，值为整数
score_dict = {
    'python': 100,
    'c++': 99,
    'c#': 98,
    'java': 97
}

# 通过字典创建 Series 对象，索引默认为字典的键，值为字典的值，索引的顺序为字典的键的顺序
ser3 = Series(score_dict)
print(ser3)
# 获取索引为 c++ 的值
print(ser3['c++'])
# 设置索引为 java 的值为 100
ser3['java'] = 100
print(ser3)

# 获取索引，返回的是一个 Index 对象
print(ser3.index)
# 获取值，返回的是一个 ndarray 对象
print(ser3[0])
# 切片操作
# 使用数组的切片方法，实现对 series 的切片操作，返回的是一个 Series 对象
print(ser3[1:])