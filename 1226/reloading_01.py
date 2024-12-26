from time import sleep
# reloading 模块用于在控制台中显示进度条
# 安装：pip install reloading
# reloading 函数的参数是一个可迭代对象，例如 range(iterations)。
# 在每次迭代中，reloading 函数会更新进度条，并在每次迭代结束时调用回调函数。
from reloading import reloading

value = 100
iterations = 10

# 模拟进度条
# reloading() 函数会在每次迭代结束时调用回调函数。
for iteration in reloading(range(iterations)):
    print(f"Value = {value}")
    # 模拟耗时操作
    value = value/2
    # 暂停 2 秒
    sleep(2)