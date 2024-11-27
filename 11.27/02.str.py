# 定义Student类，继承object
class Student(object):
    def __init__(self, name):
        self.name = name # 姓名

    # 用于格式化输出，返回一个字符串
    def __str__(self):
        return "Student object (name: %s)" % self.name

    # repr() 用于格式化输出，返回一个字符串
    # str 和 repr 的区别是, str 是为了打印，而 repr 为了调试
    __repr__ = __str__

print(Student("Michael"))