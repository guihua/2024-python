from power import power
from person import person

# 计算 2 的 10 次方
print(power(2, 10))

# 计算 5 的 2 次方
print(power(5))

# 计算 5 的 3 次方
print(power(5, 3))

# 调用 person 函数，传入 name 和 age 参数
p1 = person('Michael', 30)
# 调用 person 函数，传入 name、age 和 city 参数
p2 = person('Bob', 35, city='Beijing')
# 调用 person 函数，传入 name、age、gender 和 job 参数
p3 = person('Adam', 45, gender='M', job='Engineer')
# 定义一个 dict，包含 city 和 job 两个键值对, 然后将其作为关键字参数传入 person 函数
extra = {'city': 'Beijing', 'job': 'Engineer'}
p4 = person('Jack', 24, **extra)
print(p1, p2, p3, p4)