import pandas as pd

# 定义一个列表，列表中包含四个字典，每个字典包含三个键值对，键为字符串，值为整数
data = [
    {'语文': 90, '数学': 92, 'id': 1},
    {'语文': 98, '数学': 87, 'id': 2},
    {'语文': 87, '数学': 90, 'id': 3},
    {'语文': 90, '数学': 98, 'id': 4},
]
# 通过列表创建 DataFrame 对象，行索引默认为从 0 开始的整数序列，列索引为字典的键
df = pd.DataFrame(data, index=['小明', '小红', '小刚', '小丽'])
# 设置行索引的名称为姓名，列索引的名称为科目
# 注意：行索引和列索引的名称是可选的，不指定也可以
df.index.name = '姓名'
df.columns.name = '科目'

# 遍历 DataFrame，先遍历列，再遍历行
for col in df:
    print(col, df[col])
    print("*"*20)

# 采用 iteritems() 方法遍历 DataFrame，先遍历列，再遍历行
# iteritems() 方法返回的是一个迭代器，迭代器中的每个元素是一个元组，元组的第一个元素是列名，第二个元素是列数据
# TODO
# 运行报错：AttributeError: 'DataFrame' object has no attribute 'iteritems'
# for key, value in df.iteritems():
#    print(key, value)
#    print("*"*20)

# 采用 iterrows() 方法遍历 DataFrame，先遍历行，再遍历列
# iterrows() 方法返回的是一个迭代器，迭代器中的每个元素是一个元组，元组的第一个元素是行索引，第二个元素是行数据
for row_index, row in df.iterrows():
   print(row_index, row)
   print("*"*20)

# 采用 itertuples() 方法遍历 DataFrame，先遍历行，再遍历列
# itertuples() 方法返回的是一个迭代器，迭代器中的每个元素是一个元组，元组的第一个元素是行索引，第二个元素是行数据
# itertuples() 方法返回的是一个命名元组，命名元组的第一个元素是行索引，第二个元素是行数据
for row in df.itertuples():
   print(row, type(row))
   print("*"*20)