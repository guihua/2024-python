import time
from redis.client import Redis

# 创建Redis客户端
r = Redis(host='127.0.0.1', port=6379, db=0, password='guihua.pgh')

# 定义消费者函数，从队列中取出数据并消费
def consumer():
    while True:
        # rpop 命令的参数是键，返回值是键的值，键的值必须是字符串
        # rpop 命令从队列中取出最右边的元素，即最新的元素
        data = r.rpop('int_queue')
        if data is None:
            time.sleep(0.5)
            continue

        # 打印取出的数据
        print(data)

if __name__ == '__main__':
    consumer()