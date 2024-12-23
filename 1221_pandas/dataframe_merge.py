import pandas as pd

# 定义一个列表，列表中包含四个字典，每个字典包含三个键值对，键为字符串，值为整数
data1 = [
    {'语文': 90, '数学': 92, 'id': 1},
    {'语文': 98, '数学': 87, 'id': 2},
    {'语文': 87, '数学': 90, 'id': 3},
    {'语文': 90, '数学': 98, 'id': 4},
]

# 通过列表创建 DataFrame 对象，行索引默认为从 0 开始的整数序列，列索引为字典的键
left_df = pd.DataFrame(data1, index=['小明', '小红', '小刚', '小丽'])
# 设置行索引的名称为姓名，列索引的名称为科目
left_df.index.name = '姓名'
left_df.columns.name = '科目'

# 定义一个列表，列表中包含四个字典，每个字典包含三个键值对，键为字符串，值为整数
data2 = [
    {'英语': 89, '物理': 98, 'id': 1},
    {'英语': 90, '物理': 90, 'id': 2},
    {'英语': 90, '物理': 97, 'id': 3},
    {'英语': 98, '物理': 94, 'id': 5},
]

# 通过列表创建 DataFrame 对象，行索引默认为从 0 开始的整数序列，列索引为字典的键
right_df = pd.DataFrame(data2, index=['小明', '小红', '小刚', '小王'])
# 设置行索引的名称为姓名，列索引的名称为科目
right_df.index.name = '姓名'
right_df.columns.name = '科目'

# merge() 方法返回的是一个新的 DataFrame 对象，包含了两个 DataFrame 对象的所有行和列
# merge() 方法的参数包括：
# left：要合并的左侧 DataFrame 对象
# right：要合并的右侧 DataFrame 对象
# how：合并的方式，默认为 inner，可选值为 inner、outer、left、right
# on：用于合并的列名，默认为 None，可选值为列名或列名列表
# left_on：左侧 DataFrame 对象用于合并的列名，默认为 None，可选值为列名或列名列表
# right_on：右侧 DataFrame 对象用于合并的列名，默认为 None，可选值为列名或列名列表
# left_index：左侧 DataFrame 对象是否使用行索引作为合并键，默认为 False，可选值为 True 或 False
# right_index：右侧 DataFrame 对象是否使用行索引作为合并键，默认为 False，可选值为 True 或 False
# sort：是否对合并后的 DataFrame 对象进行排序，默认为 True，可选值为 True 或 False
# suffixes：当两个 DataFrame 对象的列名相同时，用于区分列名的后缀，默认为 ('_x', '_y')，可选值为元组或列表
# copy：是否复制数据，默认为 True，可选值为 True 或 False

# 合并两个 DataFrame 对象，按照 id 列进行合并
# how 参数为 inner，表示合并的方式为内连接，即只包含两个 DataFrame 对象中都有的行和列
df = pd.merge(left_df, right_df, on='姓名', how='inner')
print(df)
print("*" * 50)

# how 参数为 outer，表示合并的方式为外连接，即包含两个 DataFrame 对象的所有行和列
df = pd.merge(left_df, right_df, how='outer', on='id')
print(df)
print("*" * 50)

# left_index 参数为 True，表示左侧 DataFrame 对象使用行索引作为合并键
# right_index 参数为 True，表示右侧 DataFrame 对象使用行索引作为合并键
df = pd.merge(left_df, right_df, how='outer', left_index=True, right_index=True)
print(df)
print("*" * 50)

# how 参数为 left，表示合并的方式为左连接，即只包含左侧 DataFrame 对象的所有行和列
df = pd.merge(left_df, right_df, how='left', left_index=True, right_index=True)
print(df)
print("*" * 50)

# how 参数为 right，表示合并的方式为右连接，即只包含右侧 DataFrame 对象的所有行和列
df = pd.merge(left_df, right_df, how='right', left_index=True, right_index=True)
print(df)
print("*" * 50)