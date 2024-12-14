from mysql.connector.pooling import MySQLConnectionPool

# 第一步，创建连接
mysql_pool = MySQLConnectionPool(
    host="localhost",
    user="root",
    passwd="guihua.pgh",
    port=3306,
    database='test',
    pool_size= 5
)

# 查询数据
# select * from 表名
sql = "select * from city"

# 第二步，从连接池中获取一个连接
# 连接池会自动判断连接是否可用，如果可用，直接返回，如果不可用，会等待一段时间，直到获取到可用的连接
# get_connection() 方法会返回一个连接对象，连接对象是一个上下文管理器，使用 with 语句可以自动关闭连接
conn = mysql_pool.get_connection()

# 第三步，创建cursor
cursor = conn.cursor()

# 第四步，执行sql
cursor.execute(sql)

# 第五步，获取数据
for data in cursor.fetchall():
    print(data)

# 第六步，关闭连接
cursor.close()

# 第七步，关闭连接池
conn.close()