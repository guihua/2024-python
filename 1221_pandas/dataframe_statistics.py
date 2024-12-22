import pandas as pd

# 定义列表，列表中的元素是字典，字典的键是列名，值是列值
data = [
    {'语文': 90, '数学': 92},
    {'语文': 98, '数学': 87},
    {'语文': 87, '数学': 90},
    {'语文': 90, '数学': 98},
]
# 创建DataFrame对象，行索引为指定的列表，列索引为字典的键
df = pd.DataFrame(data, index=['小明', '小红', '小刚', '小丽'])
# 设置行索引和列索引的名称
df.index.name = '姓名'
df.columns.name = '科目'
# 按列求和
# axis=0 表示按列求和，axis=1 表示按行求和
# sum() 方法返回的是一个Series对象，索引为列索引，值为每列的和
print(df.sum(axis=0))
# 按列求平均值
# axis=0 表示按列求平均值，axis=1 表示按行求平均值
# mean() 方法返回的是一个Series对象，索引为列索引，值为每列的平均值
print(df.mean(axis=0))
# 按列求中位数
# axis=0 表示按列求中位数，axis=1 表示按行求中位数
# median() 方法返回的是一个Series对象，索引为列索引，值为每列的中位数
print(df.median(axis=0))
# 按列求最小值
# axis=0 表示按列求最小值，axis=1 表示按行求最小值
# min() 方法返回的是一个Series对象，索引为列索引，值为每列的最小值
print(df.min(axis=0))
# 按列求最大值
# axis=0 表示按列求最大值，axis=1 表示按行求最大值
# max() 方法返回的是一个Series对象，索引为列索引，值为每列的最大值
print(df.max(axis=0))
# 求绝对值
# abs() 方法返回的是一个DataFrame对象，绝对值后的DataFrame对象的行索引和列索引与原DataFrame对象相同
print(df.abs())
# 描述性统计
# describe() 方法返回的是一个DataFrame对象，包含了DataFrame对象的统计信息，包括计数、平均值、标准差、最小值、最大值、四分位数等
# 行索引为统计信息的名称，列索引为DataFrame对象的列索引
print(df.describe())
print("*"*50)
print(df.sum(axis=1))
print(df.mean(axis=1))
print(df.median(axis=1))
print(df.min(axis=1))
print(df.max(axis=1))