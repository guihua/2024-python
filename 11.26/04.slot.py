#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 定义一个class，通过__slots__限制该class实例能添加的属性
class Student(object):
    __slots__ = ("name", "age") # 用tuple定义允许绑定的属性名称, 仅对当前类实例起作用，对继承的子类是不起作用的

# 定义子类，继承父类Student的所有功能
class GraduateStudent(Student):
    pass

# 定义实例
s = Student()
s.name = "Michael" # 绑定属性"name"
s.age = 25 # 绑定属性"age"
print("s.name =", s.name)
print("s.age =", s.age)

try:
    s.score = 99 # 绑定属性"score"，由于"score"没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误
except AttributeError as e:
    print("AttributeError:", e)

g = GraduateStudent() # 定义子类实例
g.score = 99 # 绑定属性"score"，由于子类没有__slots__，所以允许绑定score属性
print("g.score =", g.score) # 打印绑定的属性score，此时不会报错