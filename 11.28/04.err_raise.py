# 自定义异常类，继承自 ValueError
class FooError(ValueError):
    pass


def foo(s):
    """
    此函数将输入的字符串 s 转换为整数。
    若转换后的整数为 0，则引发自定义异常 FooError。
    若不为 0，则将 10 除以该整数。
    :param s: 输入的字符串，将被转换为整数
    :return: 10 除以转换后的整数的结果
    """
    # 将输入的字符串 s 转换为整数
    n = int(s)
    if n == 0:
        # 当 n 为 0 时，引发自定义异常 FooError，并输出错误信息
        raise FooError("invalid value: %s" % s)
    # 当 n 不为 0 时，将 10 除以 n
    return 10 / n

# 调用 foo 函数并传入字符串 "0"，会引发 FooError 异常
foo("0")
