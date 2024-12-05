import requests

# 发送 GET 请求
r = requests.get('https://www.douban.com/') # 豆瓣首页
# 打印响应状态码
# 200 表示请求成功，404 表示请求失败
print(r.status_code)
# 打印响应头，它的值是一个 dict，它的键是响应头的名字，值是响应头的值
print(r.headers)
# 打印响应内容的二进制数据，它的值是一个 bytes，它的长度是响应内容的二进制数据的长度
print(r.content)
# 打印响应内容的二进制数据的长度
print(len(r.content))
# 打印响应内容的二进制数据的类型
print(type(r.content))
print(r.text)