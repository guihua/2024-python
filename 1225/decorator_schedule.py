import time
from schedule import repeat, every, run_pending

# repeat 装饰器用于设置任务的执行间隔时间，参数为时间间隔的单位，如 seconds、minutes、hours、days、weeks 等
# 这里的 repeat 装饰器相当于上面的 schedule.every().day.at("14:45").do(send_email)
# repeat 装饰器可以设置多个，如下面的 @repeat(every(10).seconds) 和 @repeat(every(5).seconds)
# 这里的 @repeat(every(10).seconds) 表示每隔 10 秒执行一次 send_email() 函数
# 这里的 @repeat(every(5).seconds) 表示每隔 5 秒执行一次 send_email() 函数
@repeat(every(10).seconds)
@repeat(every(5).seconds)
def send_email():
    # 发送邮件的操作可以加在这里
    print("Sending email...")

while True:
    # 每隔 1 秒检查一次是否有任务需要执行
    # 如果有任务需要执行，则执行该任务；如果没有任务需要执行，则继续等待
    # run_pending() 方法会检查所有已计划的任务，并执行那些已经到达时间的任务
    run_pending()
    time.sleep(1)