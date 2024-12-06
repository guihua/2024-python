from turtle import *

# 五角星的绘制
# 其中：
# x 和 y 分别表示五角星的中心坐标
# size 表示五角星的大小，即五角星的外接圆的半径
# color 表示五角星的颜色
def drawStar(x, y):
    # pu() 表示 penup()，即抬起画笔，不绘制图形
    pu()

    # goto(x, y) 表示将画笔移动到 (x, y) 坐标处，不绘制图形
    goto(x, y)

    # pd() 表示 pendown()，即放下画笔，开始绘制图形
    pd()

    # seth(0) 表示将画笔的方向设置为 0 度，即正右方
    seth(0)

    # 由于五角星是一个五边形，因此需要旋转 144 度才能绘制出一个五角星
    # 因此需要循环 5 次，每次旋转 144 度，绘制一个角
    for i in range(5):
        # fd(40) 表示向前移动 40 个像素
        fd(40)
        # rt(144) 表示向右旋转 144 度，绘制一个角
        rt(144)

for x in range(0, 250, 50):
    drawStar(x, 0)

done()