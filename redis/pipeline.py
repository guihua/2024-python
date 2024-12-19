from redis.client import Redis

# 创建Redis客户端
r = Redis(host='127.0.0.1', port=6379, db=0, password='guihua.pgh')

# 创建一个管道对象
# pipeline 是一个上下文管理器，使用 with 语句可以自动关闭管道对象
# pipeline 可以将多个命令打包成一个事务，然后一次性发送给 Redis 服务器，减少网络开销
# 使用 with 语句，在 with 语句块中执行的命令都会被打包到一个事务中，最后使用 execute() 方法执行事务
with r.pipeline()as p:
    for i in range(100):
        # 向管道中添加命令
        # 将命令添加到管道中，并不会立即执行命令，而是将命令添加到一个队列中，等待执行
        p.set(f'key_{i}', i)

    # 执行事务
    # execute() 方法执行事务，返回一个列表，列表中的元素是每个命令的返回值
    p.execute()

print(r.get('key_1'))