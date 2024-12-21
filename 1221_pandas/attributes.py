from pandas import Series

# Series 对象的属性，包括：
# - axes：返回行轴标签列表
# - dtype：返回对象的数据类型
# - empty：如果系列为空，则返回 True
# - ndim：返回底层数据的维数，默认情况下为 1
# - size：返回基础数据中的元素数
# - values：将 Series 的值作为 ndarray 返回
# - head()：返回前 n 行
# - tail()：返回最后 n 行
# - index：返回索引对象
# - name：返回对象的名称
# - T：转置对象
# - shape：返回表示 DataFrame 的维度的元组

lst = ['python', 'c++', 'c#', 'java']
ser = Series(lst, index=['a', 'b', 'c', 'd'])

# 行轴标签
# 返回的是一个 list 对象，list 中的元素是索引对象的值
# 索引对象的长度为 1，表示 Series 对象只有一行
print(ser.axes)
# 数据类型
# 返回的是一个 numpy.dtype 对象，表示 Series 对象中元素的数据类型
print(ser.dtype)
# 空对象，这里的空对象是指 Series 对象中没有元素
# 返回的是一个 bool 对象，如果 Series 对象为空，则返回 True，否则返回 False
print(ser.empty)
# 维度
# 返回的是一个 int 对象，如果 Series 对象为空，则返回 0，否则返回 1
print(ser.ndim)
# 元素个数
# 返回的是一个 int 对象，表示 Series 对象中元素的个数
print(ser.size)
# 值
# 返回的是一个 numpy.ndarray 对象，表示 Series 对象中的值
print(ser.values)
# 前 n 行
# 返回的是一个 Series 对象，表示 Series 对象的前 n 行
print(ser.head())
# 后 n 行
# 返回的是一个 Series 对象，表示 Series 对象的后 n 行
print(ser.tail())
# 索引对象
# 返回的是一个 Index 对象，表示 Series 对象的索引对象
print(ser.index)
# 对象名称
# 返回的是一个 str 对象，表示 Series 对象的名称
print(ser.name)