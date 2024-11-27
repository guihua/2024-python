# 定义一个名为 Student 的类，继承自 object 类
class Student(object):
    def __init__(self):
        # 初始化学生对象的属性 name，将其赋值为 "Michael"
        self.name = "Michael"

    def __getattr__(self, attr):
        """
        当访问对象的属性不存在时，会调用此方法。
        它根据属性名称进行不同的处理。
        :param attr: 要访问的属性名称
        :return: 根据属性名称返回相应的值或抛出异常
        """
        # 如果访问的属性是 score，返回 99
        if attr == "score":
            return 99
        # 如果访问的属性是 age，返回一个匿名函数，调用该函数将返回 25
        if attr == "age":
            return lambda: 25
        # 对于其他不存在的属性，抛出 AttributeError 异常
        raise AttributeError("'Student' object has no attribute '%s'" % attr)

# 创建一个 Student 类的实例
s = Student()
# 打印学生的名字
print(s.name)
# 打印学生的分数，由于 score 属性不存在，会调用 __getattr__ 方法，返回 99
print(s.score)
# 打印学生的年龄，由于 age 属性不存在，会调用 __getattr__ 方法，返回一个匿名函数，调用该函数将返回 25
print(s.age())
# 尝试访问不存在的 grade 属性，会调用 __getattr__ 方法，抛出 AttributeError 异常
print(s.grade)
