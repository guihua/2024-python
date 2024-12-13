# mysql.connector 是一个 Python 模块，用于连接和操作 MySQL 数据库。它提供了一系列的函数和方法，使得开发者可以方便地与 MySQL 数据库进行交互，执行查询、插入、更新和删除等操作
# 安装：pip install mysql-connector-python
import mysql.connector

# 打开数据库连接
mydb = mysql.connector.connect(
    host="localhost",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="guihua.pgh",  # 数据库密码
    port=3306,  # 数据库端口，默认3306
    database='test' # 数据库名称
)

sqls = [
    "insert into city(name)values('北京')",
    "insert into city(name)values('上海')",
    "insert into city(name)values('广州')",
    "insert into city(name)values('深圳')",
]

# 获得游标
# 游标（Cursor）是与数据库进行交互的对象，它允许执行 SQL 查询并获取结果。通过游标，我们可以执行各种 SQL 语句，如查询、插入、更新和删除数据。
mycursor = mydb.cursor()

for sql in sqls:
    # execute() 方法用于执行 SQL 语句
    # 语法：cursor.execute(sql, params=None)
    # 参数：
    # sql: 要执行的 SQL 语句，可以包含占位符（%s、%d、%f 等）
    # params: 可选参数，用于替换 SQL 语句中的占位符，以防止 SQL 注入攻击
    mycursor.execute(sql)

# 提交事务
# 提交事务是指将数据库中的数据永久保存到磁盘上，以确保数据的完整性和一致性。在执行 INSERT、UPDATE 或 DELETE 等操作后，需要调用 commit() 方法来提交事务，以确保这些操作的结果被永久保存到数据库中。
mydb.commit()
# 关闭数据库连接
mydb.close()