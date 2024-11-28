def foo(s):
    """
    此函数将输入的字符串 s 转换为整数。
    若转换后的整数为 0，则引发 ValueError 异常。
    若不为 0，则将 10 除以该整数。
    :param s: 输入的字符串，将被转换为整数
    :return: 10 除以转换后的整数的结果
    """
    # 将输入的字符串 s 转换为整数
    n = int(s)
    if n == 0:
        # 当 n 为 0 时，引发 ValueError 异常，并输出错误信息
        raise ValueError("invalid value: %s" % s)
    # 当 n 不为 0 时，将 10 除以 n
    return 10 / n


def bar():
    """
    此函数调用 foo 函数。
    若 foo 函数引发 ValueError 异常，将打印错误信息并重新引发该异常。
    """
    try:
        # 调用 foo 函数并传入字符串 "0"
        foo("0")
    except ValueError as e:
        # 当捕获到 ValueError 异常时，打印错误信息
        print("ValueError!")
        # 重新引发该异常
        raise


# 调用 bar 函数
bar()
