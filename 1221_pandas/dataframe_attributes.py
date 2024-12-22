import pandas as pd

# DataFrame 对象的属性，包括：
# axes：获取 DataFrame 对象的行索引和列索引。
# dtypes：获取 DataFrame 对象中每一列的数据类型。
# empty：判断 DataFrame 对象是否为空。
# ndim：获取 DataFrame 对象的维度。
# shape：获取 DataFrame 对象的形状。
# size：获取 DataFrame 对象的元素个数。
# values：获取 DataFrame 对象中的值，返回的是一个二维的 ndarray 对象。
# head()：获取 DataFrame 对象的前 n 行，返回的是一个 DataFrame 对象。
# tail()：获取 DataFrame 对象的后 n 行，返回的是一个 DataFrame 对象。
# T：将 DataFrame 对象转置，行变成列，列变成行。

# 定义一个列表，列表中包含四个字典，每个字典包含两个键值对，键为字符串，值为整数
data = [
    {'语文': 90, '数学': 92},
    {'语文': 98, '数学': 87},
    {'语文': 87, '数学': 90},
    {'语文': 90, '数学': 98},
]
# 通过列表创建 DataFrame 对象，指定行索引，列索引默认为字典的键
df = pd.DataFrame(data, index=['小明', '小红', '小刚', '小丽'])
# 设置行索引的名称为姓名，列索引的名称为科目
# 注意：行索引和列索引的名称是可选的，不指定也可以
df.index.name = '姓名'
df.columns.name = '科目'
print(df)
# axes 属性用于获取 DataFrame 对象的行索引和列索引
# 返回的是一个列表，列表中包含两个元素，第一个元素是行索引，第二个元素是列索引
# 行索引和列索引都是 Index 对象，Index 对象是一个序列，序列中的元素是索引对象的值
print(df.axes)
# dtypes 属性用于获取 DataFrame 对象中每一列的数据类型，返回的是一个 Series 对象
print(df.dtypes)
# empty 属性用于判断 DataFrame 对象是否为空，返回的是一个布尔值
# 如果 DataFrame 对象为空，则返回 True，否则返回 False
print(df.empty)
# ndim 属性用于获取 DataFrame 对象的维度，返回的是一个整数
# DataFrame 对象是二维的，所以返回的是 2
print(df.ndim)
# shape 属性用于获取 DataFrame 对象的形状，返回的是一个元组
# 元组中的第一个元素是行数，第二个元素是列数
print(df.shape)
# size 属性用于获取 DataFrame 对象的元素个数，返回的是一个整数
# DataFrame 对象的元素个数等于行数乘以列数
print(df.size)
# values 属性用于获取 DataFrame 对象中的值，返回的是一个二维的 ndarray 对象
# ndarray 对象是一个数组，数组中的元素是 DataFrame 对象的值
print(df.values)
# type() 函数用于获取对象的类型，返回的是一个类型对象
print(type(df.values))
# head() 方法用于获取 DataFrame 对象的前 n 行，返回的是一个 DataFrame 对象
# 默认返回前 5 行
print(df.head(2))
# tail() 方法用于获取 DataFrame 对象的后 n 行，返回的是一个 DataFrame 对象
# 默认返回后 5 行
print(df.tail(2))
print("*"*20)

# T 属性用于倒置 DataFrame 对象，行变成列，列变成行
# 行索引变成列索引，列索引变成行索引
reversed_df = df.T
print(reversed_df)
print(reversed_df.axes)
print(df.dtypes)
print("*"*20)
