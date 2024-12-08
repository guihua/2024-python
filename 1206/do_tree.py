# turtle 是Python的标准GUI库，使用Tkinter可以快速简单地创建GUI应用程序
from turtle import *

# colormode() 函数用于设置画笔的颜色模式，有两种模式：
# 1. RGB:red, green, blue，取值范围是0~1.0
#   例如：red=0.8, green=0.8, blue=0.8
# 2. CMYK:cyan, magenta, yellow, black，取值范围是0~255
#   例如：cyan=0, magenta=0, yellow=0, black=0
# 默认的颜色模式是RGB模式
# colormode() 函数必须在调用其他绘图函数之前调用，否则会报错
colormode(255)

# lt() 函数用于设置画笔的方向，单位为度，默认的方向是向右
lt(90)

# lv 是树的深度，l 是树的长度，s 是树的角度，宽度是树的宽度，宽度越大，树越粗
lv = 14
l = 120
s = 45

# 绘制树的宽度，宽度越大，树越粗
# width() 函数用于设置画笔的宽度，单位为像素，默认的宽度是1
width(lv)

# 绘制树的颜色，颜色可以是字符串，也可以是RGB值，例如：'red'、'#ff0000'、(255, 0, 0)，默认的颜色是黑色
r = 0
g = 0
b = 0
# pencolor() 函数用于设置画笔的颜色，颜色可以是字符串，也可以是RGB值，例如：'red'、'#ff0000'、(255, 0, 0)，默认的颜色是黑色
pencolor(r, g, b)

# penup() 函数用于抬起画笔，即不绘制图形，penup() 函数必须在调用其他绘图函数之前调用，否则会报错
penup()
# bk() 函数用于向后移动画笔，单位为像素，默认的距离是1
bk(l)
# pendown() 函数用于放下画笔，即开始绘制图形，pendown() 函数必须在调用其他绘图函数之前调用，否则会报错
pendown()
# fd() 函数用于向前移动画笔，单位为像素，默认的距离是1
fd(l)

# 绘制树的函数，l 是树的长度，level 是树的深度
# 函数的参数 l 和 level 都是整数，l 是树的长度，level 是树的深度，level 越大，树越粗
def draw_tree(l, level):
    # global 语句用于声明变量 r、g、b 是全局变量，否则会报错
    global r, g, b

    w = width()

    width(w * 3.0 / 4.0)

    r = r + 1
    g = g + 2
    b = b + 3
    pencolor(r % 200, g % 200, b % 200)

    l = 3.0 / 4.0 * l

    # lt() 函数用于设置画笔的方向，单位为度，默认的方向是向右
    lt(s)
    # fd() 函数用于向前移动画笔，单位为像素，默认的距离是1
    fd(l)

    # 绘制树的函数，l 是树的长度，level 是树的深度
    if level < lv:
        draw_tree(l, level + 1)

    # bk() 函数用于向后移动画笔，单位为像素，默认的距离是1
    bk(l)
    # rt() 函数用于设置画笔的方向，单位为度，默认的方向是向右
    rt(2 * s)
    # fd() 函数用于向前移动画笔，单位为像素，默认的距离是1
    fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    lt(s)

    width(w)

# speed() 函数用于设置画笔的速度，单位为像素，默认的速度是6，最快的速度是0，最慢的速度是10
# speed() 函数必须在调用其他绘图函数之前调用，否则会报错
# normal 是正常的速度，fast 是快速的速度，fastest 是最快的速度，slowest 是最慢的速度
speed("fastest")

draw_tree(l, 4)

done()