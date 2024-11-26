from student import Student

# 实例化对象
# 调用对象的方法, 打印属性
lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())

bart.age = 8
print(bart.age)
# print(lisa.age)
