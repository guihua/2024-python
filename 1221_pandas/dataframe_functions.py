import pandas as pd
import numpy as np

data = [
    {'语文': 90, '数学': 92},
    {'语文': 98, '数学': 87},
    {'语文': 87, '数学': 90},
    {'语文': 90, '数学': 98},
]

# 添加总分列，并返回新的 DataFrame 对象
def add_sum_column(df):
    # 复制 DataFrame 对象
    # cop() 方法返回的是一个 DataFrame 对象，包含了原来 DataFrame 对象的行数据和列数据
    # copy() 方法的参数可以是一个布尔值，默认为 True，表示复制原来的 DataFrame 对象，False 表示不复制原来的 DataFrame 对象
    # copy() 方法的参数可以是一个字典，字典的键是列索引，值是布尔值，表示是否复制该列
    result = df.copy()
    # 获取列索引
    # tolist() 方法将 DataFrame 对象的列索引转换为列表，返回的是一个列表对象
    columns = result.columns.tolist()

    if '平均值' in columns:
        # 删除平均值列
        columns.remove('平均值')
    # 添加总分列
    result['总分'] = result[columns].sum(axis=1)

    return result

# 添加平均值列
def add_mean_column(df):
    result = df.copy()
    columns = result.columns.tolist()
    if '总分' in columns:
        columns.remove('总分')
    result['平均值'] = result[columns].mean(axis=1)
    return result

# 创建 DataFrame 对象，行索引为指定的列表，列索引为字典的键
df = pd.DataFrame(data, index=['小明', '小红', '小刚', '小丽'])
df_sum = add_sum_column(df)
df_mean = add_mean_column(df_sum)

print(df_mean)
print("*" * 50)

data2 = [
    {'语文': 90, '数学': 92},
    {'语文': 98, '数学': 87},
    {'语文': 87, '数学': 90},
    {'语文': 90, '数学': 98},
]

df = pd.DataFrame(data2, index=['小明', '小红', '小刚', '小丽'])
# 逐行进行操作, 求语文和数学的平均值
# apply 方法返回的是一个 Series 对象，包含了原来 DataFrame 对象的行索引和计算结果
# apply 方法的参数可以是一个函数，也可以是一个匿名函数，也可以是一个 lambda 表达式
# apply 方法的参数可以是一个字典，字典的键是列索引，值是函数，返回的是一个 DataFrame 对象，包含了原来 DataFrame 对象的行索引和计算结果
print(df.apply(np.mean))
# 逐列进行操作, 求每个学生的各科平均值
print(df.apply(np.mean, axis=1))