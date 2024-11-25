# list 列表, 有序的集合
classmates = ['Michael', 'Bob', 'Tracy']
# 获取 list 中的元素，索引从 0 开始，最后一个元素的索引是 len(classmates) - 1，超出索引会报错
print(classmates[0], classmates[1], classmates[2])
print(classmates)

# len() 函数获取 list 元素个数
len = len(classmates)
print(len)

# 追加元素到 list 末尾
classmates.append('Adam')
print(classmates)

# 追加元素到 list 指定位置
classmates.insert(1, 'Jack')
print(classmates)

# 删除 list 末尾的元素, 也可以指定位置
classmates.pop()
classmates.pop(1)
print(classmates)

# 替换 list 中的元素, 直接赋值给对应的索引位置
classmates[1] = 'Sarah';
print(classmates)