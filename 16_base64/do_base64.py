import base64

# b64编码
def safe_base64_decode(s):
    # 补位，将长度补成4的倍数
    # 长度%4 = 0，不补位
    if len(s) % 4!= 0:
        s += b'=' * (4 - len(s) % 4)
    return base64.b64decode(s) # 解码，返回bytes类型

assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')