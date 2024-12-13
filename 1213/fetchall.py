import mysql.connector

# 第一步，创建连接
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="guihua.pgh",
    port=3306,
    database='test'
)
sql = "select * from city"
# 第二步，创建cursor
mycursor = mydb.cursor()
# 第三步，执行sql
mycursor.execute(sql)
# 第四步， fetchall 获取全部数据
# fetchall 是获取全部数据，fetchone 是获取一条数据，fetchmany 是获取多条数据
# fetchall() 返回的是一个列表，列表的每个元素是一个元组，元组的每个元素是一条数据的每个字段，元组的元素是按照字段的顺序排列的
datas = mycursor.fetchall()
for data in datas:
    print(data)

# fetchone() 返回的是一个元组，元组的每个元素是一条数据的每个字段，元组的元素是按照字段的顺序排列的
# data = mycursor.fetchone()
# print(data)

# fetchmany() 返回的是一个列表，列表的每个元素是一个元组，元组的每个元素是一条数据的每个字段，元组的元素是按照字段的顺序排列的
# mdata = mycursor.fetchmany()
# print(mdata)