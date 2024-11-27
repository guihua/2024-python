# 定义一个名为 Fib 的类，继承自 object 类
class Fib(object):
    # 定义 __getitem__ 方法，使对象可以使用 [] 运算符进行索引操作
    def __getitem__(self, n):
        # 判断 n 是否为整数
        if isinstance(n, int):
            # 初始化斐波那契数列的前两个数
            a, b = 1, 1
            # 生成斐波那契数列的第 n 项
            for x in range(n):
                a, b = b, a + b
            # 返回第 n 项的值
            return a
        # 判断 n 是否为切片对象
        if isinstance(n, slice):
            # 获取切片的起始位置
            start = n.start
            # 获取切片的结束位置
            stop = n.stop
            # 如果起始位置为 None，则将起始位置设为 0
            if start is None:
                start = 0
            # 初始化斐波那契数列的前两个数
            a, b = 1, 1
            # 存储切片结果的列表
            L = []
            # 生成斐波那契数列
            for x in range(stop):
                # 如果当前位置大于等于起始位置，则添加到列表中
                if x >= start:
                    L.append(a)
                # 计算下一个斐波那契数
                a, b = b, a + b
            # 返回切片结果列表
            return L


# 创建一个 Fib 类的实例
f = Fib()
# 打印斐波那契数列的第 0 项
print(f[0])
# 打印斐波那契数列的第 5 项
print(f[5])
# 打印斐波那契数列的第 100 项
print(f[100])
# 打印斐波那契数列的第 0 项到第 4 项
print(f[0:5])
# 打印斐波那契数列的前 10 项
print(f[:10])
