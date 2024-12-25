import time
# schedule 模块用于定时任务
# 安装：pip install schedule
# schedule 模块的核心是 Schedule 类，它包含了一个 run_pending() 方法，用于执行所有已计划的任务。
# 它会检查所有已计划的任务，并执行那些已经到达时间的任务。
# 它还包含了一些方法，用于添加新的任务，如 every()、at()、do() 等。
# 它还包含了一些方法，用于取消已计划的任务，如 cancel_job() 等。
import schedule

def send_email():
    # 发送邮件的操作可以加在这里
    print("Sending email...")

# every() 方法用于设置间隔时间，参数为时间间隔的单位，如 seconds、minutes、hours、days、weeks 等
# day 表示每天执行一次
# at() 方法用于设置具体的执行时间，如 "14:45" 表示每天下午 2:45 执行一次
# do() 方法用于指定要执行的函数
schedule.every().day.at("14:45").do(send_email)

while True:
    # 每隔 1 秒检查一次是否有任务需要执行
    # 如果有任务需要执行，则执行该任务；如果没有任务需要执行，则继续等待
    # run_pending() 方法会检查所有已计划的任务，并执行那些已经到达时间的任务
    schedule.run_pending()
    time.sleep(1)