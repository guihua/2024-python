# Redis 是一个基于内存的数据库，它可以用来存储键值对，也可以用来存储字符串、列表、集合、有序集合等数据结构
from redis.client import Redis

# Redis连接
# Redis的连接是通过Redis类的构造函数来完成的
# 构造函数的参数有host、port、db、password、socket_timeout、socket_connect_timeout、socket_keepalive、socket_keepalive_options、max_connections等
# 可以通过host参数指定Redis服务器的地址，默认是IP_ADDRESS# 可以通过host参数指定Redis服务器的地址，默认是127.0.0.1
# 可以通过port参数指定Redis服务器的端口，默认是6379
# 可以通过db参数指定连接到哪个数据库，默认连接到0号数据库
# 也可以通过password参数指定密码
# 也可以通过socket_timeout参数指定连接超时时间
# 也可以通过socket_connect_timeout参数指定连接超时时间
# 也可以通过socket_keepalive参数指定是否启用keepalive
# 也可以通过socket_keepalive_options参数指定keepalive选项
# 也可以通过max_connections参数指定最大连接数
r = Redis(host='127.0.0.1', port=6379, db=0, password='guihua.pgh')
# 连接成功后，就可以使用Redis的命令了
# 例如，使用set命令设置一个键值对
r.set('foo', 'ok')
# 使用get命令获取一个键的值
res = r.get('foo')
# 因为我们在上面设置了foo键的值为ok，所以这里获取到的也是ok；如果键不存在，返回None
# 输出的内容是b'ok'，表示获取到的是一个字节串；所有从Redis中获取到的数据都是字节串，需要自己进行解码
print(type(res), res)

# 可以使用decode方法将字节串解码为字符串
str_res = res.decode(encoding='utf-8')
print(type(str_res), str_res)