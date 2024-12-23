import pandas as pd

# 定义列表，列表中包含四个字典，每个字典包含两个键值对，键为字符串，值为整数
data1 = {
    '语文': [90, 98, 87, 90],
    '数学': [92, 87, 90, 98]
}
# 通过列表创建 DataFrame 对象，行索引默认为从 0 开始的整数序列，列索引为字典的键
df1 = pd.DataFrame(data1, index=['小明', '小红', '小刚', '小丽'])

# 定义列表，列表中包含四个字典，每个字典包含两个键值对，键为字符串，值为整数
data2 = {
    '语文': [98, 95, 80, 98],
    '数学': [94, 92, 88, 94]
}
# 通过列表创建 DataFrame 对象，行索引默认为从 0 开始的整数序列，列索引为字典的键
df2 = pd.DataFrame(data2, index=['小林', '小李', '小张', '小王'])

# 将两个 DataFrame 对象进行拼接，拼接后的 DataFrame 对象的行索引为原来的行索引，列索引为原来的列索引
# concat() 方法返回的是一个 DataFrame 对象，包含了两个 DataFrame 对象的行数据
# concat() 方法的参数可以是一个列表，列表中的元素是 DataFrame 对象，返回的是一个 DataFrame 对象，包含了列表中所有 DataFrame 对象的行数据
# concat() 方法的参数，包括：
# - objs：一个列表，列表中的元素是 DataFrame 对象
# - axis：默认为 0，表示按行拼接，1 表示按列拼接
# - join：默认为 outer，表示外连接，inner 表示内连接
# - keys：一个列表，列表中的元素是字符串，用于给拼接后的 DataFrame 对象的行索引添加前缀
# - levels：一个列表，列表中的元素是列表，用于给拼接后的 DataFrame 对象的行索引添加多级索引
# - names：一个列表，列表中的元素是字符串，用于给拼接后的 DataFrame 对象的行索引添加名称
# - ignore_index：默认为 False，表示不忽略原来的行索引，True 表示忽略原来的行索引，重新生成行索引
# - verify_integrity：默认为 False，表示不检查行索引是否有重复，True 表示检查行索引是否有重复
# - sort：默认为 False，表示不排序，True 表示排序
# - copy：默认为 True，表示复制原来的 DataFrame 对象，False 表示不复制原来的 DataFrame 对象
df = pd.concat([df1, df2])
print(df)
print("*" * 50)

data3 = {
    '语文': [90, 98, 87, 90],
    '数学': [92, 87, 90, 98]
}
df3 = pd.DataFrame(data3, index=['小明', '小红', '小刚', '小丽'])

data4 = {
    '物理': [98, 95, 80, 98],
    '生物': [94, 92, 88, 94]
}
df4 = pd.DataFrame(data4, index=['小明', '小红', '小刚', '小王'])

# axis=1 表示按列拼接，join=“inner” 表示内连接
df = pd.concat([df3, df4], axis=1, join="inner")
print(df)