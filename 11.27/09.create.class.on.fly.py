# 定义一个名为 fn 的函数，它接受一个参数 name，默认为 "world"
def fn(self, name="world"):
    """
    此函数用于打印包含 name 的问候语。
    :param name: 要问候的对象，默认为 "world"
    """
    # 打印包含 name 的问候语
    print("Hello, %s." % name)


# 使用 type 函数动态创建一个名为 Hello 的类，继承自 object 类，包含一个名为 hello 的方法，该方法由 fn 函数提供
Hello = type("Hello", (object,), dict(hello=fn))

# 创建一个 Hello 类的实例
h = Hello()

# 打印调用 h.hello() 的信息
print("call h.hello():")

# 调用 Hello 类实例 h 的 hello 方法
h.hello()

# 打印 Hello 类的类型
print("type(Hello) =", type(Hello))
# 打印 Hello 类实例 h 的类型
print("type(h) =", type(h))
