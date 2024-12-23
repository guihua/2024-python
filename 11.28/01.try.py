# try-except-finally 语句的使用，异常的捕获和处理，以及代码的执行流程
try:
    print("try...")
    # 尝试进行除法运算，除数为 0，会引发 ZeroDivisionError 异常，导致程序中断
    r = 10 / 0
    # 打印除法运算的结果
    # 由于会引发异常，此语句不会执行，也不会打印结果
    print("result:", r)
# 捕获 ZeroDivisionError 异常，并将异常对象赋值给变量 e
except ZeroDivisionError as e:
    # 打印异常信息
    print("except:", e)
# 无论是否发生异常，都会执行以下代码块
# 用于释放资源或清理工作
finally:
    print("finally...")

print("END")
