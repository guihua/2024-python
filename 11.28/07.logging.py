import logging

# 配置日志记录的基本设置，将日志级别设置为 INFO
# level 有 debug，info，warning，error 几个级别
logging.basicConfig(level=logging.INFO)

# 定义一个字符串 s，其值为 "0"
s = "0"
# 将字符串 s 转换为整数，并存储在变量 n 中
n = int(s)
# 使用日志记录器记录变量 n 的值，日志级别为 INFO
logging.info("n = %d" % n)
# 尝试将 10 除以 n，并打印结果
print(10 / n)
