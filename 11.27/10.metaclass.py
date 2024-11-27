# 定义一个名为 ListMetaclass 的元类，继承自 type 类
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        """
        元类的 __new__ 方法，用于创建类对象。
        :param cls: 元类本身
        :param name: 要创建的类的名称
        :param bases: 要创建的类的父类
        :param attrs: 要创建的类的属性字典
        """
        # 为类添加一个名为 add 的方法，该方法将元素添加到列表中
        attrs["add"] = lambda self, value: self.append(value)
        # 使用 type 的 __new__ 方法创建类对象
        return type.__new__(cls, name, bases, attrs)


# 定义一个名为 MyList 的类，继承自 list 类，使用 ListMetaclass 作为元类
class MyList(list, metaclass=ListMetaclass):
    pass


# 创建一个 MyList 类的实例
L = MyList()
# 使用 add 方法添加元素 1
L.add(1)
# 使用 add 方法添加元素 2
L.add(2)
# 使用 add 方法添加元素 3
L.add(3)
# 使用 add 方法添加元素 "END"
L.add("END")
# 打印列表 L 的内容
print(L)
