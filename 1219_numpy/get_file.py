import numpy as np

# 读取文本文件
# numpy提供了loadtxt()函数和genfromtxt()函数用于从文本文件中加载数据
# loadtxt()函数和genfromtxt()函数的参数基本相同，都是文件名和分隔符
# loadtxt()函数和genfromtxt()函数的返回值是一个二维数组，数组的元素是文本文件中的数据
# loadtxt()函数和genfromtxt()函数的区别在于genfromtxt()函数支持更多的参数设置，比如跳过文本文件的前n行、使用掩码等，更加灵活

# loadtxt()函数和genfromtxt()函数的参数比较多，可以根据实际需求选择合适的函数：
# loadtxt 函数的第一个参数是文件名，第二个参数是分隔符，分隔符是文本文件中数据之间的分隔符，比如空格、逗号、制表符等
# loadtxt 函数默认的分隔符是空格，如果文本文件中的数据是用逗号分隔的，可以通过delimiter参数指定分隔符为逗号
# loadtxt 函数的第三个参数是数据类型，数据类型是文本文件中的数据的类型，比如int、float、str等
# loadtxt 函数默认的数据类型是float，如果文本文件中的数据是用逗号分隔的，可以通过dtype参数指定数据类型为int
# loadtxt 函数的第四个参数是skiprows，skiprows是跳过文本文件的前n行，比如skiprows=1表示跳过文本文件的第一行
# loadtxt 函数的第五个参数是comments，comments是注释符号，比如comments='#'表示#后面的内容是注释
# loadtxt 函数的第六个参数是unpack，unpack是解包，比如unpack=True表示解包
# loadtxt 函数的第七个参数是usecols，usecols是使用的列，比如usecols=(0, 1)表示只使用第0列和第1列
# loadtxt 函数的第八个参数是names，names是列名，比如names=('a', 'b')表示第0列的列名是a，第1列的列名是b
# loadtxt 函数的第九个参数是max_rows，max_rows是最大行数，比如max_rows=10表示最多读取10行
# loadtxt 函数的第十个参数是encoding，encoding是编码方式，比如encoding='utf-8'表示使用utf-8编码
# loadtxt 函数的第十一个参数是dtype，dtype是数据类型，比如dtype='float'表示数据类型是float
# loadtxt 函数的第十二个参数是comments，comments是注释符号，比如comments='#'表示#后面的内容是注释
# loadtxt 函数的第十三个参数是encoding，encoding是编码方式，比如encoding='utf-8'表示使用utf-8编码
# loadtxt 函数的第十四个参数是unpack，unpack是解包，比如unpack=True表示解包
# loadtxt 函数的第十五个参数是usemask，usemask是使用掩码，比如usemask=True表示使用掩码
# loadtxt 函数的第十六个参数是invalid_raise，invalid_raise是无效引发，比如invalid_raise=True表示无效引发

# genfromtxt 函数的第一个参数是文件名，第二个参数是分隔符，分隔符是文本文件中数据之间的分隔符，比如空格、逗号、制表符等
# genfromtxt 函数默认的分隔符是空格，如果文本文件中的数据是用逗号分隔的，可以通过delimiter参数指定分隔符为逗号
# genfromtxt 函数的第三个参数是数据类型，数据类型是文本文件中的数据的类型，比如int、float、str等
# genfromtxt 函数默认的数据类型是float，如果文本文件中的数据是用逗号分隔的，可以通过dtype参数指定数据类型为int
# genfromtxt 函数的第四个参数是skip_header，skip_header是跳过文本文件的前n行，比如skip_header=1表示跳过文本文件的第一行
# genfromtxt 函数的第五个参数是filling_values，filling_values是填充缺失值的方式，比如filling_values=0表示用0填充缺失值
# genfromtxt 函数的第六个参数是autostrip，autostrip是去除数据两端空格的方式，比如autostrip=True表示去除数据两端空格
# genfromtxt 函数的第七个参数是comments，comments是注释符号，比如comments='#'表示#后面的内容是注释
# genfromtxt 函数的第八个参数是deletechars，deletechars是删除字符，比如deletechars='!'表示删除!字符
# genfromtxt 函数的第九个参数是replace_space，replace_space是替换空格，比如replace_space='_'表示用_替换空格
# genfromtxt 函数的第十个参数是usecols，usecols是使用的列，比如usecols=(0, 1)表示只使用第0列和第1列
# genfromtxt 函数的第十一个参数是names，names是列名，比如names=('a', 'b')表示第0列的列名是a，第1列的列名是b
# genfromtxt 函数的第十二个参数是max_rows，max_rows是最大行数，比如max_rows=10表示最多读取10行
# genfromtxt 函数的第十三个参数是encoding，encoding是编码方式，比如encoding='utf-8'表示使用utf-8编码
# genfromtxt 函数的第十四个参数是unpack，unpack是解包，比如unpack=True表示解包
# genfromtxt 函数的第十五个参数是usemask，usemask是使用掩码，比如usemask=True表示使用掩码
# genfromtxt 函数的第十六个参数是invalid_raise，invalid_raise是无效引发，比如invalid_raise=True表示无效引发

# loadtxt 函数用于从文本文件中加载数据，参数是文件名和分隔符
array_1 = np.loadtxt('./1219_numpy/data.txt', delimiter=',')
print(array_1)

# genfromtxt 函数用于从文本文件中加载数据，参数是文件名和分隔符
array_2 = np.genfromtxt('./1219_numpy/data.txt', delimiter=',')
print(array_2)