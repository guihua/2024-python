import socket

# 创建一个socket，使用IPv4协议，使用UDP协议
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口
s.bind(("127.0.0.1", 9999))

print("Bind UDP on 9999...")

while True:
    # 接收数据
    data, addr = s.recvfrom(1024)
    print("Received from %s:%s." % addr)

    # 发送数据，使用UDP协议，不需要建立连接，直接发送数据即可
    reply = "Hello, %s!" % data.decode("utf-8")
    s.sendto(reply.encode("utf-8"), addr)
