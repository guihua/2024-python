# 导入 subprocess 模块，用于创建新的进程
import subprocess

print('$ nslookup')

# 使用 subprocess.Popen 函数创建一个新的进程，执行 nslookup 命令
# stdin、stdout 和 stderr 分别指定了进程的标准输入、标准输出和标准错误的管道
# 这里将它们都设置为 subprocess.PIPE，以便可以通过 communicate 方法进行交互
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# 向进程的标准输入发送数据，这里发送了一系列的命令
# set q=mx 表示设置查询类型为 MX 记录（邮件交换记录）
# python.org 是要查询的域名
# exit 表示退出 nslookup 命令
# communicate 方法会等待进程结束，并返回输出和错误信息
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')

# 将输出信息从字节类型解码为 utf-8 编码的字符串并打印
print(output.decode('utf-8'))
# 打印进程的返回码，返回码为 0 通常表示成功，非零表示失败
print('Exit code:', p.returncode)
