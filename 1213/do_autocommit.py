import mysql.connector

# autocommit 自动提交，不自动提交，需要手动提交
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="guihua.pgh",
    port=3306,
    database='test',
    autocommit=True
)

mycursor = mydb.cursor()
mycursor.execute("insert into city(name)values('北京')")
mycursor.execute("insert into city(name)values('上海')")