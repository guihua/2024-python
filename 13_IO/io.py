# 读文件
# 要以读文件的模式打开一个文件对象，使用Python内置的open()函数，传入文件名和标示符
# 标示符 r 表示读，w 表示写，a 表示追加，rb 表示读二进制文件，wb 表示写二进制文件

# 文件路径可以是相对路径，也可以是绝对路径
# 如果是相对路径，就表示当前目录的位置；如果是绝对路径，就表示当前磁盘的位置
file1 = open('/Users/guihua.pgh/workspace/python/2024-study/13_IO/test.txt', 'r')
# 调用read()会一次性读取文件的全部内容，Python把内容读到内存，用一个str对象表示
str1 = file1.read()
print(str1)
# 最后一步是调用close()方法关闭文件
# 文件使用完毕后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件数量也是有限的
file1.close()

# 文件不存在，open()函数就会抛出一个IOError的错误，并且给出错误码和详细的信息告诉你文件不存在
# test.txt 文件存在于当前目录，但通过相对路径，不知道为何读不出来
try:
    file2 = open('test.txt', 'r')
    str2 = file2.read()
    print(str2)
# 无论是否出错都能执行的代码
finally:
    if file2:
        file2.close()
# output -------------------
# Traceback (most recent call last):
#   File "/Users/guihua.pgh/workspace/python/2024-study/13_IO/file.py", line 12, in <module>
#     file2 = open('test.txt', 'r')
#             ^^^^^^^^^^^^^^^^^^^^^
# FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'

with open('/Users/guihua.pgh/workspace/python/2024-study/13_IO/test.txt', 'r') as file3:
    print(file3.read())