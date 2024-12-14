import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="guihua.pgh",
    port=3306,
    database='test',
    autocommit=True
)

def add(city):
    mycursor = mydb.cursor()
    mycursor.execute(f"insert into city(name)values('{city}')")
    mycursor.close()

def get_count():
    mycursor = mydb.cursor()
    mycursor.execute("select count(1) as count from city")
    data = mycursor.fetchone()
    mycursor.close()
    if data[0] == 1:
        print(data, '抛出异常')
        raise Exception('抛出异常')

# start_transaction 开启事务
# 开启事务后，如果出现异常，需要回滚事务
mydb.start_transaction()

try:
    add('北京')
    get_count()
    mydb.commit()
except:
    mydb.rollback()