import pandas as pd

# Excel 文件列表
file_lst = ["./data/一组人员信息.xlsx", "./data/二组人员信息.xlsx", "./data/三组人员信息.xlsx"]
# 读取 Excel 文件
# read_excel() 方法可以从文件中读取 Excel 格式的数据，返回的是一个 DataFrame 对象
# read_excel() 方法的参数可以是一个字符串，也可以是一个文件对象，也可以是一个路径对象
# 列表推导式，遍历文件列表，读取每个文件，返回的是一个 DataFrame 对象的列表
excels = [pd.read_excel(file) for file in file_lst]
# 合并 DataFrame 对象
# concat() 方法可以将多个 DataFrame 对象合并为一个 DataFrame 对象，返回的是一个 DataFrame 对象
# concat() 方法的参数可以是一个列表，列表中的元素是 DataFrame 对象，返回的是一个 DataFrame 对象
# concat() 方法的参数，包括：
# - objs：一个列表，列表中的元素是 DataFrame 对象
# - axis：默认为 0，表示按行拼接，1 表示按列拼接
df = pd.concat(excels)
# 保存 DataFrame 对象到 Excel 文件
# to_excel() 方法可以将 DataFrame 对象保存到 Excel 文件中，返回的是一个 None 对象
# to_excel() 方法的参数可以是一个字符串，也可以是一个文件对象，也可以是一个路径对象
# index 参数用于指定是否保存行索引，默认为 True
df.to_excel("./data/人员信息汇总.xlsx", index=False)