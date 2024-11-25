names = ['Michael', 'Bob', 'Tracy']

# 遍历 list, 不需要关心 list 的长度，直接使用 for 循环, 不需要关心索引, 可以直接使用元素
# 可以使用变量 name 代表 list 中的元素
for name in names:
    print(name)


sum = 0

# 计算 1-10 的整数之和
# 可以使用变量 x 代表 list 中的元素
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

# 生成 1-10 的 list, 可以使用 range() 函数生成 1-10 的整数序列, 然后通过 list() 函数转换为 list
l0 = list(range(10))
print(l0)

# range() 函数可以指定起始值和结束值, 不包括结束值
for x in range(101):
    sum = sum + x
print(sum)

L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print(f'Hello, {name}!')