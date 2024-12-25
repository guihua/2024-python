import pandas as pd
from sqlalchemy import create_engine

# 建立连接
# create_engine 函数用于创建数据库连接，参数为数据库连接字符串，echo 参数用于控制是否输出日志信息。
# sqlite:// 表示使用 SQLite 数据库，:memory: 表示使用内存数据库，echo=True 表示输出日志信息。
engine = create_engine('sqlite:///1225/mydb', echo=True)

# 读取csv文件
# read_csv 函数用于读取 csv 文件，参数为文件路径，返回一个 DataFrame 对象。
df = pd.read_csv("./1225/population_total.csv")
# 写入数据库
# to_sql 函数用于将 DataFrame 对象写入数据库，参数为表名和连接对象。
df.to_sql("population", con=engine)
