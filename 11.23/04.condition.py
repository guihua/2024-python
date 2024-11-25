age = 3

# if 语句判断条件是否成立
# 条件成立时，执行 if 语句块，否则，执行 else 语句块, 可以没有 else 语句
# elif 是 else if 的缩写
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')


birth = input('birth: ')
# 强制转换类型, 否则，输入的是字符串, 无法比较, 会报错
birth = int(birth)
if birth < 2000:
    print('00前')
else:
    print('00后')

# BMI 指数计算：
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
height = 1.75
weight = 80.5

bmi = weight / height ** 2

if bmi < 18.5:
    print('过轻')
elif bmi < 25:
    print('正常')
elif bmi < 28:
    print('过重')
elif bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')