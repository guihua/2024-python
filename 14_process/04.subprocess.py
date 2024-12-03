import subprocess

print('$ nslookup www.python.org')
# 子进程
# 执行的函数为nslookup，参数为www.python.org
# nslookup 是一个命令行工具，用来查询DNS服务器，可以查询域名的IP地址
# subprocess.call()方法会立即返回，不会等待子进程执行完毕，而是继续往下运行，直到子进程执行完毕
r = subprocess.call(['nslookup', 'www.python.org'])

# nslookup 命令的返回值为0，表示执行成功，非0表示执行失败
print('Exit code:', r)