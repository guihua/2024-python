import time
from redis.client import Redis

# 创建Redis客户端
r = Redis(host='127.0.0.1', port=6379, db=0, password='guihua.pgh')

def sub():
    # 返回发布订阅对象，通过这个对象你能1）订阅频道 2）监听频道中的消息
    pub = r.pubsub()
    # 订阅一个channel
    pub.subscribe('int_channel')
    while True:
        msg = pub.parse_response()
        print(msg)


if __name__ == '__main__':
    sub()