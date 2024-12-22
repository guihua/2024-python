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
# print(df)
# 通过列索引获取列数据，返回的是一个Series对象，索引为行索引，值为列数据
print(df['语文'])
print('*'*50)

# 通过求和计算总分，并将总分添加到DataFrame对象中，列索引为'总分'，值为数学和语文的和
# df['总分'] = df.sum(axis=1)
# print(df)
df['总分'] = df['数学'] + df['语文']
print(df)
print('*'*50)

# 删除列
# del 关键字可以删除DataFrame对象的列，删除后的DataFrame对象将不再包含该列
# del df['语文']
# pop() 方法可以删除DataFrame对象的列，删除后的DataFrame对象将不再包含该列
# df.pop('数学')
# print(df)

# DataFrame 切片，返回的是一个DataFrame对象，包含了DataFrame对象的指定行
print(df[1:3])
# 切片的类型为DataFrame对象
print(type(df[1:3]))
print('*'*50)

# 添加行，返回的是一个DataFrame对象，包含了DataFrame对象的指定行
df2 = pd.DataFrame([{'语文': 100, '数学': 100}], index=['学霸'])
# append() 方法可以将DataFrame对象的指定行添加到DataFrame对象中，添加后的DataFrame对象将包含该行
# append() 方法返回的是一个DataFrame对象，包含了DataFrame对象的指定行
# 在较新的 pandas 版本中（1.4.0 及更高版本），DataFrame.append() 方法已被弃用，并最终在后续版本中移除。官方建议使用 pd.concat() 方法来代替 append() 方法。
# df = df.append(df2)
df = df._append(df2)
print(df)
print('*'*50)

# loc 属性用于通过标签获取 DataFrame 对象的行数据，返回的是一个 Series 对象
# loc 属性返回的是一个 Series 对象，索引为列索引，值为行数据
# loc 属性的参数可以是一个标签，也可以是一个标签列表
# loc 属性的参数可以是一个切片，也可以是一个布尔表达式
# loc 属性的参数可以是一个布尔表达式，返回的是一个 DataFrame 对象，包含了符合条件的行数据
# loc 属性的参数可以是一个函数，返回的是一个 DataFrame 对象，包含了函数返回值为 True 的行数据
# loc 属性的参数可以是一个字典，返回的是一个 DataFrame 对象，包含了字典的值为 True 的行数据
# loc 属性的参数可以是一个列表，返回的是一个 DataFrame 对象，包含了列表中的元素为 True 的行数据
# loc 属性的参数可以是一个元组，返回的是一个 DataFrame 对象，包含了元组中的元素为 True 的行数据
# loc 属性的参数可以是一个集合，返回的是一个 DataFrame 对象，包含了集合中的元素为 True 的行数据
# loc 属性的参数可以是一个 Series 对象，返回的是一个 DataFrame 对象，包含了 Series 对象的值为 True 的行数据
# loc 属性的参数可以是一个 DataFrame 对象，返回的是一个 DataFrame 对象，包含了 DataFrame 对象的值为 True 的行数据
print(df.loc['小明'])

# iloc 属性用于通过位置获取 DataFrame 对象的行数据，返回的是一个 Series 对象
# iloc 属性的参数可以是一个整数，也可以是一个整数列表，返回的是一个 DataFrame 对象，包含了指定位置的行数据
print(df.iloc[0])
print('*'*50)

# drop() 方法可以删除DataFrame对象的行，删除后的DataFrame对象将不再包含该行
# drop() 方法的参数可以是一个标签，也可以是一个标签列表，返回的是一个DataFrame对象，包含了删除后的行数据
# inplace 参数用于指定是否在原DataFrame对象上进行操作，默认为False，即不修改原DataFrame对象，而是返回一个新的DataFrame对象
df.drop('小明', inplace=True)
print(df)