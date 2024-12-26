from time import sleep
from reloading import reloading

# reloading 装饰器用于在控制台中显示进度条
@reloading
def half_value(value):
    print(f"value = {value}")
    value = value/2
    return value

value = 100
iterations = 10

for iteration in range(iterations):
    value = half_value(value)
    sleep(2)