from pandas import Series

# 创建字典对象，键为字符串，值为整数
score_dict = {
    'c++': 99,
    'python': 100,
    'c#': 98,
    'java': 97
}

# 通过字典创建 Series 对象，索引默认为字典的键，值为字典的值，索引的顺序为字典的键的顺序
ser = Series(score_dict)

# 将 Series 对象转换为列表
# tolist() 方法将 Series 对象转换为列表，返回的是一个列表对象
# 列表的元素为 Series 对象的值
print(ser.tolist())
# 将 Series 对象转换为字典
# to_dict() 方法将 Series 对象转换为字典，返回的是一个字典对象
# 字典的键为 Series 对象的索引，值为 Series 对象的值
# 字典的键的类型为字符串，值的类型为 Series 对象的值的类型
print(ser.to_dict())

# 将 Series 对象转换为 DataFrame 对象
# to_excel() 方法将 Series 对象转换为 DataFrame 对象，然后将 DataFrame 对象写入到 Excel 文件中
ser.to_excel('./1221_pandas/data.xlsx')