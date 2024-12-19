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

# lpush 方法向列表的左侧插入一个或多个元素，第一个参数是列表的名称，后面的参数是元素的值，可以是一个或多个元素
r.lpush('fans', '001', '002', '003', '004', '005', '006')
# lrange 方法获取列表的一部分元素，第一个参数是列表的名称，后面的参数是起始位置和结束位置
# lrange 返回一个列表，列表中的元素是从起始位置到结束位置的元素
res = r.lrange('fans', 0, 3)
print(res)
# lpop 方法从列表的左侧弹出一个元素，返回被弹出的元素
res = r.lpop('fans')
print(res)
r.delete('fans')

# sadd 方法向集合添加一个或多个元素，第一个参数是集合的名称，后面的参数是元素的值，可以是一个或多个元素
r.sadd('001:friend', '002', '003', '004')
r.sadd('006:friend', '002', '003', '005')
# sinter 方法返回两个集合的交集，第一个参数是集合的名称，后面的参数是集合的名称，可以是一个或多个集合
res = r.sinter('001:friend', '006:friend')
print(res)
r.delete('001:friend', '006:friend')

# zadd 方法向有序集合添加一个或多个元素，第一个参数是有序集合的名称，后面的参数是元素的值，可以是一个或多个元素
r.zadd('game', {'xiaoming': 897, 'xiaohong': 900, 'xiaogang': 865, 'xiaoli': 903, 'xiaozhang': 987})
# zrevrange 方法返回有序集合的一部分元素，第一个参数是有序集合的名称，后面的参数是起始位置和结束位置
# zrevrange 返回一个列表，列表中的元素是从起始位置到结束位置的元素，元素的顺序是从大到小的顺序
res = r.zrevrange('game', 0, 2, withscores=True)
print(res)
r.zadd('game', {'xiaoli': 1000})
res = r.zrevrange('game', 0, 2, withscores=True)
print(res)
