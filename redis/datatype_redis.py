from redis.client import Redis

# Redis 连接
r = Redis(host='127.0.0.1', port=6379, db=0, password='guihua.pgh')
r.set('score', '100')
res = r.get('score')
# 可以使用 get 方法获取一个键的值，返回一个字节串
print(type(res), res)
# 可以使用 delete 方法删除一个键
# r.delete('score')

r.set('001', '97')
r.set('002', '98')
r.set('003', '99')
# 可以使用 mget 方法获取多个键的值，返回一个列表
res = r.mget('001', '002', '003')
print(type(res), res)
# 可以使用 delete 方法删除多个键，参数是多个键的名称
# r.delete('001', '002', '003')

# 可以使用 hmset 方法设置一个哈希表，第一个参数是哈希表的名称，后面的参数是键值对
# r.hmset('004', {'english': 90, 'physics': 87,'math': 92})
# hset 方法设置一个哈希表，第一个参数是哈希表的名称，后面的参数是键值对
r.hset('004', 'chinese', 95)
r.hset('004', 'math', 92)
# 也可以使用 hset 方法设置一个哈希表，第一个参数是哈希表的名称，后面的参数是键值对，键值对可以是一个字典
r.hset('004', mapping={'physics': 95,'english': 92})
# 可以使用 hgetall 方法获取一个哈希表的所有键值对，返回一个字典
res = r.hgetall('004')
print(type(res), res)
r.delete('004')