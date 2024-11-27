# 定义一个名为 Hello 的类，继承自 object 类
class Hello(object):
    def hello(self, name='world'):
        """
        定义一个名为 hello 的方法，用于打印问候语。
        :param name: 要问候的对象，默认为 'world'
        """
        # 打印包含 name 的问候语
        print('Hello, %s.' % name)

# 创建一个 Hello 类的实例
h = Hello()
# 调用 Hello 类实例的 hello 方法，使用默认参数 'world'
h.hello()
# 打印 Hello 类的类型
print(type(Hello))
# 打印 Hello 类实例 h 的类型
print(type(h))
