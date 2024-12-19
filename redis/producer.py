import time
from redis.client import Redis

# 创建Redis客户端
r = Redis(host='127.0.0.1', port=6379, db=0, password='guihua.pgh')

# 生产者，将10个整数放入队列中
def producer():
    for i in range(10):
        # lpush 命令的参数是键和值，返回值是队列的长度
        # 队列的长度是队列中元素的个数，从左到右，从0开始编号
        # 队列的长度可以通过 llen 命令获取
        r.lpush('int_queue', i)
        time.sleep(1)

if __name__ == '__main__':
    producer()