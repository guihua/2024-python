from Screen import Screen

class Student(object):
    # 定义一个方法，通过 @property 装饰器把一个方法变成属性调用
    @property
    def score(self):
        return self._score

    # 定义一个方法，通过 @score.setter 装饰器把一个方法变成属性赋值
    @score.setter
    def score(self, value):
        # 对赋值做检查
        if not isinstance(value, int):
            raise ValueError("score must be an integer!")
        if value < 0 or value > 100:
            raise ValueError("score must between 0 ~ 100!")
        self._score = value

s = Student() # 定义实例
s.score = 60 # 赋值，调用 @score.setter 装饰器的方法
print("s.score =", s.score)
# ValueError: score must between 0 ~ 100!
# s.score = 9999

# 创建 Screen 实例
screen = Screen(1920, 1080)
print("Width:", screen.width)
print("Height:", screen.height)
print("Resolution:", screen.resolution)
# 尝试修改只读属性 resolution，会引发 AttributeError
# screen.resolution = 1000  # 取消注释会报错