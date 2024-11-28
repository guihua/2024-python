"""
自定义的 Dict 类，继承自内置的 dict 类。
提供了属性访问和设置的功能，当访问不存在的属性时会引发 AttributeError。
"""
class Dict(dict):
    """
    初始化方法，接收关键字参数并调用父类 dict 的初始化方法。
    :param kw: 关键字参数，将作为字典的键值对存储。
    """
    def __init__(self, **kw):
        super().__init__(**kw)

    """
    当访问不存在的属性时，尝试从字典中获取。
    :param key: 要访问的属性名称。
    :return: 对应的值，如果不存在则引发 AttributeError。
    """
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    """
    当设置属性时，将属性存储到字典中。
    :param key: 要设置的属性名称。
    :param value: 要设置的属性值。
    """
    def __setattr__(self, key, value):
        self[key] = value
