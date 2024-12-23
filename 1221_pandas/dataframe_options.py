import pandas as pd

# pandas 的常用配置项：
# - display.max_rows：显示的最多行数
# - display.max_columns：显示的最多列数
# - display.expand_frame_repr：显示完整的 DataFrame 信息
# - display.max_colwidth：显示的最大列宽
# - display.precision：显示的精度
# - display.float_format：浮点数的格式
# - display.colheader_justify：列头的对齐方式
# 修改配置项的常用方法：
# - pd.get_option()：获取配置项的值
# - pd.set_option()：设置配置项的值
# - pd.reset_option()：重置配置项的值
# - pd.describe_option()：查看配置项的描述信息
# - pd.option_context()：临时设置配置项的值

# pandas 中默认的最大行数是 60 行，默认的最大列数是 20 列
print("display.max_rows = ", pd.get_option("display.max_rows"))
# 设置最大行数为 20
pd.set_option('display.max_rows', 20)
print("display.max_rows = ", pd.get_option("display.max_rows"))

# 重置最大行数
pd.reset_option('display.max_rows')
print("display.max_rows = ", pd.get_option("display.max_rows"))

# 查看最大行数的描述信息
pd.describe_option('display.max_rows')

# 临时设置最大行数
with pd.option_context('display.max_rows', 20):
    print(pd.get_option('display.max_rows'))