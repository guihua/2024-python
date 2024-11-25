# tuple 元组, 有序的集合，和 list 非常类似，但是 tuple 一旦初始化就不能修改，没有 append(), insert(), pop() 等方法
t = (1, 2)
print(t)

# y 元组只有一个元素时，需要在元素后面加一个逗号，否则，Python 会把括号当作运算符使用
t1 = (1,)
print(t1)

# 不加逗号，Python 会把括号当作运算符使用
t2 = (1)
print(t2)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Bob']
]

# 打印 Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Bob:
print(L[2][2])