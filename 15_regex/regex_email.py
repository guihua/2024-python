import re

# 提取邮箱地址的正则表达式
# 1. 以字母或数字开头
# 2. 以字母或数字结尾
# 3. 中间可以有字母、数字、点、下划线
# 4. 点和下划线可以出现多次
# 5. 点和下划线不能连续出现
# 6. 点和下划线不能出现在开头和结尾
# 7. 点和下划线不能出现在中间的@符号之前或之后
# 8. 点和下划线不能出现在中间的@符号之间
def name_of_email(addr):
    if '<' in addr:
        return re.search(r'<([A-Za-z ]+)>', addr).group(1)
    else:
        return re.search(r'([A-Za-z ]+)', addr).group(1)

# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')