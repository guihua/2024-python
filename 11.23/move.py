import math

# 定义一个函数，接收 x, y 坐标，以及移动的步数，以及移动的角度，返回移动后的新坐标
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny