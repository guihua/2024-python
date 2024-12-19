from redis.client import Redis
import time

# 创建Redis客户端
r = Redis(host='127.0.0.1', port=6379, db=0, password='guihua.pgh')

r.set('foo', 'ok')
# 设置键 foo 的过期时间为 3 秒，3秒后键 foo 会被自动删除
# expire 方法设置键的过期时间，第一个参数是键的名称，第二个参数是过期时间，单位是秒
# 当键过期时，键会被自动删除
r.expire('foo', 3)

# sleep 方法暂停程序的执行，参数是暂停的时间，单位是秒
# 当程序暂停时，键 foo 还没有过期，所以可以获取到键的值
time.sleep(2)
print(r.get('foo'))

# 当程序暂停时，键 foo 已经过期，所以获取不到键的值
time.sleep(1.5)
print(r.get('foo'))