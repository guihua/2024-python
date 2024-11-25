from fact import fact
from tower import hanoi

# 计算 5 的阶乘
f5 = fact(5)
# 计算 100 的阶乘
f100 = fact(100)
print(f5)
print(f100)

move = hanoi(3, 'A', 'B', 'C')
print(move)