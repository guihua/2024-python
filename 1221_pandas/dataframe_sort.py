import pandas as pd

# 定义一个列表，列表中包含两个字典，每个字典包含三个键值对，键为字符串，值为整数
data1 = [
    {'2020-01-03': 7, '2020-01-02': 8, '2020-01-01': 4},
    {'2020-01-03': -4, '2020-01-02': -2, '2020-01-01':-9},
]

# 通过列表创建 DataFrame 对象，行索引默认为从 0 开始的整数序列，列索引为字典的键
# 注意：行索引和列索引的名称是可选的，不指定也可以
df = pd.DataFrame(data1, index=['最高温', '最低温'], columns=['2020-01-03', '2020-01-02', '2020-01-01'])
print(df)
print("*"*20)

# 按行索引排序，axis=0 表示按行索引排序，axis=1 表示按列索引排序
sorted_df = df.sort_values(axis=1, by='最高温')
print(sorted_df)
print("*"*20)

sorted_df = df.sort_values(axis=1, by='最高温', kind='mergesort')
print(sorted_df)