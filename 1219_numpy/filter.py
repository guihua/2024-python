import numpy as np

array = np.arange(1, 9)
# 筛选数组中的元素，只保留偶数
array1 = array[array % 2==0]
print(array1)

# 与或运算，使用 & | 运算符
# 筛选数组中的元素，只保留大于3且为偶数的元素
array_1 = array[(array > 3) & (array % 2 == 0)]
print(array_1)
# 筛选数组中的元素，只保留大于6或者为偶数的元素
array_2 = array[(array > 6) | (array % 2 == 0)]
print(array_2)