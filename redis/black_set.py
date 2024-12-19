import time
from random import sample
from redis.client import Redis

# 创建Redis客户端
r = Redis(host='127.0.0.1', port=6379, db=0, password='guihua.pgh')

# 创建数据，存入集合
def create_data_for_set():
    # 创建一个集合，存入 10000-50000 的数据
    for i in range(10000, 50001):
        # 将数据存入集合
        # sadd 命令的参数是集合的名称和元素，元素可以是一个或多个
        # sadd 命令的返回值是成功添加的元素个数
        r.sadd('black_set', i)

# 测试查询数据的时间
def test_set_ex(count):
    # 随机获取 count 个数据，存入一个列表
    # sample 函数的参数是一个序列和一个整数，返回一个列表，列表中的元素是序列中的元素，元素的个数是整数
    lst = sample(range(10000, 50001), count)
    t1 = time.time()

    for i in range(10):
        # 将数据存入一个新的集合
        r.sadd('black_set_2', *lst)
        # sinter 命令的参数是集合的名称，返回值是一个列表，列表中的元素是所有集合的交集
        res = r.sinter(['black_set', 'black_set_2'])
        # 删除临时集合
        r.delete('black_set_2')

    t2 = time.time()
    print(f'批量查询{count}个key耗时: ' + str((t2 - t1) / 10))

def test_set():
    test_set_ex(5)
    test_set_ex(10)
    test_set_ex(50)
    test_set_ex(100)
    test_set_ex(200)
    test_set_ex(300)
    test_set_ex(400)
    test_set_ex(500)
    test_set_ex(600)
    test_set_ex(700)
    test_set_ex(800)
    test_set_ex(900)
    test_set_ex(1000)
    test_set_ex(1500)
    test_set_ex(2000)

test_set()