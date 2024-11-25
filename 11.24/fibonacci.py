def fib(max):
    """
    生成斐波那契数列，最大长度为 max。

    参数：
    max (int)：斐波那契数列的最大长度。

    生成：
    int：斐波那契数列中的元素。
    """
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
