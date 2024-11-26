from add import add, f
from normalize import normalize, prod

print(add(abs, -10, 20, -30, -40))

r = map(f, list(range(10)))
print(list(r))

# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')