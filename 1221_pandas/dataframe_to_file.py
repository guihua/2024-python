import pandas as pd

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
# 保存到文件
# to_csv() 方法可以将 DataFrame 对象保存到文件中，文件的格式为 CSV 格式，文件的名称为 stu.csv
# to_csv() 方法的参数可以是一个字符串，也可以是一个文件对象，也可以是一个路径对象
# encoding 参数用于指定文件的编码格式，默认为 utf-8
df.to_csv('./1221_pandas/stu.csv', encoding='utf-8')
# 保存到文件
# to_excel() 方法可以将 DataFrame 对象保存到文件中，文件的格式为 Excel 格式，文件的名称为 stu.xls
# to_excel() 方法的参数可以是一个字符串，也可以是一个文件对象，也可以是一个路径对象
# sheet_name 参数用于指定 Excel 文件中的工作表名称，默认为 Sheet1
df.to_excel('./1221_pandas/stu.xlsx', sheet_name='考试成绩')
# 保存到文件
# to_json() 方法可以将 DataFrame 对象保存到文件中，文件的格式为 JSON 格式，文件的名称为 stu.json
# to_json() 方法的参数可以是一个字符串，也可以是一个文件对象，也可以是一个路径对象
# force_ascii 参数用于指定是否将非 ASCII 字符转换为 ASCII 字符，默认为 True
df.to_json('./1221_pandas/stu.json', force_ascii=False)
# 读取文件
# read_json() 方法可以从文件中读取 JSON 格式的数据，返回的是一个 DataFrame 对象
# read_json() 方法的参数可以是一个字符串，也可以是一个文件对象，也可以是一个路径对象
df = pd.read_json('./1221_pandas/stu.json')
print(df)