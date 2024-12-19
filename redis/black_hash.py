import time
from random import sample
from redis.client import Redis

# 创建Redis客户端
r = Redis(host='127.0.0.1', port=6379, db=0, password='guihua.pgh')

# 创建数据，存入哈希表
def create_data_for_hmget():
    for i in range(10000, 50001):
        key = f'black'
        # hset 命令的参数是哈希表的名称、键和值，返回值是成功添加的元素个数
        r.hset(key, f'black::{i}', 1)

def test_hmget_ex(count):
    lst = sample(range(10000, 50001), count)
    t1 = time.time()
    for i in range(10):
        # hmget 命令的参数是哈希表的名称和键，返回值是一个列表，列表中的元素是键的值
        # hmget 命令的返回值是一个列表，列表中的元素是键的值，元素的个数是键的个数
        res = r.hmget('black', [f'black::{item}' for item in lst])
    t2 = time.time()

    print(f'批量查询{count}个key耗时: ' + str((t2-t1)/10))

def test_hmget():
    test_hmget_ex(5)
    test_hmget_ex(10)
    test_hmget_ex(50)
    test_hmget_ex(100)
    test_hmget_ex(200)
    test_hmget_ex(300)
    test_hmget_ex(400)
    test_hmget_ex(500)
    test_hmget_ex(600)
    test_hmget_ex(700)
    test_hmget_ex(800)
    test_hmget_ex(900)
    test_hmget_ex(1000)
    test_hmget_ex(1500)
    test_hmget_ex(2000)
test_hmget()