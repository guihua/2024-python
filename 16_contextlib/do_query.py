class Query(object):
    # 初始化方法，初始化name属性，name是查询的对象
    def __init__(self, name):
        self.name = name

    # 上下文管理器，实现__enter__和__exit__
    # 1. __enter__方法在with语句开始时被调用
    # 2. __exit__方法在with语句结束时被调用
    def __enter__(self):
        print('Begin')
        return self

    # 3. __exit__方法可以接收3个参数
    #    exc_type:异常类型
    #    exc_value:异常值
    #    traceback:异常的调用栈
    #    如果没有异常，exc_type、exc_value和traceback都是None
    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    # 查询方法，输出查询信息
    def query(self):
        print('Query info about %s...' % self.name)