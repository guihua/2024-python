class Screen(object):
    # 构造方法，初始化 width 和 height 属性
    def __init__(self, width, height):
        self._width = width
        self._height = height

    # 把一个方法变成属性调用
    # 此时 @property 本身又创建了另一个装饰器 @width.setter，负责把一个 setter 方法变成属性赋值，于是，我们就拥有一个可控的属性操作
    @property
    def width(self):
        return self._width

    # 把一个方法变成属性赋值
    @width.setter
    def width(self, value):
        # 对赋值做检查
        if not isinstance(value, (int, float)):
            raise ValueError("width must be a number!")
        self._width = value

    # 把一个方法变成属性调用
    # 此时 @property 本身又创建了另一个装饰器 @height.setter，负责把一个 setter 方法变成属性赋值，于是，我们就拥有一个可控的属性操作
    @property
    def height(self):
        return self._height

    # 把一个方法变成属性赋值
    @height.setter
    def height(self, value):
        # 对赋值做检查
        if not isinstance(value, (int, float)):
            raise ValueError("height must be a number!")
        self._height = value

    # 把一个方法变成属性调用, 只读属性，只定义getter方法，不定义setter方法
    @property
    def resolution(self):
        return self._width * self._height