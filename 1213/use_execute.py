import time
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="guihua.pgh",  # 数据库密码
    port=3306,  # 数据库端口，默认3306
    database='test' # 数据库名称
)

sql = "insert into user(name, age) values ('小明', 14)"

t1 = time.time()
mycursor = mydb.cursor()            # 创建cursor
for i in range(100000):
    mycursor.execute(sql)
mydb.commit()                       # 提交
t2 = time.time()

print(t2-t1)        # 68.127