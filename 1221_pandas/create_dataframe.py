import pandas as pd

# DataFrame 是 Pandas 库中的一种数据结构，它类似于二维数组，可以存储任何类型的数据，如整数、字符串、浮点数等。
# DataFrame 对象由行索引（index）、列索引（columns）和数据（data）三部分组成。
# DataFrame 对象的基本语法格式如下：
# pandas.DataFrame(data, index, columns, dtype, copy)
# 参数说明：
# data：可以是列表、字典、Series、ndarray、DataFrame 等数据类型。
# index：行索引，默认为从 0 开始的整数序列。
# columns：列索引，默认为从 0 开始的整数序列。
# dtype：数据类型，默认为 None。
# copy：是否复制数据，默认为 False。

# 创建一个空的 DataFrame 对象，不传入任何参数，行索引和列索引默认为空
df = pd.DataFrame()
print(df)
print("*" * 50)

# 定义一个字典，包含两个键值对，每个键值对的值是一个列表，列表中的元素为整数
data = {
    '语文': [90, 98, 87, 90],
    '数学': [92, 87, 90, 98]
}
# 通过字典创建 DataFrame 对象
# 索引默认为从 0 开始的整数序列，列索引为字典的键
df = pd.DataFrame(data)
print(df)
print("*" * 50)

df = pd.DataFrame(data, index=['小明', '小红', '小刚', '小丽'])
print(df)
print("*" * 50)

# 定义一个列表，列表中包含四个字典，每个字典包含两个键值对，键为字符串，值为整数
data = [
    {'语文': 90, '数学': 92},
    {'语文': 98, '数学': 87},
    {'语文': 87, '数学': 90},
    {'语文': 90, '数学': 98},
]
# 通过列表创建 DataFrame 对象，行索引默认为从 0 开始的整数序列，列索引为字典的键
# 注意：字典的键必须一致，否则会报错
df = pd.DataFrame(data, index=['小明', '小红', '小刚', '小丽'])
print(df)
print("*" * 50)

# 通过列表创建 DataFrame 对象，columns 参数指定列索引
# 注意：columns 参数必须包含所有的列名，否则会报错
df = pd.DataFrame(data, index=['小明', '小红', '小刚', '小丽'], columns=['语文'])
print(df)
print("*" * 50)

# 定义一个字典，包含两个键值对，每个键值对的值是一个 Series 对象，索引为指定的列表
# Series 对象的索引为指定的列表，值为指定的整数
# 两个 Series 对象的索引不一致，会自动对齐，缺失的值用 NaN 表示；小丽的数学成绩缺失，用 NaN 表示
data = {
    '语文': pd.Series([90, 98, 87], index=['小明', '小红', '小刚']),
    '数学': pd.Series([92, 87, 90, 98], index=['小明', '小红', '小刚', '小丽'])
}
# 通过字典创建 DataFrame 对象
df = pd.DataFrame(data)
print(df)
print("*" * 50)

# 用已经存在的 DataFrame 对象创建新的 DataFrame 对象，index 参数指定行索引
# index 中删除了小丽，新的 DataFrame 对象中不会包含小丽的成绩
df_2 = pd.DataFrame(df, index=['小明', '小红', '小刚'])
print(df_2)