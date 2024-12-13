def consumer():
    # 初始化结果变量
    r = ''
    while True:
        # 从生成器接收数据，并将结果存储在 n 中
        n = yield r
        if not n:
            # 若接收到的数据为空，则结束生成器的执行
            return
        # 打印消费信息
        print('[CONSUMER] Consuming %s...' % n)
        # 更新结果
        r = '200 OK'

def produce(c):
    # 启动生成器
    c.send(None)
    # 初始化计数器
    n = 0
    while n < 5:
        # 计数器加 1
        n = n + 1
        # 打印生产信息
        print('[PRODUCER] Producing %s...' % n)
        # 向生成器发送数据，并接收结果
        r = c.send(n)
        # 打印生成器返回的结果
        print('[PRODUCER] Consumer return: %s' % r)
    # 关闭生成器
    c.close()


c = consumer()
produce(c)
