import chardet

# chardet 库是一个用于检测编码的库，它可以根据字节流的内容来猜测编码
# chardet 库的使用非常简单，只需要调用 chardet.detect() 函数即可
# chardet.detect() 函数的参数是一个字节流，它的值是一个 bytes 类型的对象
# chardet.detect() 函数的返回值是一个 dict，它的键是编码，它的值是一个 float，它的单位是百分比
cd1 = chardet.detect(b'Hello, world!')
print(cd1)

data1 = '离离原上草，一岁一枯荣'.encode('gbk')
cd2 = chardet.detect(data1)
print(cd2)

data2 = '离离原上草，一岁一枯荣'.encode('utf-8')
cd3 = chardet.detect(data2)
print(cd3)

data3 = '最新の主要ニュース'.encode('euc-jp')
cd4 = chardet.detect(data3)
print(cd4)