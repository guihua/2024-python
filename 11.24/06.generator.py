from fibonacci import fib
from triangles import triangles

# 列表推导式
L = [x * x for x in range(10)]
print(L)

# 生成器
g = (x * x for x in range(10))
print(g)
# 生成器的使用，使用next()函数获得下一个返回值
# print(next(g))
# print(next(g))

# 使用for循环迭代生成器的元素
for n in g:
    print(n)

print(fib(10))

n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')