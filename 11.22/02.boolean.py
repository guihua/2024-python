# 与运算，只有所有都为 True，与运算的结果才是 True
print(True and True)
print(True and False)
print(False and False)

# 或运算，只要其中有一个为 True，或运算的结果就是 True
print(True or False)
print(False or False)

# 非运算，它是一个单目运算符，把 True 变成 False，False 变成 True
print(not True)
print(not False)

age = input('请输入你的年龄: ');
age = int(age)
if age >= 18:
    print('adult')
else:
    print('teenager')