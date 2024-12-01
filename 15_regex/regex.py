import re

# 匹配邮箱地址的正则表达式
# 1. 以字母或数字开头
# 2. 以字母或数字结尾
# 3. 中间可以有字母、数字、点、下划线
# 4. 点和下划线可以出现多次
# 5. 点和下划线不能连续出现
# 6. 点和下划线不能出现在开头和结尾
# 7. 点和下划线不能出现在中间的@符号之前或之后
# 8. 点和下划线不能出现在中间的@符号之间
def is_valid_email(addr):
    if re.match(r'^[a-zA-Z0-9\.]+@[a-zA-Z0-9\.]+$', addr):
        return True
    else:
        return False

# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')