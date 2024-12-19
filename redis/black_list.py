import time
from random import sample
from redis.client import Redis

# 创建Redis客户端
r = Redis(host='127.0.0.1', port=6379, db=0, password='guihua.pgh')

# 创建数据，存入集合
def create_data_for_mget():
    # 存入数据，key为 black::i，value为1
    for i in range(10000, 50001):
        key = f'black::{i}'
        r.set(key, 1)

# 测试查询数据的时间
def test_mget_ex(count):
    lst = sample(range(10000, 50001), count)
    t1 = time.time()
    for i in range(10):
        # mget 命令的参数是一个列表，列表中的元素是 key，返回值是一个列表，列表中的元素是 key 的值
        res = r.mget([f'black::{item}' for item in lst])
    t2 = time.time()

    print(f'批量查询{count}个key耗时: ' + str((t2-t1)/10))

def test_mget():
    test_mget_ex(5)
    test_mget_ex(10)
    test_mget_ex(50)
    test_mget_ex(100)
    test_mget_ex(200)
    test_mget_ex(300)
    test_mget_ex(400)
    test_mget_ex(500)
    test_mget_ex(600)
    test_mget_ex(700)
    test_mget_ex(800)
    test_mget_ex(900)
    test_mget_ex(1000)
    test_mget_ex(1500)
    test_mget_ex(2000)

test_mget()