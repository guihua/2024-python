import argparse

# 定义一个函数，用于发送邮件
# 可以使用默认参数，也可以使用命令行参数
def send_email(email="default_email@yeah.net"):
    # 发送邮件的操作可以加在这里
    print(f"Sending email...: to {email}")

if __name__ == "__main__":
    # 使用 argparse 模块来解析命令行参数
    parser = argparse.ArgumentParser()
    # 添加参数
    # -e, --email 表示可选参数，-e 表示短参数，--email 表示长参数
    # -e 表示短参数，--email 表示长参数
    # help 参数表示帮助信息
    # add_argument() 方法用于添加参数
    parser.add_argument("-e", "--email", help="Email to send")
    # 解析参数，将命令行参数解析成一个命名空间
    args = parser.parse_args()

    # 调用 send_email() 函数，将命令行参数传递给函数
    # 如果命令行参数中没有 -e 或 --email 参数，则使用默认参数
    # 如果命令行参数中包含 -e 或 --email 参数，则使用命令行参数
    if args.email:
        send_email(args.email)
    else:
        send_email()