import socket

# 客户端，使用UDP协议
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in [b"Michael", b"Tracy", b"Sarah"]:
    # 发送数据，使用UDP协议，不需要建立连接，直接发送数据即可
    s.sendto(data, ("127.0.0.1", 9999))
    # 接收数据，使用UDP协议，不需要建立连接，直接接收数据即可
    print(s.recv(1024).decode("utf-8"))

# 关闭连接
s.close()
