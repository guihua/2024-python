import time
from redis.client import Redis

# 创建Redis客户端
r = Redis(host='127.0.0.1', port=6379, db=0, password='guihua.pgh')

# 发布消息
# 每隔1秒发布一个消息，一共发布10个消息
# 订阅者可以通过监听这个频道来获取消息
def publish():
    for i in range(10):
        r.publish('int_channel', i)
        time.sleep(1)

if __name__ == '__main__':
    publish()