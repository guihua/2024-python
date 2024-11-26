from operator import itemgetter

# 排序
s1 = sorted([36, 5, -12, 9, -21])
s2 = sorted([36, 5, -12, 9, -21], key=abs)
print(s1, s2)

students = [("Bob", 75), ("Adam", 92), ("Bart", 66), ("Lisa", 88)]

print(sorted(students, key=itemgetter(0)))
print(sorted(students, key=lambda t: t[1]))
print(sorted(students, key=itemgetter(1), reverse=True))