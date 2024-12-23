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

# 保存到 csv 文件
# to_csv() 方法可以将 DataFrame 对象保存到文件中，文件的格式为 CSV 格式，文件的名称为 stu.csv
# to_csv() 方法的参数可以是一个字符串，也可以是一个文件对象，也可以是一个路径对象
# encoding 参数用于指定文件的编码格式，默认为 utf-8
df.to_csv('./1221_pandas/stu.csv', encoding='utf-8')

# 读取 csv 文件
# read_csv() 方法可以从文件中读取 CSV 格式的数据，返回的是一个 DataFrame 对象
# read_csv() 方法的参数可以是一个字符串，也可以是一个文件对象，也可以是一个路径对象
# index_col 参数用于指定 DataFrame 对象的索引列，默认为 None
# encoding 参数用于指定文件的编码格式，默认为 utf-8
df = pd.read_csv('./1221_pandas/stu.csv')
# 设置行索引的名称为姓名，列索引的名称为科目
# inplace 参数用于指定是否在原 DataFrame 对象上修改，默认为 False
df.set_index('姓名', inplace=True)
print(df)
print("*" * 50)

# 读取 csv 文件
# read_table() 方法可以从文件中读取表格格式的数据，返回的是一个 DataFrame 对象
# read_table() 方法的参数可以是一个字符串，也可以是一个文件对象，也可以是一个路径对象
df = pd.read_table('./1221_pandas/stu.csv')
print(df)
print("*" * 50)

# 保存到 excel 文件
# to_excel() 方法可以将 DataFrame 对象保存到文件中，文件的格式为 Excel 格式，文件的名称为 stu.xls
# to_excel() 方法的参数可以是一个字符串，也可以是一个文件对象，也可以是一个路径对象
# sheet_name 参数用于指定 Excel 文件中的工作表名称，默认为 Sheet1
df.to_excel('./1221_pandas/stu.xlsx', sheet_name='考试成绩')

# 读取 excel 文件
# read_excel() 方法可以从文件中读取 Excel 格式的数据，返回的是一个 DataFrame 对象
# read_excel() 方法的参数可以是一个字符串，也可以是一个文件对象，也可以是一个路径对象
df = pd.read_excel('./1221_pandas/stu.xlsx')
print(df)
print("*" * 50)

# 保存到 json 文件
# to_json() 方法可以将 DataFrame 对象保存到文件中，文件的格式为 JSON 格式，文件的名称为 stu.json
# to_json() 方法的参数可以是一个字符串，也可以是一个文件对象，也可以是一个路径对象
# force_ascii 参数用于指定是否将非 ASCII 字符转换为 ASCII 字符，默认为 True
df.to_json('./1221_pandas/stu.json', force_ascii=False)

# 读取 json 文件
# read_json() 方法可以从文件中读取 JSON 格式的数据，返回的是一个 DataFrame 对象
# read_json() 方法的参数可以是一个字符串，也可以是一个文件对象，也可以是一个路径对象
df = pd.read_json('./1221_pandas/stu.json')
print(df)
print("*" * 50)

# 保存到 pickle 文件
# to_pickle() 方法可以将 DataFrame 对象保存到文件中，文件的格式为 pickle 格式，文件的名称为 stu.data
# to_pickle() 方法的参数可以是一个字符串，也可以是一个文件对象，也可以是一个路径对象
df.to_pickle('./1221_pandas/stu.data')

# 读取 pickle 文件
# read_pickle() 方法可以从文件中读取 pickle 格式的数据，返回的是一个 DataFrame 对象
# read_pickle() 方法的参数可以是一个字符串，也可以是一个文件对象，也可以是一个路径对象
df = pd.read_pickle('./1221_pandas/stu.data')
print(df)
print("*" * 50)

# 保存到 html 文件
# to_html() 方法可以将 DataFrame 对象保存到文件中，文件的格式为 HTML 格式，文件的名称为 stu.html
# to_html() 方法的参数可以是一个字符串，也可以是一个文件对象，也可以是一个路径对象
df.to_html('./1221_pandas/stu.html')

# 读取 html 文件
# read_html() 方法可以从文件中读取 HTML 格式的数据，返回的是一个 DataFrame 对象的列表
# read_html() 方法的参数可以是一个字符串，也可以是一个文件对象，也可以是一个路径对象
# encoding 参数用于指定文件的编码格式，默认为 utf-8
df = pd.read_html('./1221_pandas/stu.html', encoding='utf-8')
print(df)