import logging

def foo(s):
    """
    此函数将输入的字符串 s 转换为整数，并将 10 除以该整数。
    :param s: 输入的字符串，将被转换为整数
    :return: 10 除以转换后的整数的结果
    """
    return 10 / int(s)


def bar(s):
    """
    此函数调用 foo 函数并将结果乘以 2。
    :param s: 输入的字符串，将传递给 foo 函数
    :return: foo 函数结果乘以 2 的结果
    """
    return foo(s) * 2


def main():
    """
    此函数调用 bar 函数并传入字符串 "0"。
    若 bar 函数调用引发异常，将使用 logging.exception 记录异常信息。
    """
    try:
        # 调用 bar 函数并传入字符串 "0"
        bar("0")
    except Exception as e:
        # 若发生异常，使用 logging.exception 记录异常信息
        logging.exception(e)


# 调用 main 函数
main()
# 打印 "END" 表示程序结束
print("END")
