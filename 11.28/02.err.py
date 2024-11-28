def foo(s):
    """
    此函数用于将输入的字符串 s 转换为整数，并将 10 除以该整数。
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
    """
    bar("0")


main()
