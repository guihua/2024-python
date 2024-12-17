age = 18
valid = "你是成年人"
invalid = "你是未成年人"
# 单行代码，带条件判断的表达式
# 条件为真，返回valid，否则返回invalid
print(valid) if age >= 18 else print(invalid)

countries = ['united states', 'brazil', 'united kingdom', 'japan']
# 带条件判断的列表推导式，返回首字母为u的国家名字，并将首字母大写
# title()方法将字符串的首字母大写
# startswith()方法检查字符串是否以指定的前缀开头
# 列表推导式的语法：[expression for item in iterable if condition]
# 列表推导式的执行顺序：for item in iterable -> if condition -> expression
capitalized = [country.title() for country in countries if country.startswith('u')]
print(capitalized)

# 带条件判断的字典推导式，返回1-5的平方数
# 字典推导式的语法：{key_expression: value_expression for item in iterable if condition}
# 字典推导式的执行顺序：for item in iterable -> if condition -> key_expression: value_expression
dict_numbers = {x:x*x for x in range(1,6) }
print(dict_numbers)

dict_1 = {'a': 1, 'b': 2}
dict_2 = {'c': 3, 'd': 4}
# 合并字典，使用**运算符，将字典拆分为关键字参数
# **运算符将字典拆分为关键字参数，即将字典的键作为关键字，将字典的值作为参数
# 合并字典的语法：{**dict_1, **dict_2}
# 合并字典的执行顺序：**dict_1 -> **dict_2
merged_dict = {**dict_1, **dict_2}
print(merged_dict)

numbers = [1,1,1,2,2,3,4,5,6,7,7,8,9,9,9]
# 去重，使用set()函数，将列表转换为集合，再将集合转换为列表
# set()函数将列表转换为集合，集合中的元素不重复
# list()函数将集合转换为列表
# 去重的语法：list(set(numbers))
print(list(set(numbers)))

# 单行赋值多变量，使用逗号分隔，左边是变量名，右边是值
# 逗号分隔的语法：a, b, c = 1, "abc",  True
# 逗号分隔的执行顺序：1, "abc",  True -> a, b, c
a, b, c = 1, "abc",  True
print(a, b, c)

my_list = [10, 11, 12, 13, 14, 15]
# 选出所有偶数，使用filter()函数，将列表中的元素传入lambda表达式，返回True的元素
# filter()函数将列表中的元素传入lambda表达式，返回True的元素
# 选出所有偶数的语法：list(filter(lambda x: x%2 == 0, my_list ))
# 选出所有偶数的执行顺序：lambda x: x%2 == 0 -> filter() -> list()
print(list(filter(lambda x: x%2 == 0, my_list )))

product_prices = {'Z': 9.99, 'Y': 9.99, 'X': 9.99}
# 使用字典推导式，将字典中的键值对交换，返回一个新的字典
# keys()方法返回字典的所有键，values()方法返回字典的所有值
# sorted()函数将键排序，排序后的键作为新的字典的键，原来的值作为新的字典的值，返回一个新的字典
print({key:product_prices[key] for key in sorted(product_prices.keys())})

population = {'USA':329.5, 'Brazil': 212.6, 'UK': 67.2}
# 使用sorted()函数，将字典中的键值对排序，返回一个新的列表
# sorted()函数的key参数指定排序的依据，这里是按照值排序，即x[1]，返回一个新的列表
# lambda x: x[1] 表示按照值排序，即x[1]，返回一个新的列表
print(sorted(population.items(), key=lambda x:x[1]))
# 使用字典推导式，将排序后的列表转换为字典
print({k:v for k, v in sorted(population.items(), key=lambda x:x[1])})