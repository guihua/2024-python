# 定义一个名为 Fib 的类，继承自 object 类
class Fib(object):
    """
    这个类用于生成斐波那契数列。
    它实现了迭代器协议，通过 __iter__ 和 __next__ 方法来实现迭代功能。
    """
    def __init__(self):
        # 初始化斐波那契数列的前两个数，self.a 为 0，self.b 为 1
        self.a, self.b = 0, 1

    def __iter__(self):
        # 返回迭代器对象本身，这里是 self
        return self

    def __next__(self):
        # 更新斐波那契数列的下一个数，将 self.b 的值赋给 self.a，将 self.a + self.b 的值赋给 self.b
        self.a, self.b = self.b, self.a + self.b
        # 当生成的斐波那契数大于 100000 时，停止迭代
        if self.a > 100000:
            raise StopIteration()
        # 返回生成的斐波那契数
        return self.a


# 使用 for 循环遍历 Fib 类的实例，打印生成的斐波那契数列
for n in Fib():
    print(n)
