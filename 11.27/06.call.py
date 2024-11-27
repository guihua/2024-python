# 定义一个名为 Student 的类，继承自 object 类
class Student(object):
    def __init__(self, name):
        """
        类的构造函数，用于初始化 Student 类的实例。
        :param name: 学生的名字
        """
        # 将传入的 name 参数赋值给实例的 name 属性
        self.name = name

    def __call__(self):
        """
        使 Student 类的实例可调用，当调用实例时，会执行此方法。
        打印出包含学生名字的信息。
        """
        # 打印包含学生名字的信息
        print("My name is %s." % self.name)


# 创建一个 Student 类的实例，传入名字 "Michael"
s = Student("Michael")
# 调用 Student 类的实例 s，会执行 __call__ 方法
s()
