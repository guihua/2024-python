from collections import namedtuple

# 定义一个元组，元组的名字为Point，元组的元素为x和y
# 元组的作用是存储坐标，然后可以通过p.x和p.y获取坐标
# namedtuple 是一个函数，函数的作用是创建一个元组，元组的元素为x和y，元组的名字为Point，元组的元素可以通过p.x和p.y获取，也可以通过p[0]和p[1]获取
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)

# 判断p是否是Point类型和tuple类型的实例，如果是则返回True，否则返回False
print(isinstance(p, Point), isinstance(p, tuple))