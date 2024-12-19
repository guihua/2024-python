from redis.client import Redis
from redis.client import WatchError

# 创建Redis客户端
r = Redis(host='127.0.0.1', port=6379, db=0, password='guihua.pgh')

# pipeline 可以将多个命令打包成一个事务，然后一次性发送给 Redis 服务器，减少网络开销
# 使用 with 语句，在 with 语句块中执行的命令都会被打包到一个事务中，最后使用 execute() 方法执行事务
with r.pipeline()as p:
    try:
        # 在 watch 方法中指定要监视的键，当这些键的值被修改时，事务会被取消执行
        p.watch('coolpython')
        # int 方法将字符串转换为整数，返回一个整数
        value = int(p.get('coolpython'))

        # multi 方法将当前的事务标记为一个事务，后面的命令都会被添加到这个事务中，最后使用 execute() 方法执行事务
        # 当事务执行时，如果监视的键的值被修改，事务会被取消执行，抛出 WatchError 异常
        p.multi()
        p.set('coolpython', value + 1)
        # execute() 方法执行事务，返回一个列表，列表中的元素是每个命令的返回值
        p.execute()
    except WatchError:
        print('coolpython 被修改')

print(r.get('coolpython'))