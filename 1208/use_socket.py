# 导入socket库，用于网络通信
# 注意：这里的socket库是Python内置的库，不需要安装，直接导入即可
import socket

# 创建一个socket，使用IPv4协议，使用TCP协议
# AF_INET表示使用IPv4协议，SOCK_STREAM表示使用TCP协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接
# 参数是一个元组，包含服务器的地址和端口号
s.connect(('www.sina.com.cn', 80))

# 发送数据
# 使用bytes类型，以b开头表示这是bytes类型的数据，以\r\n结尾表示这是一个HTTP请求的结束标志
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# 接收数据
buffer = []
while True:
    # 每次最多接收1k字节，如果没有数据了，就退出循环
    d = s.recv(1024)
    if d:
        # 将接收到的数据添加到buffer中
        buffer.append(d)
    else:
        break

# 拼接数据，将buffer中的数据拼接成一个bytes类型的数据
data = b''.join(buffer)

# 关闭连接
s.close()