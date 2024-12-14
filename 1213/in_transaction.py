import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="guihua.pgh",
    port=3306,
    database='test'
)

mycursor = mydb.cursor()
# in_transaction 查看是否在事务中，返回值为 0 或者 1，默认是 0
# 0 不在事务中，1 表示在事务中，在事务中执行的 sql 语句不会自动提交
# 只有在事务中执行的 sql 语句才会自动提交
print(mydb.in_transaction)
# insert 语句不会自动提交，需要手动提交
mycursor.execute("insert into city(name)values('北京')")
# 开启事务
print(mydb.in_transaction)
mycursor.execute("insert into city(name)values('上海')")
mydb.commit()
print(mydb.in_transaction)