import math
from abstest import my_abs
from move import move
from quadratic import quadratic

# print(my_abs('A'))
print(my_abs(-100))

print(move(100, 100, 60, math.pi / 6))

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')