from contextlib import closing
from urllib.request import urlopen

# 使用 closing 装饰器
# 该函数的作用是在进入上下文时执行 __enter__ 方法，退出上下文时执行 __exit__ 方法
# __enter__ 方法打印 "Begin"，返回 urlopen 对象
# __exit__ 方法打印 "End"
with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)