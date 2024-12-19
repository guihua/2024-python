import time
from datetime import datetime, timedelta
from redis.client import Redis

# 创建Redis客户端
r = Redis(host='127.0.0.1', port=6379, db=0, password='guihua.pgh')

r.set('foo', 'ok')
# 设置键的过期时间
# expireat 方法设置键的过期时间，参数是键的名称和过期时间，过期时间是一个时间戳，单位是秒
# expireat 方法返回一个整数，表示设置过期时间的结果，1表示设置成功，0表示设置失败
# timedelta 方法返回一个时间差，单位是秒
# datetime.now() + timedelta(seconds=5) 返回一个时间戳，5秒后
r.expireat('foo', datetime.now() + timedelta(seconds=5))

# sleep 方法暂停程序的执行，参数是暂停的时间，单位是秒
# sleep 方法不会阻塞程序的执行，而是让程序暂停一段时间，然后继续执行后面的代码
# sleep 方法可以用来模拟程序的执行时间，例如模拟网络延迟，模拟程序的执行时间等
# sleep 方法可以用来测试程序的性能，例如测试程序的响应时间，测试程序的吞吐量等
# sleep 方法可以用来测试程序的正确性，例如测试程序的正确性，测试程序的正确性等
time.sleep(4)
print(r.get('foo'))

# 再次睡眠1.5秒，查看键是否过期
# 键foo的过期时间是5秒，所以在第4秒时，键foo的值为ok，在第5秒时，键foo的值为None
time.sleep(1.5)
print(r.get('foo'))