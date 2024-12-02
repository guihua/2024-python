from collections import Counter

# Counter 是一个简单的计数器，用于统计字符出现的个数，返回一个字典，key 是字符，value 是出现的次数
# Counter 继承自 dict，所以它也是一个无序的容器，key 是有序的，value 是无序的
# Counter 是一个 dict 的子类，所以它可以使用 dict 的所有方法
c = Counter('programming')

for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)

# 可以使用 update 方法，一次update一个字符，也可以一次update多个字符
c.update('hello')
print(c)