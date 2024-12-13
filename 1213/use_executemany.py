import time
import mysql.connector

# 第一步，创建连接
mydb = mysql.connector.connect(
    host="localhost",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="guihua.pgh",  # 数据库密码
    port=3306,  # 数据库端口，默认3306
    database='test' # 数据库名称
)

sql = "insert into user(name, age) values (%s,%s)"

citys = [
    ('小明', 14) for i in range(100000)
]

t1 = time.time()
mycursor = mydb.cursor()
# executemany() 方法用于执行多个 SQL 语句，以提高执行效率
# 语法：cursor.executemany(sql, params)
# 参数：
# sql: 要执行的 SQL 语句，可以包含占位符（%s、%d、%f 等）
# params: 可选参数，用于替换 SQL 语句中的占位符，以防止 SQL 注入攻击
mycursor.executemany(sql, citys)
mydb.commit()
t2 = time.time()

print(t2-t1)