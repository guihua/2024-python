import mysql.connector

# 第一步，创建连接
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="guihua.pgh",
    port=3306,
    database='test'
)

# sql 语句
# update 表名 set 字段名=值 where 条件
sql = "update city set name='beijing' where id = 1"

# 第二步，创建cursor
mycursor = mydb.cursor()

# 第三步，执行sql
mycursor.execute(sql)

# 第四步，提交数据
mydb.commit()

# 第五步，关闭连接
mydb.close()