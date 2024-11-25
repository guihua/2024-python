# 导入 os 模块
import os

# 列表生成式, 生成一个1~10的列表,
L = list(range(1, 11))
print(L)

# 列表生成式, 生成一个1~10的列表, 并将每个元素乘以自己
L = [x * x for x in range(1, 11)]
print(L)

# 列表生成式, 生成一个1~10的列表, 并将每个元素乘以自己, 并过滤掉偶数
L = [x * x for x in range(1, 11) if x % 2 == 1]
print(L)

# 列表生成式, 生成一个1~10的列表, 并将每个元素乘以自己, 并过滤掉偶数, 并将结果转换为字符串
L = [str(x * x) for x in range(1, 11) if x % 2 == 1]
print(L)

# 双层循环, 生成一个全排列的列表
L = [m + n for m in 'ABC' for n in 'XYZ']
print(L)

# 列出当前目录下的所有文件和目录名
files = [d for d in os.listdir('.')]
print(files)

L1 = ['Hello', 'World', 18, 'Apple', None]
# 列表生成式, 生成一个全小写的列表, 并过滤掉非字符串元素
L2 = [x.lower() for x in L1 if isinstance(x, str)]
print(L2)

if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')