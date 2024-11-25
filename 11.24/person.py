# 定义一个名为 person 的函数，接收三个参数：name、age 和关键字参数 kw
# 关键字参数可以传入任意个数的键值对，在函数内部自动组装为一个 dict, 也可以直接传入一个 dict, 这样函数内部会自动将其转换为关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)